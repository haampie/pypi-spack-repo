# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyAzuremlTrainAutomlClient(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("1.23.0.post1", sha256="66ace503328dc34c23de3e2d2a1b422403fa36864a505451bcb8afdbc46d5827", url="https://pypi.org/packages/7c/8b/7d498aa2ab4678ef48649ab9a03ce7718231399ff1baec2a1adea429f5f4/azureml_train_automl_client-1.23.0.post1-py3-none-any.whl")
    version("1.23.0", sha256="ac5f1ce9b04b4e61e2e28e0fa8d2d8e47937a546f624d1cd3aa6bc4f9110ecbe", url="https://pypi.org/packages/aa/3b/787bf39d04d346ab3747a6d5dd10a6edcba9b1ab7e310f650e39fdf46074/azureml_train_automl_client-1.23.0-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@:3.10", when="@1.49:")
        depends_on("python@:3.9", when="@1.45:1.48")
        depends_on("python@:3.8", when="@1.19:1.44")
        depends_on("py-azureml-automl-core@1.23", when="@1.23")
        depends_on("py-azureml-core@1.23", when="@1.23")
        depends_on("py-azureml-dataset-runtime@1.23", when="@1.23")
        depends_on("py-azureml-telemetry@1.23", when="@1.23")
    # END DEPENDENCIES

