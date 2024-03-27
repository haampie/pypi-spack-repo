##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyYte(PythonPackage):
    version("1.5.4", sha256="14ccfcb57d60b7652041b606129851423805140b22f52f5152f7c2692cd7b905", url="https://pypi.org/packages/15/64/97df1886abf11291e9a18b1672b2b79eb940499263c85339a1645d870600/yte-1.5.4-py3-none-any.whl")
    version("1.5.1", sha256="fd646bc47c355f202f14b7476996de4a31501cf1e107ac7ad8e19edcd786d30b", url="https://pypi.org/packages/27/a2/638c528c6b35582b1de094de2ff2e8d0ac87c426ed04a375281356857bc7/yte-1.5.1-py3-none-any.whl")
    version("1.4.0", sha256="1e7d03e72eec2d7c311dd363f66069d6ff53fd4fecd99714fb0753fc0f3ab36b", url="https://pypi.org/packages/f4/16/5e39a562dc688498ef2f71fe755e247a109a47525d4bfc29b4e24f191772/yte-1.4.0-py3-none-any.whl")
    version("1.3.0", sha256="5d8d05a9043c581b420e11c5fdae73f1da5e6113c3bec397549a643e400e48d8", url="https://pypi.org/packages/82/f4/f843426353c5df6afda05ab17e96f82ff77095e1d25f98ade78854ae5468/yte-1.3.0-py3-none-any.whl")
    version("1.2.3", sha256="cb79a0b9204670a08e284a4689760cee0df1661c765d9ae81a751a8729257801", url="https://pypi.org/packages/95/3d/210f47fe592749be6d3898dd3f7888f7435bc513e0d74ae9aa4d83e0813d/yte-1.2.3-py3-none-any.whl")
    version("1.2.2", sha256="b930b617731a42551085716e09bfd7d931222f45f53a0c0728b6593d98e1e8bb", url="https://pypi.org/packages/52/d1/8675e2da35d767f326402585e347190b98ca847d08478670f353e9bd1dfa/yte-1.2.2-py3-none-any.whl")
    version("1.2.1", sha256="28ba7f8544c7916944fae1e970a3165cdf25e6ab89bf9006bf15919e7f7eb5fc", url="https://pypi.org/packages/be/18/f6c5b22071cbe629ba23be81a24d6251a64516a85b252b8c3db72e5c7f6f/yte-1.2.1-py3-none-any.whl")
    version("1.2.0", sha256="3f1a89c48c20a5db6bd6426d3f554916b5ebbcf90fdff5b5d210d4af992819ec", url="https://pypi.org/packages/fa/bb/f7bf08e6e2ede2aeb7eaa978ffa2c0a22cfc849b45b76f02d26c5ac462f3/yte-1.2.0-py3-none-any.whl")
    version("1.1.0", sha256="2fe8ddbbc4439090f3083dfa9746d26682312752334764f7b8e3be6142a10359", url="https://pypi.org/packages/18/c5/330ea01e83546c89c0706ccb597fa47c1b025cd9fa8522eb438a776e2b8a/yte-1.1.0-py3-none-any.whl")
    version("1.0.0", sha256="129ed48a848884e0e13a3cdc6cb8f52a5da103652a5b376bad487e8f2023e28c", url="https://pypi.org/packages/3b/d3/dbba84c250405194f53c6cf20bd5735701eb42bebdc9b972a449af773792/yte-1.0.0-py3-none-any.whl")

    with default_args(type="run"):
        depends_on("python@3.9:", when="@:0.1")
        depends_on("py-dpath@2.1:", when="@1.5.4:")
        depends_on("py-dpath@2:", when="@1.3:1.5.1")
        depends_on("py-plac@1.3.4:")
        depends_on("py-pyyaml@6.0:")

