##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyJaracoClasses(PythonPackage):
    version("3.3.1", sha256="86b534de565381f6b3c1c830d13f931d7be1a75f0081c57dff615578676e2206", url="https://pypi.org/packages/eb/57/d3590a153d7c1970f466f69fa2570e1a93a34d8f88f23c11411df73729bf/jaraco.classes-3.3.1-py3-none-any.whl")
    version("3.3.0", sha256="10afa92b6743f25c0cf5f37c6bb6e18e2c5bb84a16527ccfc0040ea377e7aaeb", url="https://pypi.org/packages/c7/6b/1bc8fa93ea85146e08f0e0883bc579b7c7328364ed7df90b1628dcb36e10/jaraco.classes-3.3.0-py3-none-any.whl")
    version("3.2.3", sha256="2353de3288bc6b82120752201c6b1c1a14b058267fa424ed5ce5984e3b922158", url="https://pypi.org/packages/60/28/220d3ae0829171c11e50dded4355d17824d60895285631d7eb9dee0ab5e5/jaraco.classes-3.2.3-py3-none-any.whl")
    version("3.2.2", sha256="e6ef6fd3fcf4579a7a019d87d1e56a883f4e4c35cfe925f86731abc58804e647", url="https://pypi.org/packages/8f/e6/f92d21f915cee7acf1cfe3e0ec60b8e9888dcf40a9814e3838a87ba487d0/jaraco.classes-3.2.2-py3-none-any.whl")
    version("3.2.1", sha256="22ac35313cf4b145bf7b217cc51be2d98a3d2db1c8558a30ca259d9f0b9c0b7d", url="https://pypi.org/packages/b8/74/bee5fc11594974746535117546404678fc7b899476e769c3c55bc0cfaa02/jaraco.classes-3.2.1-py3-none-any.whl")
    version("3.2.0", sha256="2229da0dc3e9f29dd14d9ba7cd86e3f66196acfc91131ede786159fbd794ebd9", url="https://pypi.org/packages/a7/e4/3b27524c46efd99836954601b3f21655f00532b55c2f13a66e0bdd48c751/jaraco.classes-3.2.0-py3-none-any.whl")
    version("3.1.1", sha256="8e7b26c4ba213817322287db9823a3903f2e7a3240e12565bafc8f7defb56515", url="https://pypi.org/packages/7b/5b/c8f1f4a6c73fb611f28229e2d6e434f1497d0ced31a49d34bc52b4bd25db/jaraco.classes-3.1.1-py3-none-any.whl")
    version("3.1.0", sha256="116429c2047953f525afdcae165475c4589c7b14870e78b2d068ecb01018827e", url="https://pypi.org/packages/68/ce/8f43aa0d0f18120e687ae0192fe3168630040841a3e87bed93c5fe024dbe/jaraco.classes-3.1.0-py2.py3-none-any.whl")
    version("3.0.0", sha256="dec765a9df411d1bd688e377d4ca4fad515dec84cc32091ea5f37ac6afd29c15", url="https://pypi.org/packages/fb/85/3e298241e4aff50eddaedcd9678b5409b01da5496a6353d9d072baa2d500/jaraco.classes-3.0.0-py2.py3-none-any.whl")
    version("2.0", sha256="d43d73bc8e4ed67c45b540fc7ea171444ff05779710104a120926ba517327df6", url="https://pypi.org/packages/f9/6c/d5ad4d56ed9a6f5d2bf843f30562e4bea2d1a694ecfabe6c56227ef31e90/jaraco.classes-2.0-py2.py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-more-itertools", when="@3:")
        depends_on("py-six", when="@1.4.1:2")

