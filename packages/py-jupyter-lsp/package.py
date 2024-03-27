##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyJupyterLsp(PythonPackage):
    version("2.2.4", sha256="da61cb63a16b6dff5eac55c2699cc36eac975645adee02c41bdfc03bf4802e77", url="https://pypi.org/packages/33/1b/9d4925e2afcf66729fbe5d3db2907ebd546a8c5d1e43a41e44bcaa1a19e0/jupyter_lsp-2.2.4-py3-none-any.whl")
    version("2.2.3", sha256="57dd90d0a2e2530831793550846168c81c952b49e187aa339e455027a5f0fd2e", url="https://pypi.org/packages/d0/7b/9307b18c5e7ee46651acef8f436eadfd61a34b6c87ecf76ad305981badb2/jupyter_lsp-2.2.3-py3-none-any.whl")
    version("2.2.2", sha256="3b95229e4168355a8c91928057c1621ac3510ba98b2a925e82ebd77f078b1aa5", url="https://pypi.org/packages/d4/35/8332e7a07f872324e29ae4620a41a21372a8dc710b63b873d80cb2184241/jupyter_lsp-2.2.2-py3-none-any.whl")
    version("2.2.1", sha256="17a689910c5e4ae5e7d334b02f31d08ffbe98108f6f658fb05e4304b4345368b", url="https://pypi.org/packages/a6/b9/bb98cc91cda084a2756938682d02bdaf221a38f30b7126ba65ed7cde3ea6/jupyter_lsp-2.2.1-py3-none-any.whl")
    version("2.2.0", sha256="9e06b8b4f7dd50300b70dd1a78c0c3b0c3d8fa68e0f2d8a5d1fbab62072aca3f", url="https://pypi.org/packages/8f/b6/a1571e48550855a79898f851f57e5858b00eb36b09ea3b1a8bb65c53a290/jupyter_lsp-2.2.0-py3-none-any.whl")
    version("2.1.0", sha256="d7c058cfe8bd7a76859734f3a142edb50a2d1e265a7e323c2fdcd8b1db80a91b", url="https://pypi.org/packages/88/b5/4937ebc29944cbd30ba8504c4d64f9d0f4e083582f0f26a6cc73c8b04ba6/jupyter_lsp-2.1.0-py3-none-any.whl")
    version("2.0.1", sha256="61207787235e7b00df967df04205df81aa2728c7717664ba0a377bb9589c5672", url="https://pypi.org/packages/3b/be/6b7aa8c1986ddb152e4f9ca1b18d81f682add16d59a42e3bfe763ce845cf/jupyter_lsp-2.0.1-py3-none-any.whl")
    version("2.0.0", sha256="d9322a00211276aec9fb9ad6de17872771946e3fb745808f641d5ca53b38e54c", url="https://pypi.org/packages/b2/15/174053982d923033fe2d9890bad3a1d89f7b8326323dfc55e0fb9989f0e9/jupyter_lsp-2.0.0-py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-importlib-metadata@4.8.3:", when="@2: ^python@:3.9")
        depends_on("py-jupyter-server@1.1.2:", when="@1.0.0:")

