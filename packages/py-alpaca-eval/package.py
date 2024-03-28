# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyAlpacaEval(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.6", sha256="7b2c4804c0b07ce9d4564a175b2a734a54f2917c53929f78397dedb8b56d5b08", url="https://pypi.org/packages/82/d0/e249da2e02481e28f8ae203caa91907e413fe368b21e13d84b1e0833cbd7/alpaca_eval-0.6-py3-none-any.whl")
    version("0.5.4", sha256="a50d8b58585f90feee6aa266a09ed3cd84745d7bc9d3820a2af0ff951f5bef73", url="https://pypi.org/packages/b7/85/4319a4362221b12262bb92c2341ae7243237d35d99d19692d279b55bfb69/alpaca_eval-0.5.4-py3-none-any.whl")
    version("0.5.3", sha256="2cf7e538a75819e2ec2ac8a2865167323bff42010d2ff82ee8e26f8f7b19b145", url="https://pypi.org/packages/b7/c5/fd50a3126e6f0752c6ee6f406edc79585f5c6b68c76365c5d35aa32c675c/alpaca_eval-0.5.3-py3-none-any.whl")
    version("0.5.2", sha256="1cdfe37285ddd7c0f401dddd9b94710f2a50f11472e348cc7768929b204b91d5", url="https://pypi.org/packages/a2/89/d47f73736995134411200dceeb3f455260ecc07f0d34bee635bf587d0a12/alpaca_eval-0.5.2-py3-none-any.whl")
    version("0.5.1", sha256="778375c862b4b2c9e663e944ab36e3fde38cc630927e51635ccfdd8b0844c728", url="https://pypi.org/packages/e7/c7/67577cbf164d90c91cbd460f143387b428cec049065368693019c86d2412/alpaca_eval-0.5.1-py3-none-any.whl")
    version("0.5.0", sha256="edee0317707103fdf5acd5d3e44eff72f748e7b7646dbfae47547ae8e08d23ad", url="https://pypi.org/packages/43/91/d2d1f08c7ce6f627c66c5a6a5d47f501e702ebe540267e03151c34eac082/alpaca_eval-0.5.0-py3-none-any.whl")
    version("0.3.6", sha256="09fc412d84dfb1f7f5d1cc76a0e786c178230e06b856d8d53ce4dee729b960d7", url="https://pypi.org/packages/ee/2f/d7c91bc3c70f9020e6010ff414375e7b475c6f168574b94ec23650b95b7b/alpaca_eval-0.3.6-py3-none-any.whl")
    version("0.3.5", sha256="f182abb7ce80d18b747ccc9e55266cc12a2c60b4d67cd038c7daf3220e13bc33", url="https://pypi.org/packages/89/40/4e2ddabd9609db1bf884f950621b435af2754ed37304ebc566517ced9d86/alpaca_eval-0.3.5-py3-none-any.whl")
    version("0.3.4", sha256="d3735a30485f2a7c7ea3045e9fcfc3cad6793272a515b22462222091d72ce9eb", url="https://pypi.org/packages/80/59/b1bb1df315ed6d9a84a77a019db5b9edf5abb48d80bc16f6c9835b68186a/alpaca_eval-0.3.4-py3-none-any.whl")
    version("0.3.3", sha256="1f7a574bb38df8bed9e0bfb53ff7b2d1021e1c9c21fc527cd2d116e341900c19", url="https://pypi.org/packages/64/c0/ceb4e00db9f07badd18024dc4a911caa87b6feb19dfab50399a659ae5f1b/alpaca_eval-0.3.3-py3-none-any.whl")
    version("0.2.8", sha256="a83279fcccfb63b81a60a410b4165291a586b7efde8709ac5a1380917530ac4f", url="https://pypi.org/packages/c9/35/f7d6eb3909fd36ecbf927186a2c23cd257c45dc95dd1314dc2169a7aa9d9/alpaca_eval-0.2.8-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.10:", when="@0.1.3:")
        depends_on("python@3.9:", when="@:0.1.2")
        depends_on("py-datasets")
        depends_on("py-fire")
        depends_on("py-huggingface-hub", when="@0.5.4:")
        depends_on("py-openai@1.5:", when="@0.5.2:")
        depends_on("py-openai", when="@:0.5.1")
        depends_on("py-pandas")
        depends_on("py-patsy", when="@0.6:")
        depends_on("py-python-dotenv", when="@0.2.2:")
        depends_on("py-scikit-learn", when="@0.6:")
        depends_on("py-scipy", when="@0.5:")
        depends_on("py-tiktoken@0.3.2:")
    # END DEPENDENCIES

