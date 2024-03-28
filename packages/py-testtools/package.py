# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyTesttools(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("2.7.1", sha256="56e118ce251544d436d9fbb5ba62f44aeb237aa8fcc3147372b484bbe5f48ef7", url="https://pypi.org/packages/5a/8a/ac002f3794e92a2820717b246719598a722e33970c7cc17413094a6bbdd7/testtools-2.7.1-py3-none-any.whl")
    version("2.7.0", sha256="068a20348482301bcee8ad6366021301469fc1c81ac3c80e8c038d711befa2c6", url="https://pypi.org/packages/7d/7e/071c1199f8023a186b02453ba2a09f339643ff0e4e842eb0c7ef169f09cf/testtools-2.7.0-py3-none-any.whl")
    version("2.6.0", sha256="cae7b2c2f459e448e0bb22c017fa1e7b4ba534b6e623d9f7ec0e0312aac8f7e8", url="https://pypi.org/packages/e6/26/1e2bf6d659ad0900fe8790dd757e594950af609ba29f017ac315cf84816c/testtools-2.6.0-py3-none-any.whl")
    version("2.5.0", sha256="798525999f053e4df4e352c0c198baeb9f5079f34bad5bd57a44e97a54fa0330", url="https://pypi.org/packages/c0/49/b2b4956528cca6954cb3a8016a8283282ccd1a1d66ab1c2d1bbde3f66946/testtools-2.5.0-py3-none-any.whl")
    version("2.4.0", sha256="36ff4998177c7d32ffe5fed3d541cb9ee62618a3b8e745c55510698997774ba4", url="https://pypi.org/packages/1a/d5/d0e0d16478fd4700694673518842be3c159fa08230e377f5f8570c170bbd/testtools-2.4.0-py2.py3-none-any.whl")
    version("2.3.0", sha256="a2be448869171b6e0f26d9544088b8b98439ec180ce272040236d570a40bcbed", url="https://pypi.org/packages/87/74/a4d55da28d7bba6d6f49430f22a62afd8472cb24a63fa61daef80d3e821b/testtools-2.3.0-py2.py3-none-any.whl")
    version("2.2.0", sha256="9b21a293cd33853956b1d3834c294d77a6ad0ab0eb1c077f858be433f0f225bb", url="https://pypi.org/packages/95/7f/24c35c97c50e91595e3d47861be016544dafdf65a2cad9379c786ac2709e/testtools-2.2.0-py2.py3-none-any.whl")
    version("2.1.0", sha256="2f05d4f68980c0f199942e13f82977f344082bd5545e222f7ccbf706a61f75e9", url="https://pypi.org/packages/73/c9/a43fda45060107ac8147980ce654b9324c28919cf1eef57df1697096bd19/testtools-2.1.0-py2.py3-none-any.whl")
    version("2.0.0", sha256="10bc0c7a23aca87f23ef5fd40cb4a8a53a0993ebdb98032de776e6274cc413db", url="https://pypi.org/packages/b8/31/95f9e5d0c5fb4eac3337f917a36854e26fd175c610964c8ea9b2c4b2c11d/testtools-2.0.0-py2.py3-none-any.whl")
    version("1.9.0", sha256="c2d878b6a15ccd8c5cf9a04bd32dcd0557fb6ab948da8828750165f9956af777", url="https://pypi.org/packages/ac/67/811419b9dee65f657d81e9b7c510951b3ebb02f3300330ec3f1bdb74fcc7/testtools-1.9.0-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-extras@1:", when="@2.5")
        depends_on("py-fixtures@2:", when="@2.6")
        depends_on("py-fixtures@1.3:", when="@2.5")
        depends_on("py-pbr@0.11:", when="@2.5:2.6")
        depends_on("py-setuptools", when="@2.7: ^python@3.12:")
    # END DEPENDENCIES

