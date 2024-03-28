# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyDomToml(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.6.1", sha256="ebdd69c571268dfa5a56b5085b5311583d8a8d2dc1811349e796160c9f36d501", url="https://pypi.org/packages/d2/9d/1c36fc21dd9c1cfa21d74ca090074adfa1e2e778f79aa3d203bacdabbb35/dom_toml-0.6.1-py3-none-any.whl")
    version("0.6.0", sha256="6e40b3d4a88db2ef5fe6b433238ca00f4f6ffe34a6de16a9f015cf9122898b20", url="https://pypi.org/packages/c0/2a/474e480ef216872be48adf41a917eac492397d7b40fd742b4cd5779ec9e8/dom_toml-0.6.0-py3-none-any.whl")
    version("0.5.1.post1", sha256="492293ded75d864365ac15f10d3796c1b3b2e3bb26e949e19f16781089f8a75f", url="https://pypi.org/packages/24/43/c7bddda32fcf66d3bd1cb6396dcd04a42f81369b952d0827fd44a873ea04/dom_toml-0.5.1.post1-py3-none-any.whl")
    version("0.5.1", sha256="6e5802c6ddee64379664b3f165b84b2739c81574f307ba7fffdbbc957b59155e", url="https://pypi.org/packages/7a/d9/ef26cd8a57ef53ba7eb6cc9a6aa18ae30280184ff1cf95f018617ec5c9e7/dom_toml-0.5.1-py3-none-any.whl")
    version("0.5.0", sha256="a5063ce7b0880952968fa8eadbc1b742314b78ee5b5282a41294f860fe07d857", url="https://pypi.org/packages/ec/c1/b321db9b576ad9f7cefc9945ce6eabaaf440133e3775d6cfba59dcef1d57/dom_toml-0.5.0-py3-none-any.whl")
    version("0.4.0", sha256="96610857dea48ffc2793f7aeb8022a26a3a07dc94a4bf48384efbce9a7a084b5", url="https://pypi.org/packages/d8/35/debec7cf09f52ff4a1adaba901fb15987978fc8713507c2bfdf2c7d58baf/dom_toml-0.4.0-py3-none-any.whl")
    version("0.3.1", sha256="55b353b658db8dfe0bc98c0b37dc85b2b75c293b8692fdefcc9c5ee9cd4997e1", url="https://pypi.org/packages/39/aa/15c4a641ca8fee91775c8b842ceeefe5460f514a8378e31be640b146e02c/dom_toml-0.3.1-py3-none-any.whl")
    version("0.3.0", sha256="8a52f9f9da1bed90339fa9c06488792eecc340c097f6786734649a45329930e7", url="https://pypi.org/packages/10/fb/7d2146a5ed2c9aa1d8b759b03bccdad4c2add64e5cfa11a60fab91d4b4a2/dom_toml-0.3.0-py3-none-any.whl")
    version("0.2.2", sha256="aa3a506132cf2bac4de487b60397f5f128c79e9c7caa181d29b4daaff46c35e4", url="https://pypi.org/packages/2f/53/ff8f6f03246373943a60301554fea17fc4cd5c6770a41a9d4c9b8807e793/dom_toml-0.2.2-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-domdf-python-tools@2.8:", when="@0.5.1:")
        depends_on("py-domdf-python-tools@2.7:", when="@:0.5.0")
        depends_on("py-toml@0.10.2:")
    # END DEPENDENCIES

