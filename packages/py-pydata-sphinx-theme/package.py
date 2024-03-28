# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPydataSphinxTheme(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.15.2", sha256="0c5fa1fa98a9b26dae590666ff576f27e26c7ba708fee754ecb9e07359ed4588", url="https://pypi.org/packages/bc/ef/1700096a5c1d17c2d99332b0759c7ca70346aac917ceafa4c380f085d359/pydata_sphinx_theme-0.15.2-py3-none-any.whl")
    version("0.15.1", sha256="064efbe96137bd0acab80413759f1db38a42b51e2429b159af75c43a7590320b", url="https://pypi.org/packages/ee/d1/4d35f8cf0b065d25f99b5d7a9bc0349c1993538f4f8bbb04477d0e8d4051/pydata_sphinx_theme-0.15.1-py3-none-any.whl")
    version("0.15.0-rc0", sha256="3ab452c7fc85d78889b88bff854a54aa059f0995140b1b80aeec131398ac1732", url="https://pypi.org/packages/65/ee/7c1553663ee739b7212cae1e035d02e54d8dd671e9a84e0c056d1dbb6f79/pydata_sphinx_theme-0.15.0rc0-py3-none-any.whl")
    version("0.14.4", sha256="ac15201f4c2e2e7042b0cad8b30251433c1f92be762ddcefdb4ae68811d918d9", url="https://pypi.org/packages/1b/bf/3f8dc653e3015fa0656587e101013754d9bf926f395cbe0892f7e87158dd/pydata_sphinx_theme-0.14.4-py3-none-any.whl")
    version("0.14.3", sha256="b7e40cd75a20449adfe2d7525be379b9fe92f6d31e5233e449fa34ddcd4398d9", url="https://pypi.org/packages/4b/a1/3434ce0450af1007a396ae16fb61d2a465958c4704682bad20120ee1141b/pydata_sphinx_theme-0.14.3-py3-none-any.whl")
    version("0.14.2", sha256="098184c932c37106737e18b1527b741a53e19327ec04b5cbc564259a5eb27650", url="https://pypi.org/packages/4d/6f/a0a9f6d644ea8ef78f0771f3dd8a8cafe975d0025f9166e3859470b367e7/pydata_sphinx_theme-0.14.2-py3-none-any.whl")
    version("0.14.1", sha256="c436027bc76ae023df4e70517e3baf90cdda5a88ee46b818b5ef0cc3884aba04", url="https://pypi.org/packages/81/0d/87e4ca68a348a62a15008ddfb24fc6bb54e060dcc061b87bbf0f801f574a/pydata_sphinx_theme-0.14.1-py3-none-any.whl")
    version("0.14.0", sha256="bdf7d275914e7675628ca2bf6eb3a21d0efa0e6b99a3a5421832594076754c33", url="https://pypi.org/packages/fe/17/cdca09b4dd6e85e59567b4bc581c6ca6e454075dd344b8f28d18cc5501fe/pydata_sphinx_theme-0.14.0-py3-none-any.whl")
    version("0.13.3", sha256="bf41ca6c1c6216e929e28834e404bfc90e080b51915bbe7563b5e6fda70354f0", url="https://pypi.org/packages/d2/61/1802ddf553af5850c2c3b6c183c6a3bdfc1145cec9873b56cac107291036/pydata_sphinx_theme-0.13.3-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.9:", when="@0.15:")
        depends_on("py-accessible-pygments", when="@0.13:")
        depends_on("py-babel", when="@0.13.0-rc5:")
        depends_on("py-beautifulsoup4", when="@0.5:")
        depends_on("py-docutils@:0.17-beta1,0.17.1-beta1:", when="@0.7:")
        depends_on("py-packaging", when="@0.8.1:")
        depends_on("py-pygments@2.7:", when="@0.10:")
        depends_on("py-sphinx@5.0.0:", when="@0.14:")
        depends_on("py-sphinx@4.2:", when="@0.11.0-rc3:0.13")
        depends_on("py-typing-extensions", when="@0.13.3:")
    # END DEPENDENCIES

