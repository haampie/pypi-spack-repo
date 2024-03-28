# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyAzureMgmtManagementgroups(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.2.0", sha256="8194ee6274df865eccd1ed9d385ea625aeba9b8058b9e4fdf547f5207271a775", url="https://pypi.org/packages/95/e8/2bbe79c62ad2787944dd7ae4d06d60afb3967b5efc09ed14046919371b59/azure_mgmt_managementgroups-0.2.0-py2.py3-none-any.whl")
    version("0.1.0", sha256="005e8289c2e1d8a8368c96790edf6a34e5c37b4096bce2eb8a923c6d5dc11fb2", url="https://pypi.org/packages/f2/50/591adac2a6cd8d77cccd38bdf5d177ad6a2e95b9217daa9a60b5d86de5cd/azure_mgmt_managementgroups-0.1.0-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-azure-common@1.1:")
        depends_on("py-azure-mgmt-nspkg@2:", when="@:0.1")
        depends_on("py-msrest@0.5:", when="@0.2:1.0.0-beta1")
        depends_on("py-msrestazure@0.4.32:", when="@0.2:0")
        depends_on("py-msrestazure@0.4.27:", when="@:0.1")
    # END DEPENDENCIES

