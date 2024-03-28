# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyAzureMgmtMarketplaceordering(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.2.1", sha256="12d595f3dbda90de7cbc08ace99b925124ce675219b32bb3fde90e36d357c095", url="https://pypi.org/packages/38/10/7a334338d33d5d0f409ee3736568761cf681f2db50a32e477f287c7e4602/azure_mgmt_marketplaceordering-0.2.1-py2.py3-none-any.whl")
    version("0.2.0", sha256="600c5ab5deb8493202ef7ffd6520c198b857702dc6a590342f7ecb223d8c6de7", url="https://pypi.org/packages/fd/9e/0aafa7c085b25de2d31899c8d1bb03d3e9abed9af0be3a6a4b4710806538/azure_mgmt_marketplaceordering-0.2.0-py2.py3-none-any.whl")
    version("0.1.0", sha256="fb7a21f4a4a4b8d32bae600614f047a17993111374c9567ac11f241ada61d69f", url="https://pypi.org/packages/a8/cb/13502fdbaf520d08fb280eb31ecfe5d926b9cf92259c22280bbde96b307d/azure_mgmt_marketplaceordering-0.1.0-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-azure-common@1.1:")
        depends_on("py-azure-mgmt-nspkg@2:", when="@:0.1")
        depends_on("py-msrest@0.5:", when="@0.2:1.1")
        depends_on("py-msrestazure@0.4.32:", when="@0.2:0")
        depends_on("py-msrestazure@0.4.20:", when="@:0.1")
    # END DEPENDENCIES

