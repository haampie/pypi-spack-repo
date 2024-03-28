# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyLightningUtilities(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.11.0", sha256="bf576a421027fdbaf48e80cbc2fdf900a3316a469748a953c33a8ca2b2718a20", url="https://pypi.org/packages/ca/7d/16afeaef22e9863a4ba1de55ffca3a85167d119ff6c6cc2373c4b1b3e253/lightning_utilities-0.11.0-py3-none-any.whl")
    version("0.10.1", sha256="e67be3f328b1c14f2b36cc09e84642db5b50afeab94e7704969b2130fe6a3bda", url="https://pypi.org/packages/7d/84/fce34a549e2f795b3a0427e7dd40719dd4f00036e50ba58198a5a706eb75/lightning_utilities-0.10.1-py3-none-any.whl")
    version("0.10.0", sha256="84d09b11fe9bc16c803ae5e412874748239d73ad2f3d1b90862f99ce15a03aa0", url="https://pypi.org/packages/5e/f4/07b748cb9834848de16aaeb1ae38bc9cfcfe3adc22ee2c8ebbe11db82795/lightning_utilities-0.10.0-py3-none-any.whl")
    version("0.9.0", sha256="918dd90c775719e3855631db6282ad75c14da4c5727c4cebdd1589d865fad03d", url="https://pypi.org/packages/46/ee/8641eeb6a062f383b7d6875604e1f3f83bd2c93a0b4dbcabd3150b32de6e/lightning_utilities-0.9.0-py3-none-any.whl")
    version("0.8.0", sha256="22aa107b51c8f50ccef54d08885eb370903eb04148cddb2891b9c65c59de2a6e", url="https://pypi.org/packages/5d/ec/a20c5d5f26894913da028110310ba55ee254e1b7ff0ff78441e4eeb7291f/lightning_utilities-0.8.0-py3-none-any.whl")
    version("0.7.1", sha256="a7c58e67831c17712736e38e8ad5b81dbf64184ce28684a502e896ecca939b67", url="https://pypi.org/packages/58/10/e5f7a23c836b63960e936a75f805ee3d92c647ee39850837187219c83a43/lightning_utilities-0.7.1-py3-none-any.whl")
    version("0.7.0", sha256="7f449504e432e80cef0775f2095a8a38f059b2f3e460499e74c71683930916f0", url="https://pypi.org/packages/e2/e6/069f3b5883e9e2ef582b2cded488de499631cc2383cb5c2ad66c6cfc22c9/lightning_utilities-0.7.0-py3-none-any.whl")
    version("0.6.0.post0", sha256="81edf3ce5ebd43389238afc1bca96ea0c6dcd3b4b442f8365c719dd3a82009dc", url="https://pypi.org/packages/52/9c/104b3c799cde4b23d2754409ba7c1f856f1406d74657287f53f6409f8231/lightning_utilities-0.6.0.post0-py3-none-any.whl")
    version("0.6.0", sha256="cf1df9fa6faa532591a91fac40149d6f7badb84ef83d746c019e67cca2d01c6c", url="https://pypi.org/packages/de/c4/d19bf68d5519d5141420d6906b40d0fa1f651e85bd4e23e097984bcaf792/lightning_utilities-0.6.0-py3-none-any.whl")
    version("0.5.0", sha256="db1fa4300ce76b171d8cd4e78ffad3b6bc82f3fbe8ca5aa35da269fbda65bea3", url="https://pypi.org/packages/f2/37/0c1e403717ad981f1ae407771a4e6f6be4407ed4f532b5c41703d5a33104/lightning_utilities-0.5.0-py3-none-any.whl")
    version("0.4.2", sha256="397fd573b406408e9d3d376b2b728dba44b0517dd487401a3117f96e434d0afc", url="https://pypi.org/packages/a0/66/14312d4b9318d9500146528d4ac4f313b19d94d90615e5599cce089967e2/lightning_utilities-0.4.2-py3-none-any.whl")
    version("0.4.1", sha256="880bbdff34ff7d3ca042b7d6ff0cc4bda1f9079a648752db654beefb6e754b03", url="https://pypi.org/packages/7e/ea/40e64439ad0869663c106de30cd4656254ad046a5871f1d45be326f5ed90/lightning_utilities-0.4.1-py3-none-any.whl")
    version("0.4.0", sha256="36d257f9eb9e1cb2669a43ca200d1dd4a0b4840768b38d9f69a892ff004cb412", url="https://pypi.org/packages/67/17/bed12398a0417be28970bb3f8252a36ae0b2bc0d580b0dcddf6ad5d89a62/lightning_utilities-0.4.0-py3-none-any.whl")
    version("0.3.0", sha256="1ae9bdd8f1be3c81b1ac4820f6eeddcbafcc2505c57a5940054466f4763bc22d", url="https://pypi.org/packages/8f/fc/1f4ff2bcba4e6162276cabe831a431ef14681a7158e693a5cf828dd6fa1b/lightning_utilities-0.3.0-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-fire", when="@0.2:0.3")
        depends_on("py-packaging@17.1:", when="@0.6.0.post:")
        depends_on("py-packaging@20:", when="@0.5:0.6.0.0")
        depends_on("py-setuptools", when="@0.10:")
        depends_on("py-typing-extensions", when="@0.5:")
    # END DEPENDENCIES

