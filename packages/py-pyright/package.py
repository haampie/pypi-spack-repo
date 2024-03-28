# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyright(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("1.1.356", sha256="a101b0f375f93d7082f9046cfaa7ba15b7cf8e1939ace45e984c351f6e8feb99", url="https://pypi.org/packages/75/1c/e924a4c9b0b07138c57f3a60b19a94d20ddf93c1aaa4df8f1b84ff9b2911/pyright-1.1.356-py3-none-any.whl")
    version("1.1.355", sha256="bf30b6728fd68ae7d09c98292b67152858dd89738569836896df786e52b5fe48", url="https://pypi.org/packages/ed/a6/bc9e80336902fcb5e72b3a12a639d99b5a60e2ab5b2f00f3cf8cab479655/pyright-1.1.355-py3-none-any.whl")
    version("1.1.354", sha256="f28d61ae8ae035fc52ded1070e8d9e786051a26a4127bbd7a4ba0399b81b37b5", url="https://pypi.org/packages/b9/0f/a0151f2c10b3823c10335657bfe4c7d59e71d3529c94d416940f062bb08f/pyright-1.1.354-py3-none-any.whl")
    version("1.1.353", sha256="8d7e6719d0be4fd9f4a37f010237c6a74d91ec1e7c81de634c2f3f9965f8ab43", url="https://pypi.org/packages/75/86/e2f88eb68126ad3fdee5f575a6aaf2c87524bfa1be009200cddd4cb5fc11/pyright-1.1.353-py3-none-any.whl")
    version("1.1.352", sha256="0040cf173c6a60704e553bfd129dfe54de59cc76d0b2b80f77cfab4f50701d64", url="https://pypi.org/packages/4a/51/7562aeb1c56b5378ad8b45618f48de52d2718400b274293e35a5d1b57e74/pyright-1.1.352-py3-none-any.whl")
    version("1.1.351", sha256="83b44b25396ae20661fc5f133c3fce30928ff1296d4f2e5ff0bca5fcf03eb89d", url="https://pypi.org/packages/23/75/2492ae386f9e1cf9dc5fb092991d3460303ebb0d8d143350a91d9529425f/pyright-1.1.351-py3-none-any.whl")
    version("1.1.350", sha256="f1dde6bcefd3c90aedbe9dd1c573e4c1ddbca8c74bf4fa664dd3b1a599ac9a66", url="https://pypi.org/packages/1c/6e/94b249c365e44c53fa89f419394b836635db26ce568fb36ecc54c2d868c6/pyright-1.1.350-py3-none-any.whl")
    version("1.1.349", sha256="8f9189ddb62222a35b3525666225f1d8f24244cbff5893c42b3f001d8ebafa1a", url="https://pypi.org/packages/e2/2f/fa05923d716e0aa76e457432719227047599f3543bf03d937a2af77a2041/pyright-1.1.349-py3-none-any.whl")
    version("1.1.348", sha256="e7d4df504c4c082b5c3725a8c15fc3fda62da5d09fc77994baa77f359a1b62f2", url="https://pypi.org/packages/dd/70/770b477b04b81317ef9cf45fe9976a768d5b1cb49b790993c8fd1b41455b/pyright-1.1.348-py3-none-any.whl")
    version("1.1.347", sha256="14dd31b594aa3ec464894f66b8a2d206ebef1501e52789eb88cf2a79b0907fbe", url="https://pypi.org/packages/ab/ac/ebcf9539ea9e35183740d5588a9777156b880ed5d5cf745785479fdd9b37/pyright-1.1.347-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-nodeenv@1.6:")
    # END DEPENDENCIES

