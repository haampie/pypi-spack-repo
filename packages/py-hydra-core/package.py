# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyHydraCore(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("1.3.2", sha256="fa0238a9e31df3373b35b0bfb672c34cc92718d21f81311d8996a16de1141d8b", url="https://pypi.org/packages/c6/50/e0edd38dcd63fb26a8547f13d28f7a008bc4a3fd4eb4ff030673f22ad41a/hydra_core-1.3.2-py3-none-any.whl")
    version("1.3.1", sha256="d1c8b273eba0be68218c4ff1ae9a7df7430ce4aa580f1bbebc03297029761cf4", url="https://pypi.org/packages/01/d1/d2e852afd72da2ca7f5ee1e71124ef61328282482b1cd8d96d37145bb947/hydra_core-1.3.1-py3-none-any.whl")
    version("1.3.0", sha256="47dac77149992ce3f4f36491f52d98e85f249b156410f4e1b99eea77a0a6674b", url="https://pypi.org/packages/a6/b1/777bdecfafa1883fe97e41e91edee0b543e447d7ad69d133ab4e18689a9f/hydra_core-1.3.0-py3-none-any.whl")
    version("1.2.0", sha256="b6614fd6d6a97a9499f7ddbef02c9dd38f2fec6a9bc83c10e248db1dae50a528", url="https://pypi.org/packages/68/0d/0da98325011cb09e1f6439f0adcc98a0f5261d3578bf182438562096913e/hydra_core-1.2.0-py3-none-any.whl")
    version("1.1.2", sha256="967fff142a44d635d85adf98881a34cb54d2ff6ff2133acc7a14fa87c57adf35", url="https://pypi.org/packages/d4/82/1b3e94a5e9ebbeb89e1dcc067f262f142e262a56fcb95ab34e186bd385e5/hydra_core-1.1.2-py3-none-any.whl")
    version("1.1.1", sha256="928b154d8105db4ee67d768e3cd0f74ca9373121fc99dee54488393b17a31929", url="https://pypi.org/packages/24/27/c8f0ccc24512fadfa53d30ea26a588c04de962e9670b3c28fe51595a9b7a/hydra_core-1.1.1-py3-none-any.whl")
    version("1.1.0", sha256="22370397633af05db594d69d885ead0728039feaec1bb4f666643f811dc6d183", url="https://pypi.org/packages/c3/cd/85aa2e3a8babc36feac99df785e54abf99afbc4acc20488630f3ef46980a/hydra_core-1.1.0-py3-none-any.whl")
    version("1.0.7", sha256="e800c6deb8309395508094851fa93bc13408f2285261eb97e626d37193b58a9f", url="https://pypi.org/packages/5f/2a/9c698daa12ed6e09e7629e6908528f043fa9de8a441c56cc13608d765fb2/hydra_core-1.0.7-py3-none-any.whl")
    version("1.0.6", sha256="500d4346b7afcd654276c87c15820d7e6b76c2da95ad698cceb4120d7a877b32", url="https://pypi.org/packages/52/e3/fbd70dd0d3ce4d1d75c22d56c0c9f895cfa7ed6587a9ffb821d6812d6a60/hydra_core-1.0.6-py3-none-any.whl")
    version("1.0.5", sha256="e0fdfe35bd2b899699482afaab7ee45ddd0c3a4e749e2983958a42d10bdcc343", url="https://pypi.org/packages/73/6e/6298e4099ecf7344fb6621e83ec92ba4384699397b2d9b2d17819f869a1d/hydra_core-1.0.5-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-antlr4-python3-runtime@4.9", when="@1.2:1.2.0.0,1.3:")
        depends_on("py-antlr4-python3-runtime@4.8", when="@1.0.0-rc2:1.1,1.2.0.dev:1.2")
        depends_on("py-importlib-resources@:5.2", when="@1.1.2:1.1 ^python@:3.8")
        depends_on("py-importlib-resources", when="@1.0.0-rc2:1.1.1,1.2: ^python@:3.8")
        depends_on("py-omegaconf@2.2:2.2.0.0,2.2.1:2.3", when="@1.3.1:")
        depends_on("py-omegaconf@2.2:2.2.0.0,2.2.1:", when="@1.2:1.2.0.0,1.3:1.3.0")
        depends_on("py-omegaconf@2.1", when="@1.1.0:1.1.0.0,1.1.1:1.1,1.2.0.dev:1.2.0.dev1,1.2.0.dev3")
        depends_on("py-omegaconf@2.0.5:2.0", when="@1.0.5:1.0")
        depends_on("py-packaging", when="@1.2:")
    # END DEPENDENCIES

