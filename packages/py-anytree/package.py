##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyAnytree(PythonPackage):
    version("2.8.0", sha256="14c55ac77492b11532395049a03b773d14c7e30b22aa012e337b1e983de31521", url="https://pypi.org/packages/a8/65/be23d8c3ecd68d40541d49812cd94ed0f3ee37eb88669ca15df0e43daed1/anytree-2.8.0-py2.py3-none-any.whl")
    version("2.7.3", sha256="34c8f62a3c28b474313414ce52afe17589e9c154bfddea5d6be7bc7bfcbf3faa", url="https://pypi.org/packages/d1/c3/f610cbdcdeb0f3580dd4652091192418faa3781e16096dfe6853857baaa6/anytree-2.7.3-py2.py3-none-any.whl")
    version("2.7.2", sha256="6692679795c7a2ef877c01b0d5131f2c08945ef21445c082d55f08b07d1b41f3", url="https://pypi.org/packages/aa/3c/c6f460664fb7c09a8647de457c206586761c54dcfa71d442733fc21ed5f8/anytree-2.7.2.tar.gz")
    version("2.7.1", sha256="afe3bfa3fb4fb18b4023d92c98179cd86de6148d9d519b61dcc81c80e7391006", url="https://pypi.org/packages/62/89/640f607533415dd4b6d7a6d981614651a5763c1a1b55124bce8d27834073/anytree-2.7.1.tar.gz")
    version("2.7.0", sha256="e39ad6f4ef112a496c92f6cadf6ec0703ab2d5dc1795d503d883ca875ec32333", url="https://pypi.org/packages/7c/08/dbd4a7c857ff83f9652477b9babc672bc50c3e59249d27d1c84af3a1ed63/anytree-2.7.0-py2.py3-none-any.whl")
    version("2.6.0", sha256="a221b6a603c3a5d5e417894dc48eaa8b1eab04056e1f5bb509bcfff0e7a47883", url="https://pypi.org/packages/78/bf/9300ecef72d105b3a76de6930916458d6bb8c7e787f5efb1c510bf898873/anytree-2.6.0.tar.gz")
    version("2.5.0", sha256="4de1010295b47a607a2a0cde6417f6f1b412225654f6606d6d4f5385b5b4c10a", url="https://pypi.org/packages/61/32/3a73d48a9008fc1e960b5b60ef546501ea9c4727537fe25155c5f657f82b/anytree-2.5.0-py2.py3-none-any.whl")
    version("2.4.3", sha256="9b43699eacfd3fab153433abbc698c74e3c8f883c0505fde2c26ad38163d93fa", url="https://pypi.org/packages/b9/cd/abd10f53ba136c77dd6c68aa96d9e6881b9713c4778fd8e854ff5d9787ba/anytree-2.4.3.tar.gz")

    with default_args(type="run"):
        depends_on("py-six@1.9:", when="@2.5,2.7:2.7.0,2.7.3:2.8")

