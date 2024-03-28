# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyAzureMgmtNetwork(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("11.0.0", sha256="0a4bda7341e33b2cfa567928f4374fe4e0c5710a328174f780813359ef15786b", url="https://pypi.org/packages/ed/6f/2f2fa743ec853f20bf151ca139aa4ae3eb3cd6319834a8f780cd634d7716/azure_mgmt_network-11.0.0-py2.py3-none-any.whl")
    version("10.2.0", sha256="f82b8b3874e0655a10fb36077036fb3e8e3daa96fa42c964e8b91ef5a466a8e6", url="https://pypi.org/packages/39/d8/84a181e6e4926ebad56e68c1d05427f5ad64e7a784acab82a302dc4a93d2/azure_mgmt_network-10.2.0-py2.py3-none-any.whl")
    version("10.1.0", sha256="ec0b6601b302f3d9fe0ffbe72c3317b780c2551f7f905e8dee4cdc5844b68e5b", url="https://pypi.org/packages/a8/38/7e83c1ad25110c791ee155054eccb52aedab8fc4a5ad9d592b2fb9ca691e/azure_mgmt_network-10.1.0-py2.py3-none-any.whl")
    version("10.0.0", sha256="d53cf32c9325f69e91a4029f08368590a5ad7a34d877eaab43bc454e7dabbdaa", url="https://pypi.org/packages/cc/2f/9cb87b06fc399884b36521dbe49dfee902a99fa84cd34a1a5ce1c8b1bc04/azure_mgmt_network-10.0.0-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-azure-common@1.1:", when="@1.5:2.0.0-rc1,2.2:")
        depends_on("py-msrest@0.5:", when="@2.0.1:18")
        depends_on("py-msrestazure@0.4.32:", when="@2.0.0:13")
    # END DEPENDENCIES

