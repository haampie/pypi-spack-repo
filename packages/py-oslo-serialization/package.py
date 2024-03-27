##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyOsloSerialization(PythonPackage):
    version("5.4.0", sha256="f999b75f2c2904c2f6aae5efbb67ab668cc0e79470510b721937626b36427220", url="https://pypi.org/packages/70/5f/80eb88d4590cc23cd68e05730ee9be51fc1fc83121b8227e0ff5d29bce65/oslo.serialization-5.4.0-py3-none-any.whl")
    version("5.3.0", sha256="0da7248d0e515b875ef9883e3631ff51f9a8d11e8576247f0ded890f3276c0bf", url="https://pypi.org/packages/19/c3/6f2061614337fb9b21d06da058addcee41c9dce76360288737125a2db9f8/oslo.serialization-5.3.0-py3-none-any.whl")
    version("5.2.0", sha256="c7ec759192a787c7e1a5e765920bb594752c75e6e0cd5a9a82c385a9088125e5", url="https://pypi.org/packages/7e/53/92c9bb7baf9dfe3b52aaf9702b69b676a4a1ba8da9bd2107b521dce9ea93/oslo.serialization-5.2.0-py3-none-any.whl")
    version("5.1.1", sha256="c5dfb97ce8ddd1d2708a9a3f4a091063f6c304940c7cb39f532f7f791441fdca", url="https://pypi.org/packages/42/f8/cca2a14c8664e3fac43e9526fa82fda6d34f0ca5b5154331c9fab615a27a/oslo.serialization-5.1.1-py3-none-any.whl")
    version("5.1.0", sha256="0b4b8f662f580f13d6c4f905560cbd71e383804966b0981ec6276001b075654f", url="https://pypi.org/packages/cf/90/2cf275b3160df6e9786d7c69d2142e810642c7549f86157a26478537c41d/oslo.serialization-5.1.0-py3-none-any.whl")
    version("5.0.0", sha256="b0452bb2fcb99ee3e11bce3e1163f25a6393681233d2b3c2abdc4e5efd49d2a3", url="https://pypi.org/packages/6a/5e/1cf11ecf53f948f359d6e1adbf349e42391d3d165da8e7c5be857ebbd43b/oslo.serialization-5.0.0-py3-none-any.whl")
    version("4.3.0", sha256="6c1c483231c3827787af9b6ca4a45f4e45fe364772a24692b02de78fe48eafb1", url="https://pypi.org/packages/f7/6f/1be52c3b976f6714ad34a3173e23966d2f12f667cff8377c14d2e285199c/oslo.serialization-4.3.0-py3-none-any.whl")
    version("4.2.0", sha256="11ec9eeaddcd5ec99c88e2b46c1584915311e858c442319bdab5e5e2ec05f20e", url="https://pypi.org/packages/86/d6/09d7a7ad96656ca2ada11294039d767c27416890715bc2308f816bb39d1e/oslo.serialization-4.2.0-py3-none-any.whl")
    version("4.1.1", sha256="bf0ca0339b6ca5d174ae97fc641fa7151dd2620b96c327398f09bd3fa7cabd38", url="https://pypi.org/packages/9b/e1/0fadd2d580c09f83c223ff0734e48249ddff470eb2818f75aa1e33835934/oslo.serialization-4.1.1-py3-none-any.whl")
    version("4.1.0", sha256="a0acf0ff7ca88b3ee6514713571f614b5c20870005ed0eb90408fa7f9f3edb60", url="https://pypi.org/packages/a4/99/d02844a4ddd063dab89b8b9cfd176081ef9e60a5b57fa89cd3a62a406195/oslo.serialization-4.1.0-py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-msgpack@0.5.2:", when="@2.27:")
        depends_on("py-oslo-utils@3.33:", when="@2.23:")
        depends_on("py-pbr@2:2.0,3:", when="@2.19:")
        depends_on("py-pytz@2013.6:", when="@5.4: ^python@:3.8")
        depends_on("py-pytz@2013.6:", when="@1.3:5.3")
        depends_on("py-tzdata@2022.4:", when="@5.4: ^python@3.9:")
        depends_on("py-tzdata@2022.4:", when="@5.2:5.3")

