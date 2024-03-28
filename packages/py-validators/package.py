# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyValidators(PythonPackage):
    # BEGIN VERSIONS
    version("0.23.1", sha256="e812ad5c0a80e44ed81bf01e42da2435705988131b83add5c9204f781cb9a4fa", url="https://pypi.org/packages/d4/01/7628818bc8477ec80f6a2c9a21a6b348cfa262daa4c5004bfcff5a9af9d9/validators-0.23.1-py3-none-any.whl")
    version("0.23.0", sha256="5fad1863feb5003993e19b733beee31fc7a64f94ede4ead4bf08e1bcac8f8db6", url="https://pypi.org/packages/a8/10/e1b40ff1c6eecf7fcf53cc6574ae96138bd77a67d5e1401c5e6fafb90c4e/validators-0.23.0-py3-none-any.whl")
    version("0.22.0", sha256="61cf7d4a62bbae559f2e54aed3b000cea9ff3e2fdbe463f51179b92c58c9585a", url="https://pypi.org/packages/3a/0c/785d317eea99c3739821718f118c70537639aa43f96bfa1d83a71f68eaf6/validators-0.22.0-py3-none-any.whl")
    version("0.21.2", sha256="6ad95131005a9d4c734a69dd4ef08cf66961e61222e60da25a9b5137cecd6fd4", url="https://pypi.org/packages/8d/e7/c2d0758c58dbd463b4a0a650f8cf3af5c4cbb6fbc61a36ce077964286feb/validators-0.21.2-py3-none-any.whl")
    version("0.21.1", sha256="be7cfd6992738a78394696395ae552d3f4e272b0135b55a795bdbf3c1704cc4e", url="https://pypi.org/packages/e7/67/0c03709a40e9cd3945e1ada5dbb41bda60d755e6dee3544bfe1b77418b72/validators-0.21.1-py3-none-any.whl")
    version("0.21.0", sha256="3470db6f2384c49727ee319afa2e97aec3f8fad736faa6067e0fd7f9eaf2c551", url="https://pypi.org/packages/ad/50/18dbf2ac594234ee6249bfe3425fa424c18eeb96f29dcd47f199ed6c51bc/validators-0.21.0-py3-none-any.whl")
    version("0.20.0", sha256="24148ce4e64100a2d5e267233e23e7afeb55316b47d30faae7eb6e7292bc226a", url="https://pypi.org/packages/95/14/ed0af6865d378cfc3c504aed0d278a890cbefb2f1934bf2dbe92ecf9d6b1/validators-0.20.0.tar.gz")
    version("0.19.0", sha256="dec45f4381f042f1e705cfa74949505b77f1e27e8b05409096fee8152c839cbe", url="https://pypi.org/packages/77/eb/e60e6704d8eb84be0648e4c667c559a210116ac2401099851abd0639a6a9/validators-0.19.0.tar.gz")
    version("0.18.2", sha256="0143dcca8a386498edaf5780cbd5960da1a4c85e0719f3ee5c9b41249c4fefbd", url="https://pypi.org/packages/db/2f/7fed3ee94ad665ad2c1de87f858f10a7785251ff75b4fd47987888d07ef1/validators-0.18.2-py3-none-any.whl")
    version("0.18.1", sha256="f787632edf9e054e9cf580d3016f5b0e9ad83b8a00a258b71406db0456e17007", url="https://pypi.org/packages/41/4a/3360ff3cf2b4a1b9721ac1fbff5f84663f41047d9874b3aa1ac82e862c44/validators-0.18.1-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-decorator@3.4:", when="@0.17.1:0.18")
        depends_on("py-six@1.4:", when="@0.17.1:0.18")
    # END DEPENDENCIES

