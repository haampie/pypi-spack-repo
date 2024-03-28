# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyContourpy(PythonPackage):
    # BEGIN VERSIONS
    version("1.2.1-rc1", sha256="502d19590fd3bfe01fe8eb0084f612b40352680477ef75cf239e7ecd0088dee0", url="https://pypi.org/packages/48/23/490651467c3b52051fbbf87797c0875d657387be2d03536e37f0176a7771/contourpy-1.2.1rc1.tar.gz")
    version("1.2.0", sha256="171f311cb758de7da13fc53af221ae47a5877be5a0843a9fe150818c51ed276a", url="https://pypi.org/packages/11/a3/48ddc7ae832b000952cf4be64452381d150a41a2299c2eb19237168528d1/contourpy-1.2.0.tar.gz")
    version("1.1.1", sha256="96ba37c2e24b7212a77da85004c38e7c4d155d3e72a45eeaf22c1f03f607e8ab", url="https://pypi.org/packages/b1/7d/087ee4295e7580d3f7eb8a8a4e0ec8c7847e60f34135248ccf831cf5bbfc/contourpy-1.1.1.tar.gz")
    version("1.1.0", sha256="e53046c3863828d21d531cc3b53786e6580eb1ba02477e8681009b6aa0870b21", url="https://pypi.org/packages/a7/3b/632c003e1dfbc82d32c0466762f2d2cf139d26032626dc65944e38d0e5b9/contourpy-1.1.0.tar.gz")
    version("1.0.7", sha256="d8165a088d31798b59e91117d1f5fc3df8168d8b48c4acc10fc0df0d0bdbcc5e", url="https://pypi.org/packages/b4/9b/6edb9d3e334a70a212f66a844188fcb57ddbd528cbc3b1fe7abfc317ddd7/contourpy-1.0.7.tar.gz")
    version("1.0.6", sha256="6e459ebb8bb5ee4c22c19cc000174f8059981971a33ce11e17dddf6aca97a142", url="https://pypi.org/packages/8f/4f/8a5789867f2a928fd9b32e7e8d4bc0f27a765aa7056989e7427f2c2a1966/contourpy-1.0.6.tar.gz")
    version("1.0.5", sha256="896631cd40222aef3697e4e51177d14c3709fda49d30983269d584f034acc8a4", url="https://pypi.org/packages/38/b3/d6fd43ab2eadce72ac089328d80e9cdf274efdb79a9933aaf52ef1621e99/contourpy-1.0.5.tar.gz")
    version("1.0.4", sha256="10d0570f5001293c73e2d7277d8eafae80ca093bade208c0bf4695d1b173a8c3", url="https://pypi.org/packages/e4/86/dee8ede1493b727927fb6ac0c8ebcb523a076f187c8292615cdc438f627a/contourpy-1.0.4.tar.gz")
    version("1.0.3", sha256="5a747ef2ebd994a90de6e5fc53e78bca4d4bc76422307cac15a71ad95028772b", url="https://pypi.org/packages/1e/49/004641fdd67641ac9564ca6c14ea9540c66fb4c14d8183ec231629e63b9f/contourpy-1.0.3.tar.gz")
    version("1.0.2", sha256="ea94bd4f15e3526e399c36ad18155d6a550fcd6fddb45cdaaaddedfb8e7e5a97", url="https://pypi.org/packages/00/21/649a9988dcffa4f3210eef7235d68cf00f178f5ffa3da2be584559f05274/contourpy-1.0.2.tar.gz")
    version("1.0.1", sha256="11630484047cf8345d7084818de1d93c14d85e6e6c9304c2e76fb64cda39c4e7", url="https://pypi.org/packages/9d/2f/7a2805a52a56f4ce5d62448d937e4ae403fc3f48d2e7d7a7c8883f8319cd/contourpy-1.0.1.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.9:", when="@1.2:")
        depends_on("py-numpy@1.20.0:", when="@1.2.1-rc1:")
        depends_on("py-numpy@1.20.0:1", when="@1.2:1.2.0")
        depends_on("py-numpy@1.26.0-rc1:1", when="@1.1.1-rc1:1.1 ^python@3.12:")
        depends_on("py-numpy@1.16.0:1", when="@1.1.1-rc1:1.1 ^python@:3.11.0")
        depends_on("py-numpy@1.16.0:", when="@1.1:1.1.0")
    # END DEPENDENCIES

