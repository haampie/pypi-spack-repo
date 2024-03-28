# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyQuaternionic(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("1.0.10", sha256="d9e6c68f24f1b42d38596db7165ae82151c075e44dbf9c6edc5b69f4e99ad2b0", url="https://pypi.org/packages/b3/c2/c7730006f348a42e6ac84119111ceebd154c499f6405bf4e0f4362e8a7b7/quaternionic-1.0.10-py3-none-any.whl")
    version("1.0.9", sha256="78856e7e7511db0bd456010473d0176c4210a72dc51ff3fb7d7b3fb867e7a523", url="https://pypi.org/packages/56/06/007a32e74d4a065e78de3de10b90d6e0eef280054cf1ede017c6a113cbd1/quaternionic-1.0.9-py3-none-any.whl")
    version("1.0.8", sha256="bb37e3ef6d3dc275a604d03fe2abfb314bc6d0ba9fe63e70e5050a510ee5a7e7", url="https://pypi.org/packages/25/6b/30c40192b788477d9471c648b20331c252e0a37cd090b73fe09be1fb740f/quaternionic-1.0.8-py3-none-any.whl")
    version("1.0.6", sha256="c4720937eb8c0816aee3c96a8a47f1c9159776273e95d13934467763c066caad", url="https://pypi.org/packages/eb/91/714d16b38fa3a5878897b0afb45643d25088a0c5ef17dd6709e2e1108487/quaternionic-1.0.6-py3-none-any.whl")
    version("1.0.5", sha256="5b397e039668066661688f334a275848ff984c0ea3322b37947c82fb782a7b7d", url="https://pypi.org/packages/4f/c5/6f8772834ea9789f43c49d36eba59dbf704849739decc6cf87b9abaeacb5/quaternionic-1.0.5-py3-none-any.whl")
    version("1.0.4", sha256="a04227cd6864ddd819ec641d14f3a8785d023bef7b9895228c0b1203dd03eff6", url="https://pypi.org/packages/23/48/8e5d42a4e451994bfe3692095ebcbb332df790c7b696129b88ef6f1f5b2d/quaternionic-1.0.4-py3-none-any.whl")
    version("1.0.3", sha256="6888c451aa4fcea2b2d532aabfa66d312c542a8a916bffa97607d221c8d645ee", url="https://pypi.org/packages/61/e9/c9c15b403a4ac01c9781982d29e8a66198659fbe86802924658b3505a680/quaternionic-1.0.3-py3-none-any.whl")
    version("1.0.2", sha256="ebb3ecb827a534baa1a9e58de8f8f3f4aa33f4156b3d003c42c33bd18a941034", url="https://pypi.org/packages/13/64/2aa2c8febd1da63f0e88ab6a25f89a25fe16044f9d5719d3280f5fff37e6/quaternionic-1.0.2-py3-none-any.whl")
    version("1.0.1", sha256="5e9ce1fa6a25d7339d3a9a9f4582b0244cbced21e289982c0fb2e0a54eabf491", url="https://pypi.org/packages/0c/fe/cc8eb0bccf084aa1cdeb777cd8adb5380e0a440ff98b4bb2dae653b6288c/quaternionic-1.0.1-py3-none-any.whl")
    version("1.0.0", sha256="97f85296135ea45b20ac079533b813068e3dbfb3f4ce196c43486d4182c7d62b", url="https://pypi.org/packages/43/ba/179564619bea893a562aef92d397cef15cf6068145ff185b7bf35b9f20bc/quaternionic-1.0.0-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@:3.11", when="@1.0.6")
        depends_on("python@:3.10", when="@1.0.2:1.0.5")
        depends_on("python@:3.9", when="@0.3:1.0.1")
        depends_on("py-black@22:", when="@1.0.2:1.0.4")
        depends_on("py-black@20.8-beta1:", when="@0.1.10:1.0.1")
        depends_on("py-numba@0.55.0:", when="@1.0.2:")
        depends_on("py-numba@0.50.0:", when="@0.1.10:1.0.1")
        depends_on("py-numpy@1.20.0:", when="@1.0.8:")
        depends_on("py-numpy@1.19.0:1", when="@1.0.2:1.0.6")
        depends_on("py-numpy@1.13.0:1", when="@:1.0.1")
        depends_on("py-scipy@1.5.0:", when="@1.0.8:")
        depends_on("py-scipy@1.0.0:", when="@:1.0.6")
    # END DEPENDENCIES

