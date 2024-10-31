#!/usr/bin/env python3

# Copyright 2021-2023, NVIDIA CORPORATION & AFFILIATES. All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the distribution.
#  * Neither the name of NVIDIA CORPORATION nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS ``AS IS'' AND ANY
# EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
# PURPOSE ARE DISCLAIMED.  IN NO EVENT SHALL THE COPYRIGHT OWNER OR
# CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
# EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
# PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
# PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY
# OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
import ast
import glob
import json
import logging
import os
import shutil
from pathlib import Path

from mlflow.exceptions import MlflowException
from wtu_mlflow_triton_plugin.config import Config, check_env
from wtu_mlflow_triton_plugin.model_config import ModelConfig, InputOutput

import numpy as np

# import tritonclient.http as tritonhttpclient
import tritonclient.grpc as tritongrpcclient
from mlflow.deployments import BaseDeploymentClient
from mlflow.exceptions import MlflowException
from mlflow.models import Model
from mlflow.tracking.artifact_utils import _download_artifact_from_uri
from tritonclient.utils import (
    InferenceServerException,
    np_to_triton_dtype,
    triton_to_np_dtype,
)
from google.protobuf.json_format import MessageToJson
from typing import Optional

logger = logging.getLogger(__name__)

_MLFLOW_META_FILENAME = "mlflow-meta.json"


class TritonPlugin(BaseDeploymentClient):
    def __init__(self, uri: Optional[str] = None):
        check_env()
        """
        Initializes the deployment plugin, sets the triton model repo
        """
        super(TritonPlugin, self).__init__(target_uri=uri)
        self.server_config = Config()
        triton_url, self.triton_model_repo = self._get_triton_server_config()
        # need to add other flavors
        self.supported_flavors = ["triton", "onnx"]

        if triton_url.startswith("http://"):
            triton_url = triton_url[len("http://") :]
            ssl = False
        elif triton_url.startswith("https://"):
            triton_url = triton_url[len("https://") :]
            ssl = True
        else:
            raise ValueError(
                "Triton URL must start with http:// or https://. Got: {}".format(
                    triton_url
                )
            )
        print("Triton URL: {}, ssl: {}".format(triton_url, ssl))

        try:
            self.triton_client = tritongrpcclient.InferenceServerClient(
                url=triton_url,
                ssl=ssl,
                # verbose=True,
                # concurrency=5,        # in http
                # network_timeout=90,   # in http
            )
        except Exception as e:
            raise MlflowException(
                "Failed to connect to Triton server at {}. Error: {}".format(
                    triton_url, e
                )
            )

    def get_config(self, model_name):
        model_data = self.triton_client.get_model_metadata(
            model_name=model_name, as_json=True
        )
        return ModelConfig(
            name=model_data["name"],
            versions=model_data["versions"],
            platform=model_data["platform"],
            ready=self.triton_client.is_model_ready(model_name=model_name),
            inputs=[InputOutput(**inp) for inp in model_data["inputs"]],
            outputs=[InputOutput(**out) for out in model_data["outputs"]],
        )

    def init(self, name, model_uri, flavor="onnx", config=None):
        self._validate_flavor(flavor)

        # Verify model does not already exist in Triton
        if self._model_exists(name):
            raise Exception(
                "Unable to create deployment for name %s because it already exists."
                % (name)
            )

        # Get the path of the artifact
        path = Path(_download_artifact_from_uri(model_uri))

        print("Copy files to Triton repo...")
        self._copy_files_to_triton_repo(path, name, flavor)

        print("Generate mlflow meta file...")
        self._generate_mlflow_meta_file(name, flavor, model_uri)

        return name, flavor

    def create_deployment(self, name, model_uri, flavor="onnx", config=None):
        """
        Deploy the model at the model_uri to the Triton model repo. Associated config.pbtxt and *labels* files will be deployed.

        :param name: Name of the of the model
        :param model_uri: Model uri in format model:/<model-name>/<version-or-stage>
        :param flavor: Flavor of the deployed model
        :param config: Configuration parameters

        :return: Model flavor and name
        """
        self._validate_flavor(flavor)

        # Verify model does not already exist in Triton
        if self._model_exists(name):
            raise Exception(
                "Unable to create deployment for name %s because it already exists."
                % (name)
            )

        # Get the path of the artifact
        path = Path(_download_artifact_from_uri(model_uri))

        print(path)

        print("Copy files to Triton repo...")
        self._copy_files_to_triton_repo(path, name, flavor)

        print("Generate mlflow meta file...")
        self._generate_mlflow_meta_file(name, flavor, model_uri)

        try:
            print("Start load model to Triton...")
            self.triton_client.load_model(model_name=name)
            print("Model loaded to Triton")
        except InferenceServerException as ex:
            raise MlflowException(str(ex))

        return name, flavor

    def delete_deployment(self, name):
        """
        Delete the deployed model in Triton with the provided model name

        :param name: Name of the of the model with version number. For ex: "densenet_onnx/2"

        :return: None
        """
        # Verify model is already deployed to Triton
        if not self._model_exists(name):
            raise Exception(
                "Unable to delete deployment for name %s because it does not exist."
                % (name)
            )

        try:
            self.triton_client.unload_model(name)
        except InferenceServerException as ex:
            raise MlflowException(str(ex))

        self._delete_deployment_files(name)

        return None

    def update_deployment(self, name, model_uri=None, flavor=None, config=None):
        """
        Update the model deployment in triton with the provided name

        :param name: Name and version number of the model, <model_name>/<version>.
        :param model_uri: Model uri models:/model_name/version
        :param flavor: The flavor of the model
        :param config: Configuration parameters

        :return: Returns the flavor of the model
        """
        # TODO: Update this function with a warning. If config and label files associated with this
        # updated model are different than the ones already deployed to triton, issue a warning to the user.
        self._validate_flavor(flavor)

        # Verify model is already deployed to Triton
        if not self._model_exists(name):
            raise Exception(
                "Unable to update deployment for name %s because it does not exist."
                % (name)
            )

        self.get_deployment(name)

        # Get the path of the artifact
        path = Path(_download_artifact_from_uri(model_uri))

        self._copy_files_to_triton_repo(path, name, flavor)

        self._generate_mlflow_meta_file(name, flavor, model_uri)

        try:
            self.triton_client.load_model(name)
        except InferenceServerException as ex:
            raise MlflowException(str(ex))

        return {"flavor": flavor}

    def list_deployments(self):
        """
        List models deployed to Triton.

        :return: None
        """
        resp = self.triton_client.get_model_repository_index(as_json=True)
        actives = []

        if not resp:
            return []

        for d in resp["models"]:
            if "state" in d and d["state"] == "READY":
                mlflow_meta_path = os.path.join(
                    self.triton_model_repo, d["name"], _MLFLOW_META_FILENAME
                )
                if "s3" in self.server_config:
                    meta_dict = ast.literal_eval(
                        self.server_config["s3"]
                        .get_object(
                            Bucket=self.server_config["s3_bucket"],
                            Key=os.path.join(
                                self.server_config["s3_prefix"],
                                d["name"],
                                _MLFLOW_META_FILENAME,
                            ),
                        )["Body"]
                        .read()
                        .decode("utf-8")
                    )
                elif os.path.isfile(mlflow_meta_path):
                    meta_dict = self._get_mlflow_meta_dict(d["name"])
                else:
                    continue

                d["triton_model_path"] = meta_dict["triton_model_path"]
                d["mlflow_model_uri"] = meta_dict["mlflow_model_uri"]
                d["flavor"] = meta_dict["flavor"]
                actives.append(d)

        return actives

    def get_deployment(self, name):
        """
        Get deployment from Triton.

        :param name: Name of the model. \n
                     Ex: "mini_bert_onnx" - gets the details of active version of this model \n

        :return: output - Returns a dict with model info
        """
        deployments = self.list_deployments()
        for d in deployments:
            if d["name"] == name:
                return d
        raise ValueError(f"Unable to get deployment with name {name}")

    def load(self, model_name: str):
        try:
            print(f"Start load {model_name} model to Triton...")
            self.triton_client.load_model(model_name=model_name)
            print(f"Model {model_name} loaded to Triton")
        except InferenceServerException as ex:
            print(f"Failed to load model {model_name}")
            raise MlflowException(str(ex))

    def unload(self, model_name: str):
        try:
            print(f"Start unload {model_name} model from Triton...")
            self.triton_client.unload_model(model_name=model_name)
            print(f"Model {model_name} unloaded from Triton")
        except InferenceServerException as ex:
            print(f"Failed to unload model {model_name}")
            raise MlflowException(str(ex))

    def predict(self, model_name: str, df):
        single_input_np = None
        if isinstance(df, np.ndarray):
            single_input_np = df

        inputs = []
        if single_input_np is not None:
            raise MlflowException("Unnamed input is not currently supported")
        else:
            for key, val in df.items():
                inputs.append(
                    tritongrpcclient.InferInput(
                        key, val.shape, np_to_triton_dtype(val.dtype)
                    )
                )
                inputs[-1].set_data_from_numpy(val)

        try:
            resp = self.triton_client.infer(model_name=model_name, inputs=inputs)
            outputs = resp.get_response(as_json=True)["outputs"]
            res = {}
            for output in outputs:
                res[output["name"]] = resp.as_numpy(output["name"])
            return res
        except InferenceServerException as ex:
            raise MlflowException(str(ex))

    def _get_triton_server_config(self):
        triton_url = self.server_config["triton_url"]
        logger.info("Triton url = {}".format(triton_url))

        triton_model_repo = self.server_config["triton_model_repo"]
        logger.info("Triton model repo = {}".format(triton_model_repo))

        return triton_url, triton_model_repo

    def _generate_mlflow_meta_file(self, name, flavor, model_uri):
        triton_deployment_dir = os.path.join(self.triton_model_repo, name)
        meta_dict = {
            "name": name,
            "triton_model_path": triton_deployment_dir,
            "mlflow_model_uri": model_uri,
            "flavor": flavor,
        }

        if "s3" in self.server_config:
            self.server_config["s3"].put_object(
                Body=json.dumps(meta_dict, indent=4).encode("utf-8"),
                Bucket=self.server_config["s3_bucket"],
                Key=os.path.join(
                    self.server_config["s3_prefix"], name, _MLFLOW_META_FILENAME
                ),
            )
        else:
            with open(
                os.path.join(triton_deployment_dir, _MLFLOW_META_FILENAME), "w"
            ) as outfile:
                json.dump(meta_dict, outfile, indent=4)

        print("Saved", _MLFLOW_META_FILENAME, "to", triton_deployment_dir)

    def _get_mlflow_meta_dict(self, name):
        mlflow_meta_path = os.path.join(
            self.triton_model_repo, name, _MLFLOW_META_FILENAME
        )

        if "s3" in self.server_config:
            mlflow_meta_dict = ast.literal_eval(
                self.server_config["s3"]
                .get_object(
                    Bucket=self.server_config["s3_bucket"],
                    Key=os.path.join(
                        self.server_config["s3_prefix"], name, _MLFLOW_META_FILENAME
                    ),
                )["Body"]
                .read()
                .decode("utf-8")
            )
        else:
            with open(mlflow_meta_path, "r") as metafile:
                mlflow_meta_dict = json.load(metafile)

        return mlflow_meta_dict

    def _get_copy_paths(self, artifact_path, name, flavor):
        copy_paths = {}
        copy_paths["model_path"] = {}
        triton_deployment_dir = os.path.join(self.triton_model_repo, name)
        if flavor == "triton":
            # When flavor is 'triton', the model is assumed to be preconfigured
            # with proper model versions and version strategy, which may differ from
            # the versioning in MLFlow
            for file in artifact_path.iterdir():
                if file.is_dir():
                    copy_paths["model_path"]["from"] = file
                    break
            copy_paths["model_path"]["to"] = triton_deployment_dir
        elif flavor == "onnx":
            # Look for model file via MLModel metadata or iterating dir
            model_file = None
            config_file = None
            for file in artifact_path.iterdir():
                if file.name == "MLmodel":
                    mlmodel = Model.load(file)
                    onnx_meta_data = mlmodel.flavors.get("onnx", None)
                    if onnx_meta_data is not None:
                        model_file = onnx_meta_data.get("data", None)
                elif file.name == "config.pbtxt":
                    config_file = file.name
                    copy_paths["config_path"] = {}
                elif file.suffix == ".txt" and file.stem != "requirements":
                    copy_paths[file.stem] = {"from": file, "to": triton_deployment_dir}
            if model_file is None:
                for file in artifact_path.iterdir():
                    if file.suffix == ".onnx":
                        model_file = file.name
                        break
            copy_paths["model_path"]["from"] = os.path.join(artifact_path, model_file)
            copy_paths["model_path"]["to"] = os.path.join(triton_deployment_dir, "1")

            if config_file is not None:
                copy_paths["config_path"]["from"] = os.path.join(
                    artifact_path, config_file
                )
                copy_paths["config_path"]["to"] = triton_deployment_dir
            else:
                # Make sure the directory has been created for config.pbtxt
                os.makedirs(triton_deployment_dir, exist_ok=True)
                # Provide a minimum config file so Triton knows what backend
                # should be performing the auto-completion
                config = """
backend: "onnxruntime"
default_model_filename: "{}"
""".format(
                    model_file
                )
                with open(
                    os.path.join(triton_deployment_dir, "config.pbtxt"), "w"
                ) as cfile:
                    cfile.write(config)
        return copy_paths

    def _walk(self, path):
        """Walk a path like os.walk() if path is dir,
        return file in the expected format otherwise.
        :param path: dir or file path

        :return: root, dirs, files
        """
        if os.path.isfile(path):
            return [(os.path.dirname(path), [], [os.path.basename(path)])]
        elif os.path.isdir(path):
            return list(os.walk(path))
        else:
            raise Exception(f"path: {path} is not a valid path to a file or dir.")

    def _copy_files_to_triton_repo(self, artifact_path, name, flavor):
        copy_paths = self._get_copy_paths(artifact_path, name, flavor)
        print(copy_paths)
        for key in copy_paths:
            if "s3" in self.server_config:
                # copy model dir to s3 recursively
                for root, dirs, files in self._walk(copy_paths[key]["from"]):
                    for filename in files:
                        local_path = os.path.join(root, filename)

                        if flavor == "onnx":
                            s3_path = os.path.join(
                                self.server_config["s3_prefix"],
                                copy_paths[key]["to"]
                                .replace(self.server_config["triton_model_repo"], "")
                                .strip("/"),
                                filename,
                            )

                        elif flavor == "triton":
                            rel_path = os.path.relpath(
                                local_path,
                                copy_paths[key]["from"],
                            )
                            s3_path = os.path.join(
                                self.server_config["s3_prefix"], name, rel_path
                            )

                        self.server_config["s3"].upload_file(
                            local_path,
                            self.server_config["s3_bucket"],
                            # "model.onnx",
                            s3_path,
                        )
            else:
                if os.path.isdir(copy_paths[key]["from"]):
                    if os.path.isdir(copy_paths[key]["to"]):
                        shutil.rmtree(copy_paths[key]["to"])
                    shutil.copytree(copy_paths[key]["from"], copy_paths[key]["to"])
                else:
                    if not os.path.isdir(copy_paths[key]["to"]):
                        os.makedirs(copy_paths[key]["to"])
                    shutil.copy(copy_paths[key]["from"], copy_paths[key]["to"])

        if "s3" not in self.server_config:
            triton_deployment_dir = os.path.join(self.triton_model_repo, name)
            version_folder = os.path.join(triton_deployment_dir, "1")
            os.makedirs(version_folder, exist_ok=True)

        return copy_paths

    def _delete_mlflow_meta(self, filepath):
        if "s3" in self.server_config:
            self.server_config["s3"].delete_object(
                Bucket=self.server_config["s3_bucket"],
                Key=filepath,
            )
        elif os.path.isfile(filepath):
            os.remove(filepath)

    def _delete_deployment_files(self, name):
        triton_deployment_dir = os.path.join(self.triton_model_repo, name)

        if "s3" in self.server_config:
            objs = self.server_config["s3"].list_objects(
                Bucket=self.server_config["s3_bucket"],
                Prefix=os.path.join(self.server_config["s3_prefix"], name),
            )

            for key in objs["Contents"]:
                key = key["Key"]
                try:
                    self.server_config["s3"].delete_object(
                        Bucket=self.server_config["s3_bucket"],
                        Key=key,
                    )
                except Exception as e:
                    raise Exception(f"Could not delete {key}: {e}")

        else:
            # Check if the deployment directory exists
            if not os.path.isdir(triton_deployment_dir):
                raise Exception(
                    "A deployment does not exist for this model in directory {} for model name {}".format(
                        triton_deployment_dir, name
                    )
                )

            model_file = glob.glob("{}/model*".format(triton_deployment_dir))
            for file in model_file:
                print("Model directory found: {}".format(file))
                os.remove(file)
                print("Model directory removed: {}".format(file))

    def _validate_config_args(self, config):
        if not config["version"]:
            raise Exception("Please provide the version as a config argument")
        if not config["version"].isdigit():
            raise ValueError(
                "Please make sure version is a number. version = {}".format(
                    config["version"]
                )
            )

    def _validate_flavor(self, flavor):
        if flavor not in self.supported_flavors:
            raise Exception("{} model flavor not supported by Triton".format(flavor))

    def _model_exists(self, name):
        deploys = self.list_deployments()
        exists = False
        for d in deploys:
            if d["name"] == name:
                exists = True
        return exists
