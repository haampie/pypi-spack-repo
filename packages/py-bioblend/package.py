##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyBioblend(PythonPackage):
    version("1.2.0", sha256="14d2d932ddabba47b88a0e030a0972a1287a1a051a9e555c1966964ef0a15cd5", url="https://pypi.org/packages/9c/2a/ba19ec668afe51b44072b6a5dbb2a2ea09cd25cb79add92ee0b8cb3dd9a2/bioblend-1.2.0-py2.py3-none-any.whl")
    version("1.1.1", sha256="bad2c1eebfeef4fb83e92af91de5de9e1d9098a006d8dd6112d453a9dcdd0a0c", url="https://pypi.org/packages/18/99/e77ea37ab78d0e4e48193892fb9360b93bb43aad29305354e1315c020c89/bioblend-1.1.1-py2.py3-none-any.whl")
    version("1.0.1", sha256="74626486efae2b4fd737c21f18a6868b2618d26ae91f87c735f3cb81fc25f649", url="https://pypi.org/packages/c5/b6/fcb0439af30cf0fd488b64f84a6ab2921ca220cd34f3178cec8e3f6a8ec6/bioblend-1.0.1-py2.py3-none-any.whl")
    version("1.0.0", sha256="db9616a77c614f3de900796079e9db72af739809232702d5ea4acf5ef49b4d38", url="https://pypi.org/packages/97/cb/eb052cb733e6422599786f56f5f6bf2a055e7041a522ec3541beb9ee4518/bioblend-1.0.0-py2.py3-none-any.whl")
    version("0.18.0", sha256="0cfbe8f11b0c3813a3822a9640931ae62ea14bea31e21591bca1310b25e745b3", url="https://pypi.org/packages/ee/ee/0e15ff7b6a0514c09ab5558ebdb72ac88cf2b690bc3a93dc98060b70740e/bioblend-0.18.0-py2.py3-none-any.whl")
    version("0.17.0", sha256="0bcff2987f849cc243779640c34b084518216df529adfcd2022348769aec2bb6", url="https://pypi.org/packages/bc/bc/be8be28ba0e61610e8da8d067b4d8c9e82e0b093405e57ea5657004d8eb7/bioblend-0.17.0-py2.py3-none-any.whl")
    version("0.16.0", sha256="057450d39054cf91fff31e9025f269eb08e1ef1b437d71dfc73957e7cb0d8195", url="https://pypi.org/packages/cc/28/7b3f9a4e77a9e13e7e0ff932c6363201ff91b31ca125e5f5a82727b79d59/bioblend-0.16.0-py2.py3-none-any.whl")
    version("0.15.0", sha256="a362a251a9429f17713bda51b29ccd3f4616a7613eedeb23e828307afb93eb34", url="https://pypi.org/packages/a2/93/dd391a268dc1a819750867e5b29723fe350aa259ebc675268b4536755614/bioblend-0.15.0-py2.py3-none-any.whl")
    version("0.14.0", sha256="b63505ddbecdebcc30406bc3186247d7d205ec6ba0fa4bfd220518c96ff92dd7", url="https://pypi.org/packages/d8/64/d1c3ab0ae9ec3c4e927cbe87620e0cb233d8cbd5e62e3f67a3a0a099648e/bioblend-0.14.0-py2.py3-none-any.whl")
    version("0.13.0", sha256="bcdb9f0dea1683bc61be8c4fd129ba8538b62f0499e6a07f86839cbc485944a4", url="https://pypi.org/packages/31/fb/5a6541f0e3faeddf31d3106bca85416a1e611c7f358b3a7c0b70a92a9b6a/bioblend-0.13.0-py2.py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-boto@2.9.7:", when="@0.9:0")
        depends_on("py-pyyaml", when="@0.9:0")
        depends_on("py-requests@2.20:", when="@0.12:")
        depends_on("py-requests-toolbelt@0.5.1:0.8,0.9.1:", when="@0.13:")
        depends_on("py-six", when="@0.9:0.13")
        depends_on("py-tuspy", when="@0.18:")
        depends_on("py-typing-extensions", when="@1:")

