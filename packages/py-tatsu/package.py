# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyTatsu(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("5.12.0", sha256="a7a13bea264b749963695a3c42ef5631811330887882cb0de2c2ad6e2348f986", url="https://pypi.org/packages/cf/44/f2c21d888cb57e6b0b8db0026dd32f9b3532993e16b78518513d9b6369a7/TatSu-5.12.0-py3-none-any.whl")
    version("5.11.3", sha256="97954dfad6a3f73c7179f88d706eab6be92e6753e1c09e9e28cd726aa2f8e22b", url="https://pypi.org/packages/f9/aa/abc4313688d431ba690de10bc94cf3d690cd2cbbc44f1101add7471ab1de/TatSu-5.11.3-py3-none-any.whl")
    version("5.11.2", sha256="fef2a34f21d9180fdca251177390c1c53df5898de143070615c13ff6bd268e56", url="https://pypi.org/packages/52/68/bd7f90df3d22f915b4d6198b806d362721a0e4270a48b21180e2161e1373/TatSu-5.11.2-py3-none-any.whl")
    version("5.11.1", sha256="0044cfa7cfadb8f9ee9f6ed652b46064add81730d84010b9b4975f9b671e8c12", url="https://pypi.org/packages/d8/a4/ac07ab150d9f593030866428e76d7ff72b44577ee61222629cb3f8214ec6/TatSu-5.11.1-py3-none-any.whl")
    version("5.11.0", sha256="12c17c2713665f9e8d1430236ec92a666c136470cae24d34010b7da1b6b2fff1", url="https://pypi.org/packages/9e/c9/2f32e3f8da471c88f8dcb5c5940613b853fc44270c5dd1c1594a2921319a/TatSu-5.11.0-py3-none-any.whl")
    version("5.10.6", sha256="de992c0d1c85ef396c305d0f63db30e5d9da771128b091955c39e1bc2f7951c9", url="https://pypi.org/packages/4d/bb/2d3e93bccabfffb0e202712e24c85f96438b7dd4f8c727b8c2c3146e79a5/TatSu-5.10.6-py3-none-any.whl")
    version("5.10.5", sha256="276364c6eef4d6a368b1f46137c1bb5d88c75c996b356b27d5a0187e36f7434d", url="https://pypi.org/packages/86/35/42b1b996e69c3269ce9b0fd55840900cdcf67b00d4a054a8e5dc72799c75/TatSu-5.10.5-py3-none-any.whl")
    version("5.10.4", sha256="e75e09241ad994dcc4663e96595f98a446447817e5a26ad26823339703634e4d", url="https://pypi.org/packages/01/c0/09b734d1608376d901986d62eb929f7be4c21080c3f4c6b2c67c0e34115e/TatSu-5.10.4-py3-none-any.whl")
    version("5.10.3", sha256="d3d90d0f73c9b6ab2a18a92ce0723f9528bacd90b0f85ef6f6cdf52c9ea09294", url="https://pypi.org/packages/e6/c6/a886d06a39e7dcb08c5b613a0526c386ab530b85b729358f05ebfccc7254/TatSu-5.10.3-py3-none-any.whl")
    version("5.10.2", sha256="24f85671c71936226989b468661fc95b288fe96c68549536f5791f0311eb8dcd", url="https://pypi.org/packages/0a/7c/f384c61de69468ffeecdeee30f3eb3375b46183dfe968fd89eeb4829d924/TatSu-5.10.2-py3-none-any.whl")
    version("4.4.0", sha256="c9211eeee9a2d4c90f69879ec0b518b1aa0d9450249cb0dd181f5f5b18be0a92", url="https://pypi.org/packages/1b/36/00664e684e4bba5730db661847447bbcfe789008a154755013e5f457b648/TatSu-4.4.0-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    variant("future_regex", default=False)
    # END VARIANTS

    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.11:", when="@5.9:")
        depends_on("python@3.10:", when="@5.7.1:5.7.3,5.8:5.8.2")
    # END DEPENDENCIES

