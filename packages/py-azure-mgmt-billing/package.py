# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyAzureMgmtBilling(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.2.0", sha256="3810cdda69ec1409191b292628fe6ba86ce5e0444723b960d91af4f401846ac3", url="https://pypi.org/packages/0f/24/5106287ea0f6562d965afb055e3c6c0da058f7844a70464e67bab56c6c4b/azure_mgmt_billing-0.2.0-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-azure-common@1.1:", when="@0.2:")
        depends_on("py-azure-mgmt-nspkg@2:", when="@:0")
        depends_on("py-msrestazure@0.4.20:", when="@0.2:0")
    # END DEPENDENCIES

