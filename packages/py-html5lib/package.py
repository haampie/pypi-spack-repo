##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyHtml5lib(PythonPackage):
    version("1.1", sha256="0d78f8fde1c230e99fe37986a60526d7049ed4bf8a9fadbad5f00e22e58e041d", url="https://pypi.org/packages/6c/dd/a834df6482147d48e225a49515aabc28974ad5a4ca3215c18a882565b028/html5lib-1.1-py2.py3-none-any.whl")
    version("1.0.1", sha256="20b159aa3badc9d5ee8f5c647e5efd02ed2a66ab8d354930bd9ff139fc1dc0a3", url="https://pypi.org/packages/a5/62/bbd2be0e7943ec8504b517e62bab011b4946e1258842bc159e5dfde15b96/html5lib-1.0.1-py2.py3-none-any.whl")
    version("1.0", sha256="d09ae03efb1c64b489052110f570b7d6b0e9e0d30d66ba3c76f4340a215d5f80", url="https://pypi.org/packages/da/66/ea28be5e5aa471f499b2dac8dd57c0755743daaec050c418f6e24688aaa6/html5lib-1.0-reupload.tar.gz")
    version("1.0-beta10", sha256="08a3efc117a4fc8c82c3c6d10d6f58ae266428d57ed50258a1466d2cd88de745", url="https://pypi.org/packages/2f/74/7793ca2d36f676b740efc04b7ba887c610119beb5841d1805cb3515616cb/html5lib-1.0b10-py2.py3-none-any.whl")
    version("1.0-beta9", sha256="e144ae95a51cb690f29bd78481c80649b75cbd3809bc205e4d9b5ed4402a2680", url="https://pypi.org/packages/8c/8e/dfa046c6275177e76bf52bb4b6c604c2a595c81475fb75624d0f77e0880c/html5lib-1.0b9.tar.gz")
    version("1.0-beta8", sha256="18f4d63fa56836e3d62e96a44d06fcfe01a9be397a222368ee21403b64c176d2", url="https://pypi.org/packages/3b/89/c32486cdca98f476252a9db2cc836b605de4807ac4602ca55b3e7b52b7a8/html5lib-1.0b8.tar.gz")
    version("1.0-beta7", sha256="f6f58cfc467d539b9e3e32c03370a14a6114707fbe96cd6de70f1f77f7f51052", url="https://pypi.org/packages/50/9b/61ada852e7dc635c8e4ad0a06fe80837e1e9f0006d3cc855567ae813632a/html5lib-1.0b7.tar.gz")
    version("1.0-beta6", sha256="6f9979dac264b6ba28546b4ecc9ce4516c7cae07b76abf4ad9e92129feff1dea", url="https://pypi.org/packages/e9/aa/8f56d12c27aaeb3d8478a0b2fef7b5acb7cd1a8074c520ba96d99077b70d/html5lib-1.0b6.tar.gz")
    version("1.0-beta5", sha256="c708f2d1a8c0977e43d14b90e698becea146ac334070dc9c01b9e5b9b0ee4e1e", url="https://pypi.org/packages/e2/fc/5c017ce54ba9e69f52215019c8feb7566f14b52381cbf72992db2c36ef59/html5lib-1.0b5.tar.gz")
    version("0.999999999", sha256="b8934484cf22f1db684c0fae27569a0db404d0208d20163fbf51cc537245d008", url="https://pypi.org/packages/f7/71/a96f36d34394bcfff9fb54bfe0aa72cc5b4ff2f803e5728645aef38f7aee/html5lib-0.999999999-py2.py3-none-any.whl")
    version("0.99999999", sha256="7e793bb51f74c07cf15f4de2fb4fdf0dcc191d644a20d18bd90d82c3c2bccf35", url="https://pypi.org/packages/2f/89/04a6f0beec623397c6c849530dbc538ba96935d367a36be40f5effdd03a7/html5lib-0.99999999.tar.gz")
    version("0.9999999", sha256="2612a191a8d5842bfa057e41ba50bbb9dcb722419d2408c78cff4758d0754868", url="https://pypi.org/packages/ae/ae/bcb60402c60932b32dfaf19bb53870b29eda2cd17551ba5639219fb5ebf9/html5lib-0.9999999.tar.gz")
    version("0.999999", sha256="e372b66f4997f8e1de970ea755d0a528d7222d2aa9bd55aac078c7ef39b8f6c3", url="https://pypi.org/packages/78/8d/1661477d643e5dfd55f482201470e7fdbefd617e9848df39ba397e55d14a/html5lib-0.999999.tar.gz")
    version("0.99999", sha256="6b0bc7e9f77bb2a8ace636a827d8fb6e2f0b53e20cf0cb5e3e5b970454f8370b", url="https://pypi.org/packages/0d/0f/6e7a4171c150e4c52cff10184697a63dd9eaeae5c7b7f5023ef6b16aaf59/html5lib-0.99999.tar.gz")
    version("0.9999", sha256="87842c95c482239e5baf5d7fed1c56b8cdfdaedaba02415a56defe26f15d9bd4", url="https://pypi.org/packages/c2/0d/656e77a2a0e2e1487c5a40d394e7a80e5e038825b1dacc922d0d642cf1aa/html5lib-0.9999.tar.gz")
    version("0.999", sha256="c3887f7e2875d7666107fa8bee761ff95b9391acdcc7cd1b5fd57a23b5fbc49e", url="https://pypi.org/packages/fc/37/a7d7d3e5151e4ff0d364cc47a52d18c334eee60485b7318550b8e09f9d53/html5lib-0.999.tar.gz")
    version("0.99", sha256="aff6fd3031c563883197e5a04b7df324086ff5f358278a0386808c463a077e59", url="https://pypi.org/packages/2c/e8/4944b8a4e48951cf9db0cd05c4efdfc341583017f66d67b04ac1f4e63ab5/html5lib-0.99.tar.gz")

    with default_args(type="run"):
        depends_on("py-six@1.9:", when="@1.0.1:")
        depends_on("py-webencodings", when="@1.0.1:")

