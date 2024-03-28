# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyBeniget(PythonPackage):
    # BEGIN VERSIONS
    version("0.4.1", sha256="cb061256631313f9d06031b824f7f403baecaf609b2d3d14d43f23356cf143f2", url="https://pypi.org/packages/cc/4a/af3f1b3d00efd47309b7a0e28351e06453727fa55d9b3a45fd4b91031a63/beniget-0.4.1-py3-none-any.whl")
    version("0.4.0", sha256="dd8e40dac139f162613f22158393231d450fa7ed5763c20dfa18192f32d5d8ee", url="https://pypi.org/packages/f6/eb/791da915b6179b0b23affed0dbcf3dbced1f3fd14a7f6fdc678115bace5e/beniget-0.4.0-py3-none-any.whl")
    version("0.3.0", sha256="f2bb32fcec2a2598abe03b45cbaa3c54d0dab89ab306e3fc8f3292ba20ff81ad", url="https://pypi.org/packages/af/14/210eb0053124922abbd1ace0fe6fe46782acda64edb101f5fc890a72f6ad/beniget-0.3.0-py3-none-any.whl")
    version("0.2.3", sha256="350422b0598c92fcc5f8bcaf77f2a62f6744fb8f2fb495b10a50176c1283639f", url="https://pypi.org/packages/19/0d/f7e1dcf1a26a42d4898bb14e7c96b401489362f31cc6a47b95e4f058b5a7/beniget-0.2.3.tar.gz")
    version("0.2.2", sha256="db95db425d99f8f35a4f9e53cf9843179f4dc89e335574f8c49c849b801cab1f", url="https://pypi.org/packages/a7/3f/2b3fe92da80b162c81bd8025aba3751c7c9e7857b7d28f1ccf6e82732162/beniget-0.2.2.tar.gz")
    version("0.2.1", sha256="6b14f24dc6334e2ea9c71e4eaf6085c405dffbd8bbabf7e7e8e5ddb14936b9df", url="https://pypi.org/packages/39/de/c4d3f953290a1a617508050d7e67ec391a083c9c4a87cd952a42b385f28b/beniget-0.2.1.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-gast@0.5:", when="@0.4:")
        depends_on("py-gast@0.4", when="@0.3")
    # END DEPENDENCIES

