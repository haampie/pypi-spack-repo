##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyCopulas(PythonPackage):
    version("0.7.1.dev0", sha256="42eac1ff6f0b87a8b257ac5eeb9248b63ffe0441b279b93e5a01b796fb1a0b49", url="https://pypi.org/packages/95/36/bb59d0f63930cdb9569545228545db2052a109ce35dc7552380d0532e043/copulas-0.7.1.dev0-py2.py3-none-any.whl")
    version("0.7.0", sha256="5f4c2419615882d589142916b56f837aa5b263ece6abd2acbbce95112e77ae40", url="https://pypi.org/packages/a3/ca/501dc64e7d260ce8457c78cb63d6de8deee98e6262096728ba0dab9d3287/copulas-0.7.0-py2.py3-none-any.whl")
    version("0.6.1", sha256="9db6686acb5101d1d615f6530ff59b094a8e7f053c9e073c64800a0be240e667", url="https://pypi.org/packages/03/8b/ec87edb5436a1b6a950c93732659209b7967b60189da69655d870930be13/copulas-0.6.1-py2.py3-none-any.whl")
    version("0.6.1.dev0", sha256="f6a8f329bac93279563d7329c1830e4487fefa418f24ee865d83acd061ad8102", url="https://pypi.org/packages/e5/61/28d082289ce442d825e90c6762d99db5078f4c764233f3dc575ad520a996/copulas-0.6.1.dev0-py2.py3-none-any.whl")
    version("0.6.0", sha256="556543df162dbd316aea5bffb0c17ed2c34f5b642abb52618a8e818260542872", url="https://pypi.org/packages/62/2a/9f801a73a61dedab6c34b9444b1710bc464f4ada8e85756de3599ad2cb51/copulas-0.6.0-py2.py3-none-any.whl")

    with default_args(type="run"):
        depends_on("python@:3.11", when="@0.7.1:")
        depends_on("python@:3.9", when="@0.5.2.dev1:0.7.0")
        depends_on("python@:3.8", when="@0.3.2:0.5.2.dev0")
        depends_on("py-boto3@1.7.47:1.9", when="@0.2.3:0.3.0")
        depends_on("py-docutils@0.10:0.14", when="@0.2.3:0.3.0")
        depends_on("py-matplotlib@3.6.0:", when="@0.7.1:0.9 ^python@3.10:")
        depends_on("py-matplotlib@3.4.0:", when="@0.7.1:0.9 ^python@:3.9")
        depends_on("py-matplotlib@3.4.0:", when="@0.6.1:0.7.0")
        depends_on("py-matplotlib@3.2.0:", when="@0.5:0.6.0")
        depends_on("py-numpy@1.23.3:1", when="@0.7.1: ^python@3.10:")
        depends_on("py-numpy@1.20.0:1", when="@0.7.1: ^python@:3.9")
        depends_on("py-numpy@1.20.0:1", when="@0.5.2.dev1:0.7.0")
        depends_on("py-pandas@1.5.0:1", when="@0.8:0.8.0 ^python@3.11:")
        depends_on("py-pandas@1.1.3:1", when="@0.7.1:0.8.0 ^python@:3.9")
        depends_on("py-pandas@1.5.0:1", when="@0.7.1:0.7 ^python@3.10:")
        depends_on("py-pandas@1.1.3:1", when="@0.5.2.dev1:0.7.0")
        depends_on("py-scipy@1.9.2:", when="@0.7.1: ^python@3.10:")
        depends_on("py-scipy@1.5.4:", when="@0.7.1: ^python@:3.9")
        depends_on("py-scipy@1.5.4:", when="@0.5.2.dev1:0.7.0")

