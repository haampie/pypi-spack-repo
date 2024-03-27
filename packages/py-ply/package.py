##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPly(PythonPackage):
    version("3.11", sha256="00c7c1aaa88358b9c765b6d3000c6eec0ba42abca5351b095321aef446081da3", url="https://pypi.org/packages/e5/69/882ee5c9d017149285cab114ebeab373308ef0f874fcdac9beb90e0ac4da/ply-3.11.tar.gz")
    version("3.10", sha256="96e94af7dd7031d8d6dd6e2a8e0de593b511c211a86e28a9c9621c275ac8bacb", url="https://pypi.org/packages/ce/3d/1f9ca69192025046f02a02ffc61bfbac2731aab06325a218370fd93e18df/ply-3.10.tar.gz")
    version("3.9", sha256="0d7e2940b9c57151392fceaa62b0865c45e06ce1e36687fd8d03f011a907f43e", url="https://pypi.org/packages/a8/4d/487e12d0478ee0cbb15d6fe9b8916e98fe4e2fce4cc65e4de309209c0b24/ply-3.9.tar.gz")
    version("3.8", sha256="e7d1bdff026beb159c9942f7a17e102c375638d9478a7ecd4cc0c76afd8de0b8", url="https://pypi.org/packages/96/e0/430fcdb6b3ef1ae534d231397bee7e9304be14a47a267e82ebcb3323d0b5/ply-3.8.tar.gz")
    version("3.6", sha256="61367b9eb2f4b819f69ea116750305270f1df8859992c9e356d6a851f25a4b47", url="https://pypi.org/packages/7f/ea/6aff5b67ddb00d38fa6498df2010b50529700621353d38ac29d25ddb0845/ply-3.6.tar.gz")
    version("3.4", sha256="af435f11b7bdd69da5ffbc3fecb8d70a7073ec952e101764c88720cdefb2546b", url="https://pypi.org/packages/40/7d/95a7a67fb4c2205d0cbf89e8fabb7b49b4ed812ffdab45510d124bc2bd7e/ply-3.4.tar.gz")


