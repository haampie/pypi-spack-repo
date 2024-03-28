# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPymdownExtensions(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("10.7.1", sha256="f5cc7000d7ff0d1ce9395d216017fa4df3dde800afb1fb72d1c7d3fd35e710f4", url="https://pypi.org/packages/ff/4b/4ebb08f36e83e91b31117fe8f67844bac7f5c7d11ed151ae5db807be363f/pymdown_extensions-10.7.1-py3-none-any.whl")
    version("10.7", sha256="6ca215bc57bc12bf32b414887a68b810637d039124ed9b2e5bd3325cbb2c050c", url="https://pypi.org/packages/9f/08/d34528eaafe5521449aaedd897a0422b88ac311276384b162f6a65518008/pymdown_extensions-10.7-py3-none-any.whl")
    version("10.6", sha256="561eb3a5f3c3c2512952a4d6f5b311aa124b7147bd54a3ea0f36ce030c7e3dd9", url="https://pypi.org/packages/33/98/047bc685950df1e11de4b5cfbd854c18cfe45d385977b423fce8c4f78369/pymdown_extensions-10.6-py3-none-any.whl")
    version("10.5", sha256="1f0ca8bb5beff091315f793ee17683bc1390731f6ac4c5eb01e27464b80fe879", url="https://pypi.org/packages/4b/fb/7316b19d9a342b9b4bc953abd806dfc609d5d8e1b250b727e8f47551ecf7/pymdown_extensions-10.5-py3-none-any.whl")
    version("10.4", sha256="cfc28d6a09d19448bcbf8eee3ce098c7d17ff99f7bd3069db4819af181212037", url="https://pypi.org/packages/98/2d/2929de81618c7213176899dd6372d6ec9c8f24337841dd74634fb69864ae/pymdown_extensions-10.4-py3-none-any.whl")
    version("10.3.1", sha256="8cba67beb2a1318cdaf742d09dff7c0fc4cafcc290147ade0f8fb7b71522711a", url="https://pypi.org/packages/0e/f3/31b0d3472a65eabe2eeeb682d7ab142b6a29045d997bf1b73aabcf59a3e2/pymdown_extensions-10.3.1-py3-none-any.whl")
    version("10.3", sha256="77a82c621c58a83efc49a389159181d570e370fff9f810d3a4766a75fc678b66", url="https://pypi.org/packages/bf/15/aa3a1d1a6da955fabb16e1de5627d2e3c3a7067b891c7bf42bd1ae50cca0/pymdown_extensions-10.3-py3-none-any.whl")
    version("10.2.1", sha256="bded105eb8d93f88f2f821f00108cb70cef1269db6a40128c09c5f48bfc60ea4", url="https://pypi.org/packages/2f/5d/aaadfd7c9cc1a1a720c487fd28ecb18418728cd61dd3451e8a831e8030ea/pymdown_extensions-10.2.1-py3-none-any.whl")
    version("10.2", sha256="fbb86243db9a681602e3b869deef000211c55d0261015a5cc41d6f34d2afc57f", url="https://pypi.org/packages/33/df/239467d754ff74d993adb4759958fe97ef4dc60610ec6c8b08e86c1130c2/pymdown_extensions-10.2-py3-none-any.whl")
    version("10.1", sha256="ef25dbbae530e8f67575d222b75ff0649b1e841e22c2ae9a20bad9472c2207dc", url="https://pypi.org/packages/f5/55/740e1c6f1d3a598b6d2d3afc9691d154596f1b7a50f7a7288526b8818529/pymdown_extensions-10.1-py3-none-any.whl")
    version("9.5", sha256="ec141c0f4983755349f0c8710416348d1a13753976c028186ed14f190c8061c4", url="https://pypi.org/packages/f1/e0/1ed09f66cd1648f8e009120debf9b7d67596fb688e53e71522da1daa02a0/pymdown_extensions-9.5-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-markdown@3.5:", when="@10.5:")
        depends_on("py-markdown@3.2:", when="@7.0-rc1,7.1:10.4")
        depends_on("py-pyyaml", when="@9.10-alpha1:")
    # END DEPENDENCIES

