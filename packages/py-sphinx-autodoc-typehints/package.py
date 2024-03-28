# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PySphinxAutodocTypehints(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("2.0.0", sha256="12c0e161f6fe191c2cdfd8fa3caea271f5387d9fbc67ebcd6f4f1f24ce880993", url="https://pypi.org/packages/28/1a/edfbaf4b1eab690ea4561514a046f090da7f39339406df79e0d73b10dc7f/sphinx_autodoc_typehints-2.0.0-py3-none-any.whl")
    version("1.25.3", sha256="d3da7fa9a9761eff6ff09f8b1956ae3090a2d4f4ad54aebcade8e458d6340835", url="https://pypi.org/packages/ba/d3/8c375e2a6ce21c29021d413e5ebb4d285431acd209f82b89101f157d4b9b/sphinx_autodoc_typehints-1.25.3-py3-none-any.whl")
    version("1.25.2", sha256="5ed05017d23ad4b937eab3bee9fae9ab0dd63f0b42aa360031f1fad47e47f673", url="https://pypi.org/packages/8a/0a/06da064e6b9962b40ded75c63538b9773e48c84178f353e161e0e67940a1/sphinx_autodoc_typehints-1.25.2-py3-none-any.whl")
    version("1.25.1", sha256="fbadc10f9fc48da69d5f7b6ed6e5e7ef3d441a3356a1aaedc65f32cdd45933b2", url="https://pypi.org/packages/fc/e7/d8d9b42900aa1e63e5bb740544af094ea445e6774df9581da2ad9db27e3e/sphinx_autodoc_typehints-1.25.1-py3-none-any.whl")
    version("1.25.0", sha256="e07601112663dd016568d9d31a4623d29ae91d554840f8c76d4c5573cfbd9d79", url="https://pypi.org/packages/92/ec/a59e260485f45c8b0c56817993744fe779764597839a0cf4bc1c366ee71d/sphinx_autodoc_typehints-1.25.0-py3-none-any.whl")
    version("1.24.1", sha256="4cc16c5545f2bf896ca52a854babefe3d8baeaaa033d13a7f179ac1d9feb02d5", url="https://pypi.org/packages/c1/42/a29d85cada86d9ddbbecab22e09914bffeb6d417f0da813686c4af2aa60d/sphinx_autodoc_typehints-1.24.1-py3-none-any.whl")
    version("1.24.0", sha256="6a73c0c61a9144ce2ed5ef2bed99d615254e5005c1cc32002017d72d69fb70e6", url="https://pypi.org/packages/a4/a2/71ee28033c218b025348555747cb95993338179875bae75c197138be77ad/sphinx_autodoc_typehints-1.24.0-py3-none-any.whl")
    version("1.23.4", sha256="46a98ee116e42ccdfe683bfc17a5cdce319b8b77f32e2bffe9c0cdad91acae32", url="https://pypi.org/packages/57/d0/9847a09f7c054f932636d9cec2709d5cf5d813e6ccd4eac2170a4b74ef87/sphinx_autodoc_typehints-1.23.4-py3-none-any.whl")
    version("1.23.3", sha256="ec913d93e915b4dae6a8758cd95baecc70ed77fcdfe050601fc6b12afd0fc059", url="https://pypi.org/packages/74/0b/da14533947c9d250917c3537a2ac4efd3d0f149c43ebfca63e718cfd5db8/sphinx_autodoc_typehints-1.23.3-py3-none-any.whl")
    version("1.23.2", sha256="92d0074e48acf26551795e1fad3416709fa7f1d67b809ce76e4aa093e032ad90", url="https://pypi.org/packages/81/81/fa50a8950f0028a1cc82f621e203db019322b3b0c82a72c92b31ff9df951/sphinx_autodoc_typehints-1.23.2-py3-none-any.whl")
    version("1.12.0", sha256="5e81776ec422dd168d688ab60f034fccfafbcd94329e9537712c93003bddc04a", url="https://pypi.org/packages/25/04/f59887284d9ea7e5e1473b74177fc8fca43c949a683750c733a154ba8148/sphinx_autodoc_typehints-1.12.0-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-sphinx@7.1.2:", when="@1.24.1:")
        depends_on("py-sphinx@7.0.1:", when="@1.23.1:1.23.3,1.24:1.24.0")
        depends_on("py-sphinx@5.3:", when="@1.19.5:1.23.0,1.23.4:1.23")
        depends_on("py-sphinx@3.0.0:", when="@1.11:1.12")
    # END DEPENDENCIES

