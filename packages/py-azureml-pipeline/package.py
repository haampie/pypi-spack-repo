# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyAzuremlPipeline(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("1.23.0", sha256="ed0fae96771840d3ffd63d63df1b1eed2f50c3b8dbe7b672a4f1ba6e66d0a392", url="https://pypi.org/packages/e1/6e/2ae53879796f5d46ca959a146c1db401fc3c6cc01afa4b754aba404d6f36/azureml_pipeline-1.23.0-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-azureml-pipeline-core@1.23", when="@1.23")
        depends_on("py-azureml-pipeline-steps@1.23", when="@1.23")
    # END DEPENDENCIES

