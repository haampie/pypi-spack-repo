##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyAioitertools(PythonPackage):
    version("0.11.0", sha256="04b95e3dab25b449def24d7df809411c10e62aab0cbe31a50ca4e68748c43394", url="https://pypi.org/packages/45/66/d1a9fd8e6ff88f2157cb145dd054defb0fd7fe2507fe5a01347e7c690eab/aioitertools-0.11.0-py3-none-any.whl")
    version("0.10.0", sha256="a2ea2a39ebf272a2fbb58bfdb73e1daeeb6686edbbc8082215dfc8b8ffffa6e8", url="https://pypi.org/packages/b4/20/8af729fab3df6827407b060211ffffe79e0d220fba0c4f768de599f3cbe3/aioitertools-0.10.0-py3-none-any.whl")
    version("0.10.0-beta1", sha256="8bb2ebaf5712af397cdd21c8ce1320b1f76b385c3caeb40858b7a5543b96f454", url="https://pypi.org/packages/25/84/c4503c8ce72e5171c98ebb238cdbd4a71122173e5fa42d32d4fc4045bb77/aioitertools-0.10.0b1-py3-none-any.whl")
    version("0.9.0", sha256="70a643f07be2b0437674bde442548e18a6d33a653d23bc4be9dc9ba6f3116f94", url="https://pypi.org/packages/92/a0/d7addf01e207e91076c7529b52515355c3d91ef67be8a498ebe394cac364/aioitertools-0.9.0-py3-none-any.whl")
    version("0.8.0", sha256="3a141f01d1050ac8c01917aee248d262736dab875ce0471f0dba5f619346b452", url="https://pypi.org/packages/bf/ef/fd35e61a554489a4438cc34aadc95bdc4987f513b56624d78d8b22f08516/aioitertools-0.8.0-py3-none-any.whl")
    version("0.7.1", sha256="8972308474c41ed5e0636819f948ebff32f2318e70f7e7d23cd208c4357cc773", url="https://pypi.org/packages/32/0b/3260ac050de07bf6e91871944583bb8598091da19155c34f7ef02244709c/aioitertools-0.7.1-py3-none-any.whl")
    version("0.7.0", sha256="e931a2f0dcabd4a8446b5cc2fc71b8bb14716e6adf37728a70869213f1f741cd", url="https://pypi.org/packages/83/42/90df27c516ce54fa26964bc4a632ecaf352c7e99574b515255e48b4a7cc7/aioitertools-0.7.0-py3-none-any.whl")
    version("0.6.1", sha256="34155556df490ae1afb63b6393f80111cd3afdd32a5e6fe7c6fb897ace3277d3", url="https://pypi.org/packages/a6/90/f8ce07b77a17f4140f55b066fee76a650ded3ed382293181fe492bd22c1d/aioitertools-0.6.1-py3-none-any.whl")
    version("0.6.0", sha256="dd7232299dccb0650b1b5489aa9a7a7c40824bd40daec5afd47260c3b943790a", url="https://pypi.org/packages/05/81/313cd5e430cbba00279167fbe13b581b43821e4ea937b063ec477ea80310/aioitertools-0.6.0-py3-none-any.whl")
    version("0.5.1", sha256="4906089fceeab0c4e3e9784de36eae253012ed9d5a8da1a1c376bbcf1b5f9a69", url="https://pypi.org/packages/d5/72/5f2c75e34b10bdb53baaae1929331699bdd4505c4887d5a6e84aa4aeb460/aioitertools-0.5.1-py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-typing-extensions@4:", when="@0.9: ^python@:3.9")
        depends_on("py-typing-extensions@3.7:", when="@0.7")

