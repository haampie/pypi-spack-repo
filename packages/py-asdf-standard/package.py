##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyAsdfStandard(PythonPackage):
    version("1.1.1", sha256="9b559b5d43f086a3e9e12604fb591e056e5d8c0b4a1d2d99a011d278afbc6fd8", url="https://pypi.org/packages/51/86/2818771491fc4004f5cb5f297c6a94e786db704e9b091abedf9fc0248771/asdf_standard-1.1.1-py3-none-any.whl")
    version("1.1.0", sha256="ec77a457f0845ecff197e3fa30e78bb68f0fe2702dc02ca280f7526f02f69aca", url="https://pypi.org/packages/2b/e3/e053baa9210ea061c99f50eb2072be00b461b061e4dbaeb1f3ab3094c88b/asdf_standard-1.1.0-py3-none-any.whl")
    version("1.0.3", sha256="1c628379c75f0663b6376a7e681d31b1b54391053e53447c9921fb04c26d41da", url="https://pypi.org/packages/b1/3e/2873079563324cbc60a152be07a38c8595bcfe0cadda4db8a1a1c9b5b2a7/asdf_standard-1.0.3-py3-none-any.whl")
    version("1.0.2", sha256="1886ec4f947ad5d77de70d26d2f85c70245905a685bc48e3875d8ae564586a2a", url="https://pypi.org/packages/86/59/cc618281558da57181bfab30489c28397c44680822b63b9d390a3637f7bf/asdf_standard-1.0.2-py3-none-any.whl")
    version("1.0.1", sha256="2dfee061dce8d44c4d94fa7335c7c262d61af5e56bb8f42a479d54de2df38f1c", url="https://pypi.org/packages/91/04/b22c40eff987f31e6a21a44ae9f433218fce75a8df49370be557f8adbc4a/asdf_standard-1.0.1-py3-none-any.whl")

    with default_args(type="run"):
        depends_on("python@3.9:", when="@1.1:")
        depends_on("py-importlib-resources@3:", when="@1.0.1:1.0 ^python@:3.8")

