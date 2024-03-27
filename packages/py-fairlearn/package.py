##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyFairlearn(PythonPackage):
    version("0.10.0", sha256="772224097f8c073168bde44e659d7a2107f96d608063a738df9c985e17dab30f", url="https://pypi.org/packages/28/f2/bb5b2874498e023ebecc2e1b66d8c3d4cc5fd688837cbb9f4f79c323a8f0/fairlearn-0.10.0-py3-none-any.whl")
    version("0.9.0", sha256="08e75168a57274d4c8d24168fbb1e7c3f698f89ea542df12e0bf16886e289f8b", url="https://pypi.org/packages/b0/51/074c3e83d1254de673819e792326d74fc4b59cbc3820a02bc120b6edb854/fairlearn-0.9.0-py3-none-any.whl")
    version("0.8.0", sha256="f2dce40dd39b91252aacec229f0b71aa946344839604bfadc0a13fa4c9611111", url="https://pypi.org/packages/65/3b/2145139ec51519cd8c870cc47ecdfa64796ce68ad010cce27065e4af5c88/fairlearn-0.8.0-py3-none-any.whl")
    version("0.7.0", sha256="ac27e89952b5c5e3a3fdee05bfbadacfacc30fe00b917b057e2f605920ef5e44", url="https://pypi.org/packages/f9/22/93697472801e44344b5f7c3653762c4a143774f62b2a8bf97e7e7b1f7afa/fairlearn-0.7.0-py3-none-any.whl")
    version("0.6.2", sha256="bcf74911f4f73deb9d6dbce8d9638757b1e9670011f6bb4483d6e2a91b294130", url="https://pypi.org/packages/ea/a4/87a3ee19c036860a0b04dc5c9d51c86b0e147a379981f05fec0b34f8cdfc/fairlearn-0.6.2-py3-none-any.whl")
    version("0.6.1", sha256="7b4f8d7a6d2581e3a725656a32e536770d7244c3cd9c16ff0546055fd0881c95", url="https://pypi.org/packages/e7/03/6b4e8d1d1400eb2febeb49959720239cbebc94fa1578e03769941216e400/fairlearn-0.6.1-py3-none-any.whl")
    version("0.6.0", sha256="9f6bf09d99ec1be6663a1c48e09d8b58f52c4799507d80232e1e7c4763e9ecb8", url="https://pypi.org/packages/09/f2/354cd1ddb030e68dcced6f1932d9ef926ee13bad525faaf2f882e69705aa/fairlearn-0.6.0-py3-none-any.whl")
    version("0.5.0", sha256="474c59e0d1a5aadabb94462b123a1c97dd6b331cef8e2d2f12003d5c0b53b492", url="https://pypi.org/packages/3a/c6/64bdd611982cd2afef284f10022d1003b266ae7f86914418b8deda3ce2b2/fairlearn-0.5.0-py3-none-any.whl")
    version("0.4.6", sha256="03a794321a0e5d22996f0076e5530cd390407312b0fa16bc24a3d5164385fe78", url="https://pypi.org/packages/c0/ec/15764c20d27f4ec53e826eff160139c937274b646491c4de936a73444fd8/fairlearn-0.4.6-py3-none-any.whl")
    version("0.4.5", sha256="25fa075621fcece4158671e3080751b925133f28137f0a6b31f16c24c63c541e", url="https://pypi.org/packages/1b/c3/61e5f2df5dec4e20a69a746021b8e88844a340e9b02518591f5021cabaa2/fairlearn-0.4.5-py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-ipywidgets@7.5.0:", when="@0.4")
        depends_on("py-matplotlib@3.0.3:", when="@0.3:0.4.1")
        depends_on("py-numpy@1.24.4:", when="@0.10:")
        depends_on("py-numpy@1.18.0:", when="@0.9")
        depends_on("py-numpy@1.17.2:", when="@0.3:0.8")
        depends_on("py-pandas@2.0.3:", when="@0.10:")
        depends_on("py-pandas@0.25.2:", when="@0.9")
        depends_on("py-pandas@0.25.1:", when="@0.3:0.8")
        depends_on("py-scikit-learn@1.2.1:", when="@0.10:")
        depends_on("py-scikit-learn@0.22.1:", when="@0.4.5:0.9")
        depends_on("py-scipy@1.9.3:", when="@0.10:")
        depends_on("py-scipy@1.5.0:", when="@0.9")
        depends_on("py-scipy@1.4.1:", when="@0.5:0.8")
        depends_on("py-scipy@1.3.1:", when="@0.3:0.4")

