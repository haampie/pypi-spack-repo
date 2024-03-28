# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyConsolekit(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("1.6.0", sha256="53d05dba2a38c28532f2b193a4e7b68054821e201d39d7ca818753d4add603c1", url="https://pypi.org/packages/4d/f2/14af4f2ff61f9dd6b6e089edbd7de345b6adf75391494f328d4179e63eae/consolekit-1.6.0-py3-none-any.whl")
    version("1.5.2", sha256="f1b11d4475f0a803fbd01de002e8f7d74a90c1d02e821e8b0a52ff8cb63f71c7", url="https://pypi.org/packages/36/b3/93b955675b808623fcb71a8d0be4ed3103137fd423bc71987c9e339d5882/consolekit-1.5.2-py3-none-any.whl")
    version("1.5.1", sha256="5f9f98b2d618d51cd9ddb73062c531811253d144b05ae351a972867b4ecde7b9", url="https://pypi.org/packages/3e/86/93eb5e2bd7b05cb04cf555da79c4bb769c5d0966c5592831273b570e4129/consolekit-1.5.1-py3-none-any.whl")
    version("1.5.0", sha256="3bad99ace60b3a68fd8de0c08dc93136500b6f9e1d221d07ae5f122c71742f7d", url="https://pypi.org/packages/b7/2d/11119df58247064e8a3f3268c9341ceeb2c2e51517ed31b7ee43647577fe/consolekit-1.5.0-py3-none-any.whl")
    version("1.4.1", sha256="698dca1d1b712b76efc115922a8c8d679bf0d97cadb917404d5f68a1b3f300d7", url="https://pypi.org/packages/a4/58/773c93d7969fae9708e7522484ee5a0629226173d795269da011729fd005/consolekit-1.4.1-py3-none-any.whl")
    version("1.4.0", sha256="8e0d0cc8de3e1a72c1b2fc1c7cc13cdabb8cfe396e7f04e6844f726fef4254ea", url="https://pypi.org/packages/05/8e/ab8827701ed5d3150ce14157865e2432bedb13d90e703ad8a3e1af7e8ccf/consolekit-1.4.0-py3-none-any.whl")
    version("1.3.3", sha256="4f8a04d2af3585117beba029b91975cf36266abf9b141b5eec73a8d89af4339d", url="https://pypi.org/packages/19/cc/ea1bb8a8e03989d3c9ebc20a7c2700ef8f2aaca41fca1ca8c12af7f0f763/consolekit-1.3.3-py3-none-any.whl")
    version("1.3.2", sha256="6f980306b12ec228096c05ca9b49251ccf27af0919998521b74f86508d366715", url="https://pypi.org/packages/0e/03/cde736483f74113d5cbf19b7d5342ee4dbbcf0d151540ca393ba57209a81/consolekit-1.3.2-py3-none-any.whl")
    version("1.3.1", sha256="ecdff040f97aa413fd77bbfbfe30f1a9b3ed0f67dc32277381172b8ac165391c", url="https://pypi.org/packages/6d/d7/5fb62c82409b0d3370fa800d0d7e654785bd2aef0bb71ecb0f5f6e7a327b/consolekit-1.3.1-py3-none-any.whl")
    version("1.3.0", sha256="be4d6486840d08b518f8b8f8eade248c2b1839979a93a19d8f6a631b95036e21", url="https://pypi.org/packages/ab/be/cec2ef889181dde8f1c3329969e9718cdb071c6f0a586ced1d91b5c58413/consolekit-1.3.0-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-click@7.1.2:")
        depends_on("py-colorama@0.4.3:", when="@1.2: platform=windows ^python@:3.9")
        depends_on("py-colorama@0.4.3:", when="@0.7.1:1.1 ^python@:3.9")
        depends_on("py-colorama@0.4.3:", when="@0.3.1:0.7.0")
        depends_on("py-deprecation-alias@0.1.1:", when="@1.1:")
        depends_on("py-domdf-python-tools@3.8:", when="@1.6:")
        depends_on("py-domdf-python-tools@2.6:", when="@1.2.2:1.5")
        depends_on("py-mistletoe@0.7.2:", when="@0.8:")
        depends_on("py-typing-extensions@3.10:3.10.0.0,3.10.0.2:", when="@1.3.2:")
        depends_on("py-typing-extensions@3.7.4.3:", when="@0.3.1:1.3.1")
    # END DEPENDENCIES

