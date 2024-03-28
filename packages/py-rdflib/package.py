# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyRdflib(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("7.0.0", sha256="0438920912a642c866a513de6fe8a0001bd86ef975057d6962c79ce4771687cd", url="https://pypi.org/packages/d4/b0/7b7d8b5b0d01f1a0b12cc2e5038a868ef3a15825731b8a0d776cf47566c0/rdflib-7.0.0-py3-none-any.whl")
    version("6.3.2", sha256="36b4e74a32aa1e4fa7b8719876fb192f19ecd45ff932ea5ebbd2e417a0247e63", url="https://pypi.org/packages/af/92/d7fb1d7fb70c9f7003fa50b7a3880ebcb311cc3f8552b3595e7c8f75aeeb/rdflib-6.3.2-py3-none-any.whl")
    version("6.3.1", sha256="b9a01b4ab94abb2d1a80e7c4968621ff8db5bdb664b018b0cd76822e7e33f066", url="https://pypi.org/packages/b3/8a/056eeca5b003e321510001600699868a5237a4635de1617832fcb33bd1c3/rdflib-6.3.1-py3-none-any.whl")
    version("6.3.0", sha256="9ee3f16c3c7c2da27c56ce5605f1bb9e07807d6c22cfec08d3abdcbac489bbb1", url="https://pypi.org/packages/ae/e1/3a0a3b79ac8c7f0416b0a47d7f49d3a5a07a2d3fcc8583e6178f1d5064a6/rdflib-6.3.0-py3-none-any.whl")
    version("6.2.0", sha256="85c34a86dfc517a41e5f2425a41a0aceacc23983462b32e68610b9fad1383bca", url="https://pypi.org/packages/50/fb/a0f8b6ab6598b49871a48a189dc1942fb0b0543ab4c84f689486233ef1ec/rdflib-6.2.0-py3-none-any.whl")
    version("6.1.1", sha256="fc81cef513cd552d471f2926141396b633207109d0154c8e77926222c70367fe", url="https://pypi.org/packages/95/7f/7729b74154047bde5a6ac39a0c4d689b98808521417571bf5e92e2d3c2c2/rdflib-6.1.1-py3-none-any.whl")
    version("6.1.0", sha256="31a65bcf8cb3c33d791ba5224fd65cdb681766a48bcdda1dbde85e013eab8e9c", url="https://pypi.org/packages/85/84/60b4678fafa04092ef1eed60fcc4c3c5ba5898f0c12d183d17fd1661ffa2/rdflib-6.1.0-py3-none-any.whl")
    version("6.0.2", sha256="b7642daac8cdad1ba157fecb236f5d1b2aa1de64e714dcee80d65e2b794d88a6", url="https://pypi.org/packages/34/77/2995c0d4b89607ce2c5e062995f7a26ed61a4d9e20cfc3711f5e8adeaa7e/rdflib-6.0.2-py3-none-any.whl")
    version("6.0.2-alpha0", sha256="d8df043507ed8345336fcd30b1d5735048e1f451080d88cfd3e03abc09eb2bab", url="https://pypi.org/packages/21/29/66f6c93d159d5861b4cda863f3e346120c611bf64e39bbc5f594f8b065e5/rdflib-6.0.2a0-py3-none-any.whl")
    version("6.0.1", sha256="a775069ab1c3d38b7e04666603666fb8a31937a4671a5afc91ca136109f8047a", url="https://pypi.org/packages/70/35/40166218caeb01914784b8b2e3e4225de5a83862055b1f8f8579323b1f80/rdflib-6.0.1-py3-none-any.whl")
    version("6.0.0", sha256="bb24f0058070d5843503e15b37c597bc3858d328d11acd9476efad3aa62f555d", url="https://pypi.org/packages/68/d4/f1bc834ca44120a5f81fc64570cc8ade33ebb8102622caa9f6ad50d13ada/rdflib-6.0.0-py3-none-any.whl")
    version("5.0.0", sha256="88208ea971a87886d60ae2b1a4b2cdc263527af0454c422118d43fe64b357877", url="https://pypi.org/packages/d0/6b/6454aa1db753c0f8bc265a5bd5c10b5721a4bb24160fb4faf758cf6be8a1/rdflib-5.0.0-py3-none-any.whl")
    version("5.0.0-rc1", sha256="d66a0346ab0e572e20746b67b071557b5ef6327a6f18596d2f4332f152c6a2e9", url="https://pypi.org/packages/9b/a9/49d72d650cf19c0b462dde7f1067fee8e3a04874f23e0ab54ddfb2f3d7d6/rdflib-5.0.0rc1-py3-none-any.whl")
    version("4.2.2", sha256="58d5994610105a457cff7fdfe3d683d87786c5028a45ae032982498a7e913d6f", url="https://pypi.org/packages/3c/fe/630bacb652680f6d481b9febbb3e2c3869194a1a5fc3401a4a41195a2f8f/rdflib-4.2.2-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.8.1:", when="@7:")
        depends_on("py-isodate@0.6:", when="@6.3:")
        depends_on("py-isodate", when="@4.2.2:6.2")
        depends_on("py-pyparsing@2.1:", when="@6.3:")
        depends_on("py-pyparsing", when="@4.2.2:6.2")
        depends_on("py-setuptools", when="@6:6.2")
        depends_on("py-six", when="@5")
    # END DEPENDENCIES

