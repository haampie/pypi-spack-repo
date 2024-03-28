# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyNptyping(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("2.5.0", sha256="764e51836faae33a7ae2e928af574cfb701355647accadcc89f2ad793630b7c8", url="https://pypi.org/packages/b1/28/92edc05378175de13a3d4986cee7531853634a22b7e5e21a988fa84fde3f/nptyping-2.5.0-py3-none-any.whl")
    version("2.4.1", sha256="23e8164b1e2c55e872f392ca7516b9b1b0cb400b03b70accaa63998b4106b0b3", url="https://pypi.org/packages/b2/c1/e6f8c5f28f9b3bdb5c9c1d349a51941a30f90347b82bd5594363e81cf3ff/nptyping-2.4.1-py3-none-any.whl")
    version("2.4.0", sha256="7aa52fe4fb159a4c6314b2ad374fe706aac53d2e347ec97284e2c5f37143546c", url="https://pypi.org/packages/11/e4/66920efbce907f49f725ce22f089c36c1cd98d3074c504b1a843327f3ed5/nptyping-2.4.0-py3-none-any.whl")
    version("2.3.1", sha256="7549bc1fb334178d0309ad1ab89e174844ebe38dd427eae2f61e7495a9bda388", url="https://pypi.org/packages/1e/cf/be960d599feb6e2e586c8b2abe29562b76fc1cea3ed11f089be87ee6c122/nptyping-2.3.1-py3-none-any.whl")
    version("2.3.0", sha256="52652be125c4cfdf56567290c16df1210aa40a3b3db95c0b213bda06c0877d66", url="https://pypi.org/packages/3e/cd/b6965b700c7d77b4016a75e10ecd1d29a0e24ccdab246de1eb7586af9205/nptyping-2.3.0-py3-none-any.whl")
    version("2.2.0", sha256="3b752f498edfea24fd90bbbfb7f683fd0365377f20b43de4cb7541b57ca2e13a", url="https://pypi.org/packages/a1/4f/9196a5d6091bd3ccdf92200926edd193aae44a8d742fdd3933d552e88922/nptyping-2.2.0-py3-none-any.whl")
    version("2.1.3", sha256="f12131d8b4ef843085bd06282d44763cf48b54a87cbe713e42f3367484be0abc", url="https://pypi.org/packages/a3/a6/50e0fcf477c7cc065b08fb231cb049ab1b3d73c87bceaa32e720a01328dd/nptyping-2.1.3-py3-none-any.whl")
    version("2.1.2", sha256="d0ca7a9be4f5f6a5a19b58f41ff3072e8fd61f8f1b10000c07b0e32b2ae36751", url="https://pypi.org/packages/39/43/5100bbdd87d7dcff733dad65d8e42c789722469d2e47429def38e355422b/nptyping-2.1.2-py3-none-any.whl")
    version("2.1.1", sha256="0eab214b5b960b755caa2344a1b2a7ee5e24eee9bfeee955809e413f30cfd593", url="https://pypi.org/packages/d7/a0/4073a26abb151485985eb4ff5cb1c5ab095ca1f3e5861d6f52e7832cf389/nptyping-2.1.1-py3-none-any.whl")
    version("2.1.0", sha256="1b4b84e3ff9d22d6f90b3cfd95657affb310307746863f5fd7551e26e0863954", url="https://pypi.org/packages/a3/9d/f5f80bca30a8a27463c79e31f251f5269579b02ad136ac3fcdc1dfa90070/nptyping-2.1.0-py3-none-any.whl")
    version("1.4.1", sha256="5ccc9bd3d284af1ffaef32ab7f3eb71f584c8c4e71c1dfac0999054ea47beb1c", url="https://pypi.org/packages/ad/5b/e8c90a98b8462768ca43ad43021d404b81430fde28a6e8f93a8101fe9a8f/nptyping-1.4.1-py3-none-any.whl")
    version("1.0.1", sha256="9f782826d5749fd8448c156b46b2deb84b3a09db860ac4a9881f4e5bd5181afd", url="https://pypi.org/packages/73/11/9e15ef1cd231182a3b568b65a612a173061d826de805481f44848fc27a32/nptyping-1.0.1-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-numpy@1.20.0:1", when="@2.1:")
        depends_on("py-numpy", when="@:1")
        depends_on("py-typing-extensions@4:", when="@2.1: ^python@:3.9")
        depends_on("py-typish@1.7:", when="@1.4:1")
        depends_on("py-typish@1.5.2:", when="@1:1.3")
    # END DEPENDENCIES

