##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyTesttools(PythonPackage):
    version("2.7.1", sha256="56e118ce251544d436d9fbb5ba62f44aeb237aa8fcc3147372b484bbe5f48ef7", url="https://pypi.org/packages/5a/8a/ac002f3794e92a2820717b246719598a722e33970c7cc17413094a6bbdd7/testtools-2.7.1-py3-none-any.whl")
    version("2.7.0", sha256="068a20348482301bcee8ad6366021301469fc1c81ac3c80e8c038d711befa2c6", url="https://pypi.org/packages/7d/7e/071c1199f8023a186b02453ba2a09f339643ff0e4e842eb0c7ef169f09cf/testtools-2.7.0-py3-none-any.whl")
    version("2.6.0", sha256="cae7b2c2f459e448e0bb22c017fa1e7b4ba534b6e623d9f7ec0e0312aac8f7e8", url="https://pypi.org/packages/e6/26/1e2bf6d659ad0900fe8790dd757e594950af609ba29f017ac315cf84816c/testtools-2.6.0-py3-none-any.whl")
    version("2.5.0", sha256="798525999f053e4df4e352c0c198baeb9f5079f34bad5bd57a44e97a54fa0330", url="https://pypi.org/packages/c0/49/b2b4956528cca6954cb3a8016a8283282ccd1a1d66ab1c2d1bbde3f66946/testtools-2.5.0-py3-none-any.whl")
    version("2.4.0", sha256="64c974a6cca4385d05f4bbfa2deca1c39ce88ede31c3448bee86a7259a9a61c8", url="https://pypi.org/packages/11/9a/26b2f192024c4abcf702750ce7f4eb4cad305d8aad9482d9b5f3760118c7/testtools-2.4.0.tar.gz")
    version("2.3.0", sha256="5827ec6cf8233e0f29f51025addd713ca010061204fdea77484a2934690a0559", url="https://pypi.org/packages/e5/d4/9b22df94d0d5c83affe2517295c85fa2d9917f3cafa7dc7f6b1ce4135b00/testtools-2.3.0.tar.gz")
    version("2.2.0", sha256="80f606607a6e4ce4d0e24e5b786562aa42c581906f3c070607a4265f3da65810", url="https://pypi.org/packages/0d/72/3212c1723d49f5b58fca736dabdd2e74f38435076d943f4a642117f04d65/testtools-2.2.0.tar.gz")
    version("2.1.0", sha256="2734d641024f6eff9918a00028c42fc7aa4e36fda399be039ff5e8a3cd1f47ae", url="https://pypi.org/packages/d1/29/ab52c43fb751099bf364902f418a968cb251add1a0739b57e297e8cc1820/testtools-2.1.0.tar.gz")
    version("2.0.0", sha256="8237ab211cdeced2ff69e7b51c66ed8b1fd2aa0b338b1749609f9567646fad57", url="https://pypi.org/packages/67/28/d3ed649a0d6c629329d199e5c9fa323096f1ec111fa79345ec3f05f19a9c/testtools-2.0.0.tar.gz")
    version("1.9.0", sha256="b46eec2ad3da6e83d53f2b0eca9a8debb687b4f71343a074f83a16bbdb3c0644", url="https://pypi.org/packages/b2/b2/45737170548b4394e1fbec6dd16363d41bb1c67395962aefa0a044f95b57/testtools-1.9.0.tar.gz")

    with default_args(type="run"):
        depends_on("py-extras@1:", when="@2.5")
        depends_on("py-fixtures@2:", when="@2.6")
        depends_on("py-fixtures@1.3:", when="@2.5")
        depends_on("py-pbr@0.11:", when="@2.5:2.6")
        depends_on("py-setuptools", when="@2.7: ^python@3.12:")

