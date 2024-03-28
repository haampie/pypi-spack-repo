# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyBuild(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("1.2.1", sha256="75e10f767a433d9a86e50d83f418e83efc18ede923ee5ff7df93b6cb0306c5d4", url="https://pypi.org/packages/e2/03/f3c8ba0a6b6e30d7d18c40faab90807c9bb5e9a1e3b2fe2008af624a9c97/build-1.2.1-py3-none-any.whl")
    version("1.2.0", sha256="6105465d9b233433ce8ffa151c760f674446ba766af0290fc14bfa32aef92a04", url="https://pypi.org/packages/26/c7/bb2bd66d9d60125e960891ac15f84f26c7c9a16e612fa1af109ba2a9a7ed/build-1.2.0-py3-none-any.whl")
    version("1.1.1", sha256="8ed0851ee76e6e38adce47e4bee3b51c771d86c64cf578d0c2245567ee200e73", url="https://pypi.org/packages/4f/81/4849059526d02fcc9708e19346dd740e8b9edd2f0675ea7c38302d6729df/build-1.1.1-py3-none-any.whl")
    version("1.1.0", sha256="05a32cbae3f42b03d1592029237914c136a880de83bc2a0fcd4f09e1336ee695", url="https://pypi.org/packages/06/d5/5ff223d89a6c461565ad06f5fdc089dcf7cc88283b9d8b84a11a80526927/build-1.1.0-py3-none-any.whl")
    version("1.0.3", sha256="589bf99a67df7c9cf07ec0ac0e5e2ea5d4b37ac63301c4986d1acb126aa83f8f", url="https://pypi.org/packages/93/dd/b464b728b866aaa62785a609e0dd8c72201d62c5f7c53e7c20f4dceb085f/build-1.0.3-py3-none-any.whl")
    version("1.0.0", sha256="f4c7b45e70e2c345e673902253d435a9a7729ff09ab574924420cf120c60bcc9", url="https://pypi.org/packages/75/59/2b0c77e78f754e4443126349e15a9f12716a34e9dcce8e8d61b1b6d553e7/build-1.0.0-py3-none-any.whl")
    version("0.10.0", sha256="af266720050a66c893a6096a2f410989eeac74ff9a68ba194b3f6473e8e26171", url="https://pypi.org/packages/58/91/17b00d5fac63d3dca605f1b8269ba3c65e98059e1fd99d00283e42a454f0/build-0.10.0-py3-none-any.whl")
    version("0.9.0", sha256="38a7a2b7a0bdc61a42a0a67509d88c71ecfc37b393baba770fae34e20929ff69", url="https://pypi.org/packages/03/97/f58c723ff036a8d8b4d3115377c0a37ed05c1f68dd9a0d66dab5e82c5c1c/build-0.9.0-py3-none-any.whl")
    version("0.8.0", sha256="19b0ed489f92ace6947698c3ca8436cb0556a66e2aa2d34cd70e2a5d27cd0437", url="https://pypi.org/packages/7a/24/ee8271da317b692fcb9d026ff7f344ac6c4ec661a97f0e2a11fa7992544a/build-0.8.0-py3-none-any.whl")
    version("0.7.0", sha256="21b7ebbd1b22499c4dac536abc7606696ea4d909fd755e00f09f3c0f2c05e3c8", url="https://pypi.org/packages/46/28/70768d6585162eb29df181aed4c1adb3081307ad46a892c390dab549dc13/build-0.7.0-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    variant("virtualenv", default=False)
    # END VARIANTS

    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-importlib-metadata@4.6:", when="@1.1: ^python@:3.10.1")
        depends_on("py-importlib-metadata@4.6:", when="@1:1.0 ^python@:3.9")
        depends_on("py-packaging@19.1:", when="@1.2:")
        depends_on("py-packaging@19:", when="@0.4:1.1")
        depends_on("py-pep517@0.9:", when="@0.4:0.9")
        depends_on("py-pyproject-hooks", when="@0.10:")
        depends_on("py-toml@0.10:", when="@0.4:0.5")
        depends_on("py-tomli@1.1:", when="@0.10: ^python@:3.10")
        depends_on("py-tomli@1:", when="@0.8:0.9 ^python@:3.10")
        depends_on("py-tomli@1:", when="@0.6:0.7")
        depends_on("py-virtualenv@20.0.35:", when="@0.2:+virtualenv")

        # marker: os_name == "nt"
        # depends_on("py-colorama", when="@0.4:")
    # END DEPENDENCIES

