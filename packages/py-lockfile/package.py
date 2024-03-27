##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyLockfile(PythonPackage):
    version("0.12.2", sha256="6c3cb24f344923d30b2785d5ad75182c8ea7ac1b6171b08657258ec7429d50fa", url="https://pypi.org/packages/c8/22/9460e311f340cb62d26a38c419b1381b8593b0bb6b5d1f056938b086d362/lockfile-0.12.2-py2.py3-none-any.whl")
    version("0.11.0", sha256="eed7e0c829135aaaf2a9df83652bc6e2cc50175d933741c25aac0394674e7fd3", url="https://pypi.org/packages/64/61/2e2b7424f5751f66f37ac12e10ffe94ea4b5bcccc697eccb19142bcf7c54/lockfile-0.11.0.tar.gz")
    version("0.10.2", sha256="9e42252f17d1dd89ee31745e0c4fbe58862c25147eb0ef5295c9cd9bcb4ea2c1", url="https://pypi.org/packages/6a/11/114c67b0e3c25c19497fde977538339530d8ffa050d6ec9349793f933faa/lockfile-0.10.2.tar.gz")
    version("0.9.1", sha256="23da589c91f59cb7c644d5ce5df539d448341bd479917d6dde973f82e2719147", url="https://pypi.org/packages/fb/89/af965281e233d8722002a4b7b7b0b650d46875d03faa7e83a1463d6789e1/lockfile-0.9.1.tar.gz")

    with default_args(type="run"):
        depends_on("py-pbr@0.6,0.8:0", when="@0.11")

