# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyChalice(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("1.31.0", sha256="f0680391f6bdc633869f91e14b1f0997bb0109152bdcbd7840033c41131ecb63", url="https://pypi.org/packages/8c/29/9e26ce0b6776d780408d43eeb47a272c2d6c5b4c8d3c2aa3366c29375101/chalice-1.31.0-py3-none-any.whl")
    version("1.30.0", sha256="a7cb5b44b35cfcd86a6d9abfeb5e1c06360adb9cba218787085e0a877f13938f", url="https://pypi.org/packages/6e/5a/c0788dd7e9e14d925263bee03f6f1bec1d3023f81cc7ae39ae0374a190a4/chalice-1.30.0-py3-none-any.whl")
    version("1.29.0", sha256="0375d93303a04c4885a05a76805370d604786acda59da80f16731312501e0114", url="https://pypi.org/packages/54/d9/fc8d0744740dd1db2490049ac3035002ec52cde7385d8d14416e829a3bc2/chalice-1.29.0-py3-none-any.whl")
    version("1.28.0", sha256="57ed833c72b75af0a276fd030daf240e0e31882a5e11a91547160c07f3dd29ab", url="https://pypi.org/packages/90/e0/c7c141129f67b97b2c062d5e09493dd82e1102a56b04a58fbebbc4939835/chalice-1.28.0-py3-none-any.whl")
    version("1.27.3", sha256="f41d0eaac1edb70ce1904b234bfc6ad4af35b7321f79b998bc6a95ff5f8cb4f6", url="https://pypi.org/packages/98/50/aff73e15a8e1c9357b6a5f581e4457f09c6c1dee3df043863944e6b6a49e/chalice-1.27.3-py3-none-any.whl")
    version("1.27.2", sha256="029d227d83b337bf067c15c30f9898422628d2e5fe724b8f4800baf2c6ff5ad1", url="https://pypi.org/packages/2f/3d/0d2e0a1e1379d40f67c9eb06b365b9e12122494c297dfdf88ac9a1016b5a/chalice-1.27.2-py3-none-any.whl")
    version("1.27.1", sha256="dd59c40711adfbdce0b61ce067d66111874246cc41b18c0cc6c5076432d60800", url="https://pypi.org/packages/c6/c0/b2f27eb6ab984d50d79a0e140dc123ff40caf3ecd8f0fd1a1bcfbc019309/chalice-1.27.1-py3-none-any.whl")
    version("1.27.0", sha256="73c38dc2c2ef41786939411dd17c024461b9abfe5c9cb1ec94fa4910cf7255c4", url="https://pypi.org/packages/90/05/cb147a644150dd7b4f88f79e2ced5560669fed54e06345f784918c16fed6/chalice-1.27.0-py3-none-any.whl")
    version("1.26.6", sha256="eeacdbe8979a13420870c3dd1647e2152727ccc8b6a58e53ddab4d1f93ff63c1", url="https://pypi.org/packages/7b/46/81b9be0fc0e1c823b5c617ee1be57ef834e26537e25d681679f752fb6898/chalice-1.26.6-py3-none-any.whl")
    version("1.26.5", sha256="6ae1bbb3dfcecbd8a1f43301ec1abe9ff0d2784f4e24da9590e2b534343af55b", url="https://pypi.org/packages/20/39/a56a963d4a96ec354ebc84a283eb48dfaf930eb6105dcdcfd1afe67e4142/chalice-1.26.5-py3-none-any.whl")
    version("1.20.0", sha256="607514b073dfc914ace44bd192ba96a227ec7c8ad7f147c147c23fa0f3dc6776", url="https://pypi.org/packages/1e/f5/9a18fe259700ea6635d18296c248142e207b1d84d0ae7bc631fbb678a856/chalice-1.20.0-py2.py3-none-any.whl")
    version("1.19.0", sha256="0229eb7749209f353e266aeddac344dfef1df6752a8e4307dfbfc5d5f98c3b66", url="https://pypi.org/packages/29/ed/b0a174eca4f26a1d5825774304db4bc7fc216e2305cab22e21b67d728015/chalice-1.19.0-py2.py3-none-any.whl")
    version("1.18.1", sha256="d18aeb83898f4d15bea822e07d862baad375b6507f9a7aa327399d163a5d328e", url="https://pypi.org/packages/eb/31/c36deff94d5acb3c5acf8654796f8fa40f5685b383c5d721f43c75510fd2/chalice-1.18.1-py2.py3-none-any.whl")
    version("1.18.0", sha256="a2787833bd8acaca66e18b67752921b3eac61efc7a38f8c047746aa35a3723bd", url="https://pypi.org/packages/50/5e/54e2fe7ce6bb797b44de1cf3963a32d10e3bdc763cf9492f41ed6dd087b1/chalice-1.18.0-py2.py3-none-any.whl")
    version("1.17.0", sha256="6b8200200ece65ee76857c46cfe033d678ffe66685eba00c44fdb38be571d647", url="https://pypi.org/packages/8c/64/a8bcd63117a4dfed256f9b88c430e2bade31349ef8def2fd972aab812327/chalice-1.17.0-py2.py3-none-any.whl")
    version("1.16.0", sha256="73dc0054421fad23bc4ad5e18eb08da220c71de60f1732df486dba085a5413ff", url="https://pypi.org/packages/5a/13/e2336421984c28392c864256c1b7f1faa0bdcb725b0fabd841512e667c3e/chalice-1.16.0-py2.py3-none-any.whl")
    version("1.15.1", sha256="9e4c000b8e8f6a5286fb0895904f2c82e1975bb60cd5df745807421c36820ce6", url="https://pypi.org/packages/6c/75/773e920859614bffcbbc9b3c6fedc99088e10fe8e4e992aca94335eeb9a7/chalice-1.15.1-py2.py3-none-any.whl")
    version("1.14.1", sha256="1602c8051341d09e01bd20de78d97c9324dc0606b53fc5c9fb96c2a1cf070331", url="https://pypi.org/packages/7d/71/3768159418fcd25ed3dc2a2116d14436caf2fac5b4f776ef1c61266b7c21/chalice-1.14.1-py2.py3-none-any.whl")
    version("1.14.0", sha256="889ee5e58a05037fc1582f556bc612e1683971db79d72d5aa8d961b39ef78bc6", url="https://pypi.org/packages/5b/97/07aef5b7f5944486c7bc104c59480ed478688c29a6d468f90da46017714b/chalice-1.14.0-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-attrs@19.3:21", when="@1.26.3:1.27")
        depends_on("py-attrs@19.3:19", when="@1.13:1.20.0")
        depends_on("py-botocore@1.14:", when="@1.23:")
        depends_on("py-botocore@1.12.86:", when="@1.8:1.22")
        depends_on("py-click@7:", when="@1.24.2:")
        depends_on("py-click@7", when="@1.17:1.24.1")
        depends_on("py-click@6.6:7", when="@1.11.1:1.16")
        depends_on("py-enum-compat@0.0.2:", when="@1.6:1.22.1")
        depends_on("py-inquirer@2.7:2", when="@1.22:")
        depends_on("py-jmespath@0.9.3:", when="@1.27:")
        depends_on("py-jmespath@0.9.3:0", when="@1.2:1.26")
        depends_on("py-mypy-extensions@0.4.3", when="@1.15:1.27.2")
        depends_on("py-pip@9:23", when="@1.30:")
        depends_on("py-pip@9:23.1", when="@1.29")
        depends_on("py-pip@9:23.0", when="@1.28")
        depends_on("py-pip@9:22.2", when="@1.27.2:1.27")
        depends_on("py-pip@9:22.1", when="@1.27.1")
        depends_on("py-pip@9:22.0", when="@1.26.6:1.27.0")
        depends_on("py-pip@9:21", when="@1.26.1:1.26.5")
        depends_on("py-pip@9:20.2", when="@1.17:1.21.4")
        depends_on("py-pip@9:20.1", when="@1.14.1:1.16")
        depends_on("py-pip@9:20.0", when="@1.13:1.14.0")
        depends_on("py-pyyaml@5.3.1:", when="@1.26.2:")
        depends_on("py-pyyaml@5.3.1:5", when="@1.15:1.26.1")
        depends_on("py-setuptools", when="@1.6.1:")
        depends_on("py-six@1.10:", when="@1.0.2:")
        depends_on("py-typing-extensions@4:", when="@1.27.3:1.30")
        depends_on("py-wheel", when="@1.6.1:")
    # END DEPENDENCIES

