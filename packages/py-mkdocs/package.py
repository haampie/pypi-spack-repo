##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyMkdocs(PythonPackage):
    version("1.5.3", sha256="3b3a78e736b31158d64dbb2f8ba29bd46a379d0c6e324c2246c3bc3d2189cfc1", url="https://pypi.org/packages/89/58/aa3301b23966a71d7f8e55233f467b3cec94a651434e9cd9053811342539/mkdocs-1.5.3-py3-none-any.whl")
    version("1.5.2", sha256="60a62538519c2e96fe8426654a67ee177350451616118a41596ae7c876bb7eac", url="https://pypi.org/packages/14/f4/66760e770dd1eb4b3aab7b7e3e97c5ec5c0d8c4f66ebbd32f1cb5cf53139/mkdocs-1.5.2-py3-none-any.whl")
    version("1.5.1", sha256="67e889f8d8ba1fe5decdfc59f5f8f21d6a8925a129339e93dede303bdea03a98", url="https://pypi.org/packages/d9/72/3624fa6994e06eae5078f88724f7f00ef137735b693ab752e5fa7ba28fb9/mkdocs-1.5.1-py3-none-any.whl")
    version("1.5.0", sha256="91a75e3a5a75e006b2149814d5c56af170039ceda0732f51e7af1a463599c00d", url="https://pypi.org/packages/af/f7/8389af1b8300cee54fa941e56697b46731c721515bf477cf9504092c8356/mkdocs-1.5.0-py3-none-any.whl")
    version("1.4.3", sha256="6ee46d309bda331aac915cd24aab882c179a933bd9e77b80ce7d2eaaa3f689dd", url="https://pypi.org/packages/42/7a/5ed794942ace9d00bb77a8036c64c999cda6ebaab57e9b8a6ec1aa5fc900/mkdocs-1.4.3-py3-none-any.whl")
    version("1.4.2", sha256="c8856a832c1e56702577023cd64cc5f84948280c1c0fcc6af4cd39006ea6aa8c", url="https://pypi.org/packages/ff/00/58f2939f8e6c5f981d9ad9b685c9915a3b315c8f34ba93f0020d64929f70/mkdocs-1.4.2-py3-none-any.whl")
    version("1.4.1", sha256="2b7845c2775396214cd408753e4cfb01af3cfed36acc141a84bce2ceec9d705d", url="https://pypi.org/packages/27/81/7219ab996d6f7ef74370a37e7c0a24d5c24f42ba4499ca5f2127221ee9df/mkdocs-1.4.1-py3-none-any.whl")
    version("1.4.0", sha256="ce057e9992f017b8e1496b591b6c242cbd34c2d406e2f9af6a19b97dd6248faa", url="https://pypi.org/packages/50/74/8231b486bb6627c7bf819eeeeb22856c8fbf388cfee203eb13f2f1be6403/mkdocs-1.4.0-py3-none-any.whl")
    version("1.3.1", sha256="fda92466393127d2da830bc6edc3a625a14b436316d1caf347690648e774c4f0", url="https://pypi.org/packages/e4/96/6b9d87ee8a11e6d2483e3767999d4aeb8d5478d2059cfb3e21404beae470/mkdocs-1.3.1-py3-none-any.whl")
    version("1.3.0", sha256="26bd2b03d739ac57a3e6eed0b7bcc86168703b719c27b99ad6ca91dc439aacde", url="https://pypi.org/packages/33/68/5b640fe30386ae27ee904f2fd411572ff7ec7b1cf51f29beb8f5615d1622/mkdocs-1.3.0-py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-click@7:", when="@1.4:")
        depends_on("py-click@3.3:", when="@0.15.1:1.3")
        depends_on("py-colorama@0.4:", when="@1.4.1: platform=windows")
        depends_on("py-ghp-import@1:", when="@1.2:")
        depends_on("py-importlib-metadata@4.3:", when="@1.4: ^python@:3.9")
        depends_on("py-importlib-metadata@4.3:", when="@1.3")
        depends_on("py-jinja2@2.11.1:", when="@1.4:")
        depends_on("py-jinja2@2.10.2:", when="@1.3")
        depends_on("py-markdown@3.2.1:3.3", when="@1.3.1:1.4")
        depends_on("py-markdown@3.2.1:", when="@1.1:1.3.0,1.5:")
        depends_on("py-markupsafe@2.0.1:", when="@1.5:")
        depends_on("py-mergedeep@1.3.4:", when="@1.2:")
        depends_on("py-packaging@20.5:", when="@1.2:")
        depends_on("py-pathspec@0.11.1:", when="@1.5:")
        depends_on("py-platformdirs@2.2:", when="@1.5:")
        depends_on("py-pyyaml@5.1:", when="@1.4:")
        depends_on("py-pyyaml", when="@0.14:1.3")
        depends_on("py-pyyaml-env-tag", when="@1.2:")
        depends_on("py-watchdog@2:", when="@1.2:")

