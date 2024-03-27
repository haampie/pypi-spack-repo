##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyEccodes(PythonPackage):
    version("1.7.0", sha256="0f233009eac228b99be6e40e5f7cc175b477d322bd91c0dac6bf226f0222cb17", url="https://pypi.org/packages/d7/b1/445b5976010f31d5a78e14f9a7cf92fadd9d24c82553d9598078746262d3/eccodes-1.7.0.tar.gz")
    version("1.6.1", sha256="0d23e88cf9f3b4f5a2bee76f2b38080fd4b84386531d06d830831af3b1a18473", url="https://pypi.org/packages/be/80/9831e82aa58389dec9f4f8c7abde07a519aed779a13814e27483a18a3168/eccodes-1.6.1.tar.gz")
    version("1.6.0", sha256="59393040bcf89d8048127410926582aaffc688e174bebd464719307bbc5d9e15", url="https://pypi.org/packages/f5/4c/8a3c62a4f055b13d407b28d9073fef771127c2f80999380fd09464bdb836/eccodes-1.6.0.tar.gz")
    version("1.5.2", sha256="f7cce47fc9b1df3ed9eea21c4060fa572e07a4d0f014f6fd1f74683df9b45801", url="https://pypi.org/packages/af/b9/57d55d70ca6fbf9ce8dc096904d6bd4984d6eaacfff20c771245d99e1f1b/eccodes-1.5.2.tar.gz")
    version("1.5.1", sha256="e848911b0d4522c2cf60a11855c175e1e87fce44a143384cf38e4d60a0b62d9d", url="https://pypi.org/packages/6f/8d/8726710d4cfa0c0293d12920a39759c0592a782ea1b231623ad4c3b0c53a/eccodes-1.5.1.tar.gz")
    version("1.5.0", sha256="e70c8f159140c343c215fd608ddf533be652ff05ad2ff17243c7b66cf92127fa", url="https://pypi.org/packages/46/ba/8d0f9416328e428c710ab47a4d1c83ebde8f0ad1b81620ef19a327eebb4e/eccodes-1.5.0.tar.gz")
    version("1.4.2", sha256="63fa80a1d1b445904f486bc396a6a6605df029f4e215acc28ceb1a1ff5eb664f", url="https://pypi.org/packages/55/d1/511defc811c6ce7cbb0df79969b174fe97ccf7c305380f8842c1311cbbdb/eccodes-1.4.2.tar.gz")
    version("1.4.1", sha256="d5ef0642e3d51dedca7832d0fb44ad2b258d18a7d9fe3a2bb35755052d2383bc", url="https://pypi.org/packages/ab/c9/30a653478ae2dd67bd92c0e26990a103d7f5a813e29ae4ed0b164a033837/eccodes-1.4.1.tar.gz")
    version("1.4.0", sha256="b737b75c48aaaa5bd72de4c3efdec6ace15ad15ca41451d4885dcd7654357380", url="https://pypi.org/packages/26/a4/85feb994756be13f2d1d00afdda85aa81f80ed46970985d49b13599d323a/eccodes-1.4.0.tar.gz")
    version("1.3.3", sha256="60284cfc753a57239515a89bef8d65d78cb36fdd042214027d4ac71303f029b5", url="https://pypi.org/packages/65/e6/551f5f522f0c0c1316028114a180f03ee785759f2f77cd91518e5184c5df/eccodes-1.3.3.tar.gz")
    version("1.3.2", sha256="f282adfdc1bc658356163c9cef1857d4b2bae99399660d3d4fcb145a52d3b2a6", url="https://pypi.org/packages/79/1d/d5209cb0b5261e832f0b43c83ef3f47e05fd22f09310dc83f82347da082c/eccodes-1.3.2.tar.gz")

    with default_args(type="run"):
        depends_on("py-attrs", when="@:1.2,1.7:")
        depends_on("py-cffi", when="@:1.2,1.7:")
        depends_on("py-findlibs", when="@1.7:")
        depends_on("py-numpy", when="@:1.2,1.7:")

