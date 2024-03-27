##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyAnsimarkup(PythonPackage):
    version("2.1.0", sha256="51ab9f3157125c53e93d8fd2e92df37dfa1757c9f2371ed48554e111c7d4401a", url="https://pypi.org/packages/60/99/878823a360a0bd9ae034d39fe37f8fdd976de8da642c2ec608f093efc273/ansimarkup-2.1.0-py3-none-any.whl")
    version("2.0.0", sha256="7edbfc6fc9cbf67589bc510ff5502aa34a2de8db9ceed61b186864af6426a70e", url="https://pypi.org/packages/28/a5/746c844af06b87993edea2a215e6a3ce8da75a28fbb4998ab39ac3902ce6/ansimarkup-2.0.0-py3-none-any.whl")
    version("1.5.0", sha256="3146ca74af5f69e48a9c3d41b31085c0d6378f803edeb364856d37c11a684acf", url="https://pypi.org/packages/22/09/3ad81e40d752ef51a9a8c320c9385de0d98a4dad68c0e4f793befc610f56/ansimarkup-1.5.0-py2.py3-none-any.whl")
    version("1.4.1", sha256="2ea88deb1900e9446922a17cf3583fd04351f9a7f1d056dba783cb5c824bfcd5", url="https://pypi.org/packages/c0/b3/9ac6cc9cd8addb3464987bec4fa95045983fcfb720bb175b268b373ee33f/ansimarkup-1.4.1-py2.py3-none-any.whl")
    version("1.4.0", sha256="174d920481416cec8d5a707af542d6fba25a1df1c21d8996479c32ba453649a4", url="https://pypi.org/packages/26/36/57272102d00be2f8c173c8ebdcff95eff067b486e3041fd7a0de71e91700/ansimarkup-1.4.0.tar.gz")
    version("1.3.0", sha256="6e071a5cdb6824362f2b6a8699ab88e07114ba5e0d480a55e872b746b81c86ff", url="https://pypi.org/packages/a6/92/9aa2b983207dab0ca81bcaebe38954014d7ef35b649127432ba2c620a5a5/ansimarkup-1.3.0.tar.gz")
    version("1.2.0", sha256="1910408423c1c22230cdd354947222c2b8ba7f855491f3d9f4c588b0f32c9a1a", url="https://pypi.org/packages/de/2c/ae3d13ad85dc194e577c7720aed726d789fd26f5d9d150fd4ad32176b875/ansimarkup-1.2.0.tar.gz")
    version("1.1.0", sha256="6fd3a9bef886b07839f9b04501f4f82863aba439c8dae526585c082607574ef7", url="https://pypi.org/packages/dc/91/c376cac274f7fd042b96200a71f692609ad678166890b500887898ccd383/ansimarkup-1.1.0.tar.gz")
    version("1.0.0", sha256="e9a23a3c259acad157c69281e1733292b148e4308e78fd097842094943f53905", url="https://pypi.org/packages/69/a1/1318c5a30b71d59194a4e01ff3a847fb755708a7f6ee976e5cc59651b984/ansimarkup-1.0.0.tar.gz")

    with default_args(type="run"):
        depends_on("py-colorama", when="@1.4.1:")

