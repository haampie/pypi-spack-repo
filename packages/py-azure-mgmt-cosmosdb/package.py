# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyAzureMgmtCosmosdb(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.15.0", sha256="967e2f54c956d343e7c2738b8725aa5133df1e894472fa3d07f387a6a4328c8b", url="https://pypi.org/packages/7a/15/3645115e2255a227292851bc9413878bf84959850b6273b5895b70f808d3/azure_mgmt_cosmosdb-0.15.0-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-azure-common@1.1:")
        depends_on("py-msrest@0.5:", when="@:6.1")
        depends_on("py-msrestazure@0.4.32:", when="@:4")
    # END DEPENDENCIES

