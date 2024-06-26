# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyAzuremlPipelineSteps(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("1.23.0", sha256="72154c2f75624a1e7500b8e2239ae1354eeedf66d2cabb11e213b7eb80aedddb", url="https://pypi.org/packages/40/d7/5b0011fc4bc95007416fb9fb873c4f5ad901315eadca46099521a8b521ae/azureml_pipeline_steps-1.23.0-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-azureml-pipeline-core@1.23", when="@1.23")
        depends_on("py-azureml-train-automl-client@1.23", when="@1.23")
        depends_on("py-azureml-train-core@1.23", when="@1.23")
    # END DEPENDENCIES

