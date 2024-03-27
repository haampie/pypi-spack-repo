##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyAutogradGamma(PythonPackage):
    version("0.5.0", sha256="f27abb7b8bb9cffc8badcbf59f3fe44a9db39e124ecacf1992b6d952934ac9c4", url="https://pypi.org/packages/85/ae/7f2031ea76140444b2453fa139041e5afd4a09fc5300cfefeb1103291f80/autograd-gamma-0.5.0.tar.gz")
    version("0.4.3", sha256="2cb570cbb8da61ede937ccc004d87d3924108f754b351a86cdd2ad31ace6cdf6", url="https://pypi.org/packages/db/70/7cabb71898dc90da52c2c7dc8fd78ac80b7af6a60a9f8427dee7af9e4929/autograd-gamma-0.4.3.tar.gz")
    version("0.4.2", sha256="6bf89881ccb5c320ec10927410d6da816bc628b17183f4dee674e6d757ab5552", url="https://pypi.org/packages/67/aa/f85ea1c24f34eef1acd97615ad84accc4764b9bb20b668fd5a94e745922d/autograd_gamma-0.4.2-py3-none-any.whl")
    version("0.4.1", sha256="99864819e3fe8423b8cb17da64a161854949b9a126ce409538d6b0f8007b1c3c", url="https://pypi.org/packages/83/0c/169c73ba0a3f085644cd720c109b1e7dac3379a33fc64c272147a0959dc2/autograd_gamma-0.4.1-py3-none-any.whl")
    version("0.4.0", sha256="a2ff4444135f66db5d134836b8290d2b9c42e7d740724beaf796dad3cde53665", url="https://pypi.org/packages/58/07/a735d64093486f75fc60f7a99024aaeef0a394d57c13e9786aca7c0b5443/autograd_gamma-0.4.0-py3-none-any.whl")
    version("0.3.0", sha256="e4143e400cb4d1a202b1fec3d345dec3627e33cda05044cba74fc4a2930fca1e", url="https://pypi.org/packages/ac/79/0ecafc2424c9bb618a23053153ec787ba1fc682a22c042c0c80bfe91869b/autograd_gamma-0.3.0-py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-autograd@1.2:", when="@:0.4.2")
        depends_on("py-scipy@1.2.0:", when="@:0.4.2")

