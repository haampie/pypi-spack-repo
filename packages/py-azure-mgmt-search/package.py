##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyAzureMgmtSearch(PythonPackage):
    version("2.1.0", sha256="ea24482c56ceb2db2c22165ad7f389054567f7a2fa67e3c13df852b790bfc297", url="https://pypi.org/packages/c9/18/fa4e0d541332c0ba6ef16beaa9b55f831436949e7d0981d5677dff2ddfb5/azure_mgmt_search-2.1.0-py2.py3-none-any.whl")
    version("2.0.0", sha256="fdbaa1721b045a4ea4a21c84c6bc1f9636b39e93dff09ffd68f22e5da88bd3ea", url="https://pypi.org/packages/e2/52/46a5984eca50393057d4e760b9ef4adc5d6b8738f333427632991c6f3739/azure_mgmt_search-2.0.0-py2.py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-azure-common@1.1:", when="@2:")
        depends_on("py-azure-mgmt-nspkg@2:", when="@1:2.0")
        depends_on("py-msrest@0.5:", when="@2.1:8")
        depends_on("py-msrestazure@0.4.32:", when="@2.1:3")
        depends_on("py-msrestazure@0.4.27:", when="@2:2.0")

