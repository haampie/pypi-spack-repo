# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyFormulaic(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.6.1", sha256="3eebbee86bfde23f66c7b86f727b52e4f2af1b08be9ea752d2ea3fe2ff951fe8", url="https://pypi.org/packages/ad/79/1ce60c6368cfbfbc186f8ccd45edaa945e0a8dba77469c7f3f0cc44db40e/formulaic-0.6.1-py3-none-any.whl")
    version("0.5.2", sha256="65d04b1249584504912eb64f83b47fc1e7e95b0ff3e24fb0859148e2f2f033c2", url="https://pypi.org/packages/15/3c/5853059034a58de0b79de67584a22d6fa8f732a1cb7a388942c735584c3e/formulaic-0.5.2-py3-none-any.whl")
    version("0.5.1", sha256="5b079477790b3aedc3760439ba53278da778c90da4a90cfedb4e8f1693ccbb02", url="https://pypi.org/packages/69/f7/924c6760cd9494403dae54ab85126c7f911cf6248e68801f721267358bff/formulaic-0.5.1-py3-none-any.whl")
    version("0.5.0", sha256="11d00aeebfd7e56b4f62bc954c218f3ec766193fbf987d83c25c56b05422f516", url="https://pypi.org/packages/1b/77/818d7192c033a767078d6f730ee5c86af3048e7478130fd9fbae762a1f15/formulaic-0.5.0-py3-none-any.whl")
    version("0.4.0", sha256="9c3f95220606e61ee6b675e5d74bd7e74fdd7494f2e1e2319333cbc4805fcc5f", url="https://pypi.org/packages/df/6e/4abb6f2c45aba7c2d5a91ea66888ac1132b2a413829b755d6fc88ca9d46b/formulaic-0.4.0-py3-none-any.whl")
    version("0.3.4", sha256="5ee1f3f4a5990c0947a68f90d051a4ca497d6eb0f9f387d2cf1e732a9cbf76ec", url="https://pypi.org/packages/1a/ae/c3ce1d2935abddef895fd6b0e4f1a06c8d5ff92f6f7ed87861f6e1616df2/formulaic-0.3.4-py3-none-any.whl")
    version("0.3.3", sha256="a126d337741c6b4c699db5a52e3e5954abe0865949424f153be45c4a9c02422e", url="https://pypi.org/packages/a8/41/55ad9306e0c70df43643bab029b30b9609d28df79c1e66718f1df226ae0c/formulaic-0.3.3-py3-none-any.whl")
    version("0.3.2", sha256="d64f69c6865864ac2b27e4e1ff2d246f0425af13655be0ffc5a7b4b43610e962", url="https://pypi.org/packages/47/3e/82676b1e9c4269c25819062f1d783270565661dfd21349282f1521b7e13b/formulaic-0.3.2-py3-none-any.whl")
    version("0.3.1", sha256="f53b92095df9e3874033c92c8bb735e00d90d34789e60cb4afc428be942754d8", url="https://pypi.org/packages/e0/d1/f02ed1e34389ace0da9c03ec6375bd96cf2da0b32f8a684bd936a9238ee8/formulaic-0.3.1-py3-none-any.whl")
    version("0.3.0", sha256="a84384b8bd84c4381fca6364fb5f6d99a401f1b7ea0cc64a84e3297e1a717f9a", url="https://pypi.org/packages/9c/24/eee2b038a75af0fe47e37afc07da5a89552d60e840e396b79b8442e270bb/formulaic-0.3.0-py3-none-any.whl")
    version("0.2.4", sha256="775620d93f24f01b33a17aa2cf65a04112003c5112f12015368e4e4605a5013b", url="https://pypi.org/packages/45/40/3c337ed87b8ffeb129f21db97bce3d4f1e9125ed4697969348bb6f871931/formulaic-0.2.4-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-astor@0.8:", when="@1: ^python@:3.8")
        depends_on("py-astor@0.8:", when="@0.3.4:0")
        depends_on("py-astor@0.7", when="@0.3.3")
        depends_on("py-astor@0.7:", when="@0.3:0.3.2")
        depends_on("py-astor", when="@0.1:0.2")
        depends_on("py-graphlib-backport", when="@0.4: ^python@:3.8")
        depends_on("py-interface-meta@1.2:", when="@0.2:")
        depends_on("py-numpy@1.16.5:", when="@0.5:")
        depends_on("py-numpy@1.3:", when="@0.3:0.4")
        depends_on("py-numpy", when="@0.2")
        depends_on("py-pandas@1.0.0:", when="@0.4:")
        depends_on("py-pandas@1.2.0:", when="@0.3")
        depends_on("py-pandas", when="@0.1:0.2")
        depends_on("py-scipy@1.6.0:", when="@0.3:")
        depends_on("py-scipy", when="@0.1:0.2")
        depends_on("py-typing-extensions@4.2:", when="@0.4:")
        depends_on("py-wrapt", when="@0.1:")
    # END DEPENDENCIES

