# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyTrameVuetify(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("2.4.3", sha256="a3d05d714b78241d61fb5c76f65754e4b26afae67a3667a2daf47b399035f69c", url="https://pypi.org/packages/4d/3d/96d8f6259996d8ee71fcb6b32ad8d50012609617d70106d14b1f1329f21d/trame_vuetify-2.4.3-py3-none-any.whl")
    version("2.4.2", sha256="7723a620a604aed5c2d9c4d577a76d8dfc8b41ba8f1b49b8b2ba02ce45961a22", url="https://pypi.org/packages/97/02/62c09f76b4c464ddf7e68ba1d86163732c868b32ac2fdc812199d4afd153/trame_vuetify-2.4.2-py3-none-any.whl")
    version("2.4.1", sha256="7533e7be8238ca57c9c73b1fbb702c67491d6178da5325943f07cae3d9895e56", url="https://pypi.org/packages/9f/62/dc00b5181ddf62c1d0680ab778d18f632cb38e9375ee8bc46d2e7169ef0e/trame_vuetify-2.4.1-py3-none-any.whl")
    version("2.4.0", sha256="f3ccfa9e07499ab4181bc50c7efed46281bbb8093536a88f8e7b55a82b9ef17b", url="https://pypi.org/packages/61/72/83fbdef2c2f474a2413d7da989e626869fcabbf8bf4bc8eac1765911a048/trame_vuetify-2.4.0-py3-none-any.whl")
    version("2.3.1", sha256="455b179143f44e71719f9b8feeb36ec9aabf1d25e79c637a425c8cb153405335", url="https://pypi.org/packages/0a/ea/808b0245c197d91b206fa2e43268f0517ce20f002df72ad33bd5cd8c07f4/trame_vuetify-2.3.1-py3-none-any.whl")
    version("2.3.0", sha256="7317e241685c11cfd007dc2ef5e9caa2fb47087c53dc890cce562ab35c3222f4", url="https://pypi.org/packages/d1/fb/dd89c37f1ae1cab2db94195eb6103cd418dd1aa637dd765a68f11253e681/trame_vuetify-2.3.0-py3-none-any.whl")
    version("2.2.4", sha256="fede3b08db60f50e0f6ab36594c662c6cee010b7514376bfdfbece8a5c2ba9ee", url="https://pypi.org/packages/f2/dc/bc9bf1f7ea0efbd447fd459023fa497dbd9e800c8dfb8183fbe6e539c5aa/trame_vuetify-2.2.4-py3-none-any.whl")
    version("2.2.3", sha256="bce94b5b064462ce93d30144db3570d485b6671abf2aa4d9b1e5be9daf4ff6ce", url="https://pypi.org/packages/56/ac/c416c9dc4b9260baec4627d6d9e1cc8b5008aae0529d41c446a3e5b8f1e9/trame_vuetify-2.2.3-py3-none-any.whl")
    version("2.2.2", sha256="1bef4bf727b0036d7906a6b49fd3be2b63372a3e863b35a7d62c0ec11c441cfe", url="https://pypi.org/packages/b3/7c/cf25d5ed0a56ec5bbf4aea7bc11b701590a305337de23fb63830422f2523/trame_vuetify-2.2.2-py3-none-any.whl")
    version("2.2.1", sha256="93fe77966640753ad8bd4d3846a3583a767cfc70c936bd35918a578f1da05a59", url="https://pypi.org/packages/9a/8d/6c28b81414333548a47fde0d615253c39a487450c5c7443080a1cb0ff3ff/trame_vuetify-2.2.1-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-trame-client")
    # END DEPENDENCIES

