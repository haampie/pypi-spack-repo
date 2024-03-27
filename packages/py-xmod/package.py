##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyXmod(PythonPackage):
    version("1.8.1", sha256="a24e9458a4853489042522bdca9e50ee2eac5ab75c809a91150a8a7f40670d48", url="https://pypi.org/packages/33/6b/0dc75b64a764ea1cb8e4c32d1fb273c147304d4e5483cd58be482dc62e45/xmod-1.8.1-py3-none-any.whl")
    version("1.8.0", sha256="11ae15c4e14d4cd7f62131d269053ad0e16199fc2aeda9431a375038c06f11ac", url="https://pypi.org/packages/4f/29/01688fc41f2497fc97976de71c788a540f8521cb4747fdf436f0814d228e/xmod-1.8.0-py3-none-any.whl")
    version("1.7.2", sha256="2b092cbf34ace5eee9cb7c67570c5788f73efd15d008a72c2730cf6494a1257a", url="https://pypi.org/packages/61/11/0393be48e73a51cc8b4e1c62133b44ca9dd4e4221fd1b74bf861df0e7cee/xmod-1.7.2-py3-none-any.whl")
    version("1.7.1", sha256="07a5d8ab27aed3d59d684a022e309e4728b1046fdddaa756caba7f1ebbc8b967", url="https://pypi.org/packages/16/d5/ea855c8a9ed6b3c21b5f749725cecd0fc3e9362ea2d4bb97a693c7676b00/xmod-1.7.1-py3-none-any.whl")
    version("1.7.0", sha256="8cfa11d19d959cf3703fe8823829b77576bb354b659defcf3f99dea241f0432a", url="https://pypi.org/packages/33/58/0e449fe4af9567a59cd50ea760e1d4e163dc8875a456ec0d86ad7f3df294/xmod-1.7.0-py3-none-any.whl")
    version("1.6.1", sha256="ece12f2cecf6d243e09a5db23f3daee032eec00d83560774200d3805116c20bb", url="https://pypi.org/packages/c5/c0/7e08a51203fb736bfe899b9f80835afb991b6a1bb02cc9a7958e75419795/xmod-1.6.1-py3-none-any.whl")
    version("1.6.0", sha256="e8309df5de74ba1baeb28510592910ac17284aaaff49fc795c1cf6c1641dd392", url="https://pypi.org/packages/de/45/1c1ec334ee6e137c2bd6b1eeb84a5b1d42cf854b0a69cc9d5aadf2195491/xmod-1.6.0-py3-none-any.whl")
    version("1.5.0", sha256="1ef43b78282e1593938e948f428c343d071ce3dba87450c2849fa710010f9f14", url="https://pypi.org/packages/c1/dc/912a36d36a101f1cdc46726f4e21a5752aa67ac3093f1bba40a83a121d04/xmod-1.5.0-py3-none-any.whl")
    version("1.4.0", sha256="dce91e65c5e645628d90ce0c366c387ccd039146592da3a5d6aa76d24a35a13f", url="https://pypi.org/packages/69/93/e69f1de61c1c2e11a6a54bd58fbd4dd3e13ea2e27634ebe8a304ea70e841/xmod-1.4.0-py3-none-any.whl")
    version("1.3.2", sha256="a95b0b3d3d67481d33dc1bb53abb88775d26e967e5a2280033030fe25a147f3f", url="https://pypi.org/packages/79/6a/4125aa282f6971b69ab3c2e8673f1cc2c04c410747140998f975012a6f9a/xmod-1.3.2-py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-black@23.12.1:23", when="@1.7:1.7.0")
        depends_on("py-dek@1.0.2:", when="@1.4")
        depends_on("py-dek", when="@:1.3,1.5:1.6.0")
        depends_on("py-isort@5.13.2:5", when="@1.7:1.7.0")
        depends_on("py-mypy@1.8:", when="@1.7:1.7.0")
        depends_on("py-pyright@1.1.343:", when="@1.7:1.7.0")
        depends_on("py-ruff@0.1.9:0.1", when="@1.7:1.7.0")

