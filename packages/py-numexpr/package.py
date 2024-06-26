# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyNumexpr(PythonPackage):
    # BEGIN VERSIONS
    version("2.8.4", sha256="d5432537418d18691b9115d615d6daa17ee8275baef3edf1afbbf8bc69806147", url="https://pypi.org/packages/45/d0/0d5216512b59f139053f2d6c941598752ac8ad50eb3737e4accca08b3b50/numexpr-2.8.4.tar.gz")
    version("2.8.3", sha256="cb647c9d9c785dae0759bf6c875cde2bec472b5c3f7a6015734b161ae766d141", url="https://pypi.org/packages/b2/52/79f6b7db72b4cb847006d915801cc423c6b57e794c3802cfda648a4c6321/numexpr-2.8.3.tar.gz")
    version("2.7.3", sha256="43616529f9b7d1afc83386f943dc66c4da5e052f00217ba7e3ad8dd1b5f3a825", url="https://pypi.org/packages/17/91/688234440a7b45a4f6a9931d2541de5e9e48b2c54b8fcd5951ab14bd6a12/numexpr-2.7.3.tar.gz")
    version("2.7.2", sha256="4cf5082f3e4f256ba4033ba31d0b95cacc7619babd09d7b5fb56b3036c8923aa", url="https://pypi.org/packages/cf/e0/44e876061fcb05d085c35f6d572d258a44694f77e6f3c29f93e64e84700e/numexpr-2.7.2.tar.gz")
    version("2.7.0", sha256="37324b5981b8962102bdc8640c4f05f5589da5d1df2702418783085cb78ca217", url="https://pypi.org/packages/87/91/9e6305ec0f0560bf2c3730ad0b5ff3c8d6b48b442a830ff506bc6c829ac0/numexpr-2.7.0.tar.gz")
    version("2.6.9", sha256="fc218b777cdbb14fa8cff8f28175ee631bacabbdd41ca34e061325b6c44a6fa6", url="https://pypi.org/packages/82/a0/42e0f42d79e0db81e78424828dee1aea08a06da66c2bc06068742e9b860f/numexpr-2.6.9.tar.gz")
    version("2.6.5", sha256="f8ad8014085628eab91bc82fb9d10cf9ab8e04ede4884e4a1061445d395b36bb", url="https://pypi.org/packages/5e/04/9780a640cf173e36db72f8500e084990c67fff5576c6d72b228d19c02c23/numexpr-2.6.5.tar.gz")
    version("2.6.1", sha256="db2ee72f277b23c82d204189290ea4b792f9bd5b9d67744b045f8c2a8e929a06", url="https://pypi.org/packages/c6/f0/11628fa4d332d8fe9ab0ba8e9bfe0e065fb6b5324859171ee72d84e079c0/numexpr-2.6.1.tar.gz")
    version("2.5", sha256="319cdf4e402177a1c8ed4972cffd09f523446f186d347b7c1974787cdabf0294", url="https://pypi.org/packages/7b/a4/e4fb495692ba8b2a6798b2b93c2ee090c1addaf0f6c16395ef3bad72e0ce/numexpr-2.5.tar.gz")
    version("2.4.6", sha256="052397670dc56d7845ff894cd7d858e4f115491ecd93bcc0eda5cb83990c5da3", url="https://pypi.org/packages/5a/d5/14b87de25ea857a321e0729a2b2ec3a4a98a993801427938209380a3fc82/numexpr-2.4.6.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.7:", when="@2.8.2:2.8.6")
        depends_on("py-numpy@1.7:", when="@2.6.4:2.6.6.0,2.6.7,2.6.9:2.7.1")
    # END DEPENDENCIES

