# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyAzuremlAutomlCore(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("1.23.0", sha256="1fa4a900856b15e1ec9a6bb949946ed0c873a5a54da3db592f03dbb46a117ceb", url="https://pypi.org/packages/88/48/86dd8031ccba9d0310417944965a7ce10bbc0f8693313fb299fb23104fe2/azureml_automl_core-1.23.0-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@:3.8", when="@1.19:1.44")
        depends_on("py-azureml-dataset-runtime@1.23", when="@1.23")
        depends_on("py-azureml-telemetry@1.23", when="@1.23")
    # END DEPENDENCIES

