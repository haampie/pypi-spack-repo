# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyBlosc2(PythonPackage):
    # BEGIN VERSIONS
    version("2.5.1", sha256="47d5df50e7286edf81e629ece35f87f13f55c13c5e8545832188c420c75d1659", url="https://pypi.org/packages/f7/60/5bc8601f8ffcd5d8787b346898de8a0b454d031c3e158e3bbc312003984e/blosc2-2.5.1.tar.gz")
    version("2.5.0", sha256="22133ee3b101d9b2e4f922fe4876856dbbe093c99aa7ee4df2bb186502afb6d5", url="https://pypi.org/packages/55/e8/6754127df99a3cc6a0025cf54b30d65918ed9ab53c071caabc512d0f3231/blosc2-2.5.0.tar.gz")
    version("2.4.0", sha256="43687a9ebdd8befba962885fb991ab54d2710513696263f79d383aa22a7b1833", url="https://pypi.org/packages/89/73/8bd60f59fd090cd00e8291f07441e229e062d55b3d46eb4ab87de94ea556/blosc2-2.4.0.tar.gz")
    version("2.3.2", sha256="daf75a3ba973578732cb31848f1404fb5b465bdd821d437b6ff4b605e7f1e0c0", url="https://pypi.org/packages/3a/e0/ea2ca6388883e54b46398797104a87793c3d1498dc2a46894cb03efd48db/blosc2-2.3.2.tar.gz")
    version("2.3.1", sha256="d76b839ecfe2044f6ba43db9db95d223b37deb9225b5f337718caace62e70002", url="https://pypi.org/packages/11/ee/8cf3751166f1fea4a5d5b80499af6092e9ab52f21783064269f1ebf938ed/blosc2-2.3.1.tar.gz")
    version("2.3.0", sha256="2a1c664915b8226d602f03767fe0c8228232d0327546068e8952e1fbc2fd25f7", url="https://pypi.org/packages/58/a8/ff71cc6bcdcfa8003791b0f4db56641b197e9e24ccd4a66c83e65f16e57d/blosc2-2.3.0.tar.gz")
    version("2.2.9", sha256="63606498aaa72d58215b618d4512d5d3de29000a7b01a870edce8cb21d237c40", url="https://pypi.org/packages/53/cc/ef9893a19076b28f94b30f4746151b2e5c83a8222a66f3edd4d8179dcdb8/blosc2-2.2.9.tar.gz")
    version("2.2.8", sha256="59065aac5e9b01b0e9f3825d8e7f69f64b59bbfab148a47c54e4115f62a97474", url="https://pypi.org/packages/0a/66/ed9545df299067df5e87e49d6cdce6db594d7f32ee39f9deb4f0933c3422/blosc2-2.2.8.tar.gz")
    version("2.0.0", sha256="f19b0b3674f6c825b490f00d8264b0c540c2cdc11ec7e81178d38b83c57790a1", url="https://pypi.org/packages/6e/bb/339a2ea90db9c2c78ac6de8b4627f9d1ff1551fc260de2d54999f91a6538/blosc2-2.0.0.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.9:", when="@2.2.8")
        depends_on("py-msgpack", when="@2.2.7:")
        depends_on("py-ndindex@1.4:", when="@2.2.7:")
        depends_on("py-numpy@1.20.3:", when="@2.2.7:")
        depends_on("py-py-cpuinfo", when="@2.2.7:")
    # END DEPENDENCIES

