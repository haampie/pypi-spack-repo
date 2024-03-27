##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyMatplotlibScalebar(PythonPackage):
    version("0.8.1", sha256="a8a2f361d4c2d576d087df3092ed95cac2f708f8b40d5d2bb992bd190e740b3a", url="https://pypi.org/packages/a9/9e/22930e3deb2c374f47c6633aff9f6f379f8c421ab868fff3b4f85eac8b8a/matplotlib_scalebar-0.8.1-py2.py3-none-any.whl")
    version("0.8.0", sha256="955a86172ff3ff6f612888212d6d51534db3a7956b84e25a081420c68733862a", url="https://pypi.org/packages/07/76/71889e6f33ac4fa0e371119da182bc9214f2a83727a710f9c940615bdfc3/matplotlib_scalebar-0.8.0-py2.py3-none-any.whl")
    version("0.7.2", sha256="2b7f886f1d34c0c4fa16d4ff4bfd1e5f92c0a5925a8e2c954fdb97f42a2dbd02", url="https://pypi.org/packages/51/a4/cd254234c35f3591361988e89ab132ee14789f2ebe1ede621d63f5241f00/matplotlib_scalebar-0.7.2-py2.py3-none-any.whl")
    version("0.7.1", sha256="d6e858da5415ec82b4ce2033f1822eec9a063cb9fbe192466882354fbaa7277a", url="https://pypi.org/packages/98/31/761f61114e32afe59122e1f386ff21440fd601eccb9e8e7e4cb29f09ac25/matplotlib_scalebar-0.7.1-py2.py3-none-any.whl")
    version("0.7.0", sha256="661ae4ec4fec8d43b401daa4bc5abdb5beec04ff43d7ab5240ae9d5872bd077d", url="https://pypi.org/packages/0e/23/ceae0d790922724cd5a7326c75bcf6f97aebffb8c123cb3ce778532fb9b8/matplotlib_scalebar-0.7.0-py2.py3-none-any.whl")
    version("0.6.2", sha256="33642cd995f85e08845dd6395c0d8c5400d9683cd00360071e25d5adf7877f4a", url="https://pypi.org/packages/89/ba/46ae95cc9d2c49f2d13ec6f4322f06a5e7621bee03685fab59c64f321afd/matplotlib_scalebar-0.6.2-py2.py3-none-any.whl")
    version("0.6.1", sha256="913e0c2e3f7039d6e3d3f8bfb569241b3baaa747bfc1ec842ceec1adc1c2013f", url="https://pypi.org/packages/d1/95/d311da1083a426b872e7be318373c45f075bb356d0524c3097f5f4c6d2d9/matplotlib_scalebar-0.6.1-py2.py3-none-any.whl")
    version("0.6.0", sha256="c65bc0d49b968de543f6c64d97d76daac4f2181eeff095e83062891a7b45b197", url="https://pypi.org/packages/31/b2/acdcaea39ca40c029e3567d7bc71acd3bfefdbf7604d45ef2d7e482f31f0/matplotlib_scalebar-0.6.0-py2.py3-none-any.whl")
    version("0.5.1", sha256="7ce72468563e683e8f353d19a77535e716ca3d71485f2fdea48863e897d7f7de", url="https://pypi.org/packages/97/4f/d8b07da43cad4fe16a3b9a368b1a15629d3488e615c04c2943e7b69b8817/matplotlib_scalebar-0.5.1-py2.py3-none-any.whl")
    version("0.5.0", sha256="93f43d42eab576418650c501847bafec517e771b5cd6608cb99e5712db0aae23", url="https://pypi.org/packages/8f/3f/ca02f1dd0fd7a7d8ad64220c3c067d732ca999a78d32a45c90c495c66fc1/matplotlib_scalebar-0.5.0-py2.py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-matplotlib", when="@0.3:")

