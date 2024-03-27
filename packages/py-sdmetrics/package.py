##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PySdmetrics(PythonPackage):
    version("0.4.2", sha256="31ef0ae9966da60a1753da43dd0b5eee314b937c7ed53e51b8c35c496945a266", url="https://pypi.org/packages/cd/81/277d584fb4080e08a3b734016bd2d9fe79b24d3a5ed35bfcc445a5e0270f/sdmetrics-0.4.2-py2.py3-none-any.whl")
    version("0.4.2.dev0", sha256="4282751b4045208f2aa00e551364758f76bb68f7780d827b727d19239a34afba", url="https://pypi.org/packages/18/94/3881a61625fd13f69191c6554871c6f473e6cd408733531660cf0c395762/sdmetrics-0.4.2.dev0-py2.py3-none-any.whl")
    version("0.4.1", sha256="479ab86f466e69e12edf6d707a892479a939eb9e42ffb2b7dc6afdfddb998ee9", url="https://pypi.org/packages/f6/72/8f85dfbd06466ff64d03d4fddb2874c2c0d9ea1bba34f305ab4588135dfd/sdmetrics-0.4.1-py2.py3-none-any.whl")

    with default_args(type="run"):
        depends_on("python@:3.11", when="@0.11:")
        depends_on("python@:3.10", when="@0.9:0.10")
        depends_on("python@:3.9", when="@0.4:0.8")
        depends_on("python@:3.8", when="@0.0.2:0.3")
        depends_on("py-copulas@0.7:0.7.0.0,0.7.1:0.7", when="@0.4.2:0.8")
        depends_on("py-copulas@0.6:0.6.0.0,0.6.1:0.6", when="@0.4:0.4.1")
        depends_on("py-numpy@1.20.0:1", when="@0.9: ^python@:3.9")
        depends_on("py-numpy@1.20.0:1", when="@0.4:0.8")
        depends_on("py-pandas@1.1.3:1", when="@0.9 ^python@:3.9")
        depends_on("py-pandas@1.1.3:1", when="@0.4:0.8")
        depends_on("py-pyts@0.12", when="@0.4:0.5")
        depends_on("py-rdt@0.6.1:0.6.1.0,0.6.2:0", when="@0.4:0.5.0")
        depends_on("py-scikit-learn@0.24.0:", when="@0.13.1: ^python@:3.9")
        depends_on("py-scikit-learn@0.24.0:", when="@0.11:0.13.0 ^python@:3.10.0")
        depends_on("py-scikit-learn@0.24.0:", when="@0.3.3:0.10")
        depends_on("py-scipy@1.5.4:", when="@0.9: ^python@:3.9")
        depends_on("py-scipy@1.5.4:", when="@0.4:0.8")
        depends_on("py-torch@1.8:1", when="@0.4:0.7")

