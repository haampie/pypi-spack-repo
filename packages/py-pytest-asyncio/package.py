##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPytestAsyncio(PythonPackage):
    version("0.23.6", sha256="68516fdd1018ac57b846c9846b954f0393b26f094764a28c955eabb0536a4e8a", url="https://pypi.org/packages/e0/c9/de22c040d4c821c6c797ca1d720f1f4b2f4293d5757e811c62ae544496c4/pytest_asyncio-0.23.6-py3-none-any.whl")
    version("0.23.5.post1", sha256="30f54d27774e79ac409778889880242b0403d09cabd65b727ce90fe92dd5d80e", url="https://pypi.org/packages/16/a6/4b561db5e5ed2c928288b32d2c30265c4e6453bb172de926579c2bd979f6/pytest_asyncio-0.23.5.post1-py3-none-any.whl")
    version("0.23.5", sha256="4e7093259ba018d58ede7d5315131d21923a60f8a6e9ee266ce1589685c89eac", url="https://pypi.org/packages/ce/0c/a60bcaeb3ba2f938b4d76e535180ea9f43e8da5fa6933fd9401f6f6e46ae/pytest_asyncio-0.23.5-py3-none-any.whl")
    version("0.23.4", sha256="b0079dfac14b60cd1ce4691fbfb1748fe939db7d0234b5aba97197d10fbe0fef", url="https://pypi.org/packages/4d/a1/d7ca3b08a36e6b253666eed0cffbf9b9ab476fc66b05618e95db04d44490/pytest_asyncio-0.23.4-py3-none-any.whl")
    version("0.23.3", sha256="37a9d912e8338ee7b4a3e917381d1c95bfc8682048cb0fbc35baba316ec1faba", url="https://pypi.org/packages/1d/d6/568f370599c794cc97e2f36293e06ee9bd5bd3a2d2eb62525671425d266b/pytest_asyncio-0.23.3-py3-none-any.whl")
    version("0.23.2", sha256="ea9021364e32d58f0be43b91c6233fb8d2224ccef2398d6837559e587682808f", url="https://pypi.org/packages/4a/d4/47e991d09385ba7541e9bfdbbf49ff65d5e99400ef5590792021e5b21f40/pytest_asyncio-0.23.2-py3-none-any.whl")
    version("0.23.1", sha256="044ac9167e655f2462097e21cc9a29c9385674ea4fcc34677f1cc1ca35f3cd39", url="https://pypi.org/packages/96/e3/d80fe9f85b4ab6152c294e295ca20be5e2b637e476a8124528db53afb730/pytest_asyncio-0.23.1-py3-none-any.whl")
    version("0.23.0", sha256="91ef405536331eb9971511aeb08225869985d800cf491015f7407044e7d1d7f8", url="https://pypi.org/packages/54/65/a4bf83365294e6aba4936aef0e6d7b87cfc5846d448392a980a862104179/pytest_asyncio-0.23.0-py3-none-any.whl")
    version("0.22.0", sha256="c09905acb3b79827aace4c67fe15097daea1b363c00c8236875395414914bad3", url="https://pypi.org/packages/82/3f/d0a76a3596d5e8dd42051db3fc7b09bcf901d409dddfe1a601299b5baec8/pytest_asyncio-0.22.0-py3-none-any.whl")
    version("0.21.1", sha256="8666c1c8ac02631d7c51ba282e0c69a8a452b211ffedf2599099845da5c5c37b", url="https://pypi.org/packages/7d/2c/2e5ab8708667972ee31b88bb6fed680ed5ba92dfc2db28e07d0d68d8b3b1/pytest_asyncio-0.21.1-py3-none-any.whl")
    version("0.18.3", sha256="16cf40bdf2b4fb7fc8e4b82bd05ce3fbcd454cbf7b92afc445fe299dabb88213", url="https://pypi.org/packages/8b/d6/4ecdd0c5b49a2209131b6af78baa643cec35f213abbc54d0eb1542b3786d/pytest_asyncio-0.18.3-1-py3-none-any.whl")
    version("0.9.0", sha256="a962e8e1b6ec28648c8fe214edab4e16bacdb37b52df26eb9d63050af309b2a9", url="https://pypi.org/packages/33/7f/2ed9f460872ebcc62d30afad167673ca10df36ff56a6f6df2f1d3671adc8/pytest_asyncio-0.9.0-py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-pytest@7.0.0:7", when="@0.23.4-alpha0:0.23.4")
        depends_on("py-pytest@7.0.0:", when="@0.21:0.23.3,0.23.5-alpha0:")
        depends_on("py-pytest@6.1:", when="@0.17.1:0.20")
        depends_on("py-pytest@3.0.6:", when="@0.6:0.10")

