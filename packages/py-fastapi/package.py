##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyFastapi(PythonPackage):
    version("0.110.0", sha256="87a1f6fb632a218222c5984be540055346a8f5d8a68e8f6fb647b1dc9934de4b", url="https://pypi.org/packages/f0/f7/ea860cb8aa18e326f411e32ab537424690a53db20de6bad73d70da611fae/fastapi-0.110.0-py3-none-any.whl")
    version("0.109.2", sha256="2c9bab24667293b501cad8dd388c05240c850b58ec5876ee3283c47d6e1e3a4d", url="https://pypi.org/packages/bf/97/60351307ab4502908d29f64f2801a36709a3f1888447bb328bc373d6ca0e/fastapi-0.109.2-py3-none-any.whl")
    version("0.109.1", sha256="510042044906b17b6d9149135d90886ade170bf615efcfb5533f568ae6d88534", url="https://pypi.org/packages/e3/cb/fa5122eec49e6bca91d3a332a3bc1dff3c12d093228e9e524cad3a7f1039/fastapi-0.109.1-py3-none-any.whl")
    version("0.109.0", sha256="8c77515984cd8e8cfeb58364f8cc7a28f0692088475e2614f7bf03275eba9093", url="https://pypi.org/packages/e5/80/ddbf524c6169072ab5e8dd4e106d4eb482bf920da1996dde9f308f90aa8c/fastapi-0.109.0-py3-none-any.whl")
    version("0.108.0", sha256="8c7bc6d315da963ee4cdb605557827071a9a7f95aeb8fcdd3bde48cdc8764dd7", url="https://pypi.org/packages/d4/e0/d5d6482e992a1892f3a9a62f6a9154944ae5b276e7da1cf92faa02e3a107/fastapi-0.108.0-py3-none-any.whl")
    version("0.107.0", sha256="90a50056a958f75bdcd8c1638df342192705c293b03d74856755a17b3c40bed9", url="https://pypi.org/packages/b7/9b/55a67813ff05c6173754a9115d0e1869628770af1f06a70a795ecc155498/fastapi-0.107.0-py3-none-any.whl")
    version("0.106.0", sha256="193c2f1b495d1d6561a3dc1ca02a150757322247d895ff6bf15b6eefee24feb9", url="https://pypi.org/packages/05/e4/f57e0eb823ead5bdf80e00d484e86925b2d2d2df53428ddf85c3b0e0e718/fastapi-0.106.0-py3-none-any.whl")
    version("0.105.0", sha256="f19ebf6fdc82a3281d10f2cb4774bdfa90238e3b40af3525a0c09fd08ad1c480", url="https://pypi.org/packages/ad/b9/b7ea33663daffa9db94119ea2a3df8f97bdca297024145fe79a5a13d37af/fastapi-0.105.0-py3-none-any.whl")
    version("0.104.1", sha256="752dc31160cdbd0436bb93bad51560b57e525cbb1d4bbf6f4904ceee75548241", url="https://pypi.org/packages/f3/4f/0ce34195b63240b6693086496c9bab4ef23999112184399a3e88854c7674/fastapi-0.104.1-py3-none-any.whl")
    version("0.104.0", sha256="456482c1178fb7beb2814b88e1885bc49f9a81f079665016feffe3e1c6a7663e", url="https://pypi.org/packages/db/30/b8d323119c37e15b7fa639e65e0eb7d81eb675ba166ac83e695aad3bd321/fastapi-0.104.0-py3-none-any.whl")
    version("0.98.0", sha256="f4165fb1fe3610c52cb1b8282c1480de9c34bc270f56a965aa93a884c350d605", url="https://pypi.org/packages/50/2c/6b94f191519dcc8190e78aff7bcb12c58329d1ab4c8aa11f2def9c214599/fastapi-0.98.0-py3-none-any.whl")
    version("0.88.0", sha256="263b718bb384422fe3d042ffc9a0c8dece5e034ab6586ff034f6b4b1667c3eee", url="https://pypi.org/packages/d8/09/ce090f6d53ce8b6335954488087210fa1e054c4a65f74d5f76aed254c159/fastapi-0.88.0-py3-none-any.whl")
    version("0.87.0", sha256="254453a2e22f64e2a1b4e1d8baf67d239e55b6c8165c079d25746a5220c81bb4", url="https://pypi.org/packages/8c/f5/68a7a099ae3674e85e2de11d3859ebffd7fe32a8cda0d11bd4d43f32437b/fastapi-0.87.0-py3-none-any.whl")
    version("0.86.0", sha256="1020d7ca205d8b95813881fb3282e9c3656e47993531af3aa4ae11065b61dd2c", url="https://pypi.org/packages/7b/d6/aa8078112b5bd15b716bb431b25f00e5befc23a05cb3fa66ca4e425b6682/fastapi-0.86.0-py3-none-any.whl")
    version("0.85.2", sha256="6292db0edd4a11f0d938d6033ccec5f706e9d476958bf33b119e8ddb4e524bde", url="https://pypi.org/packages/99/d4/4256804791b1e822f46bf79015270e9e9f14e9b634cb8231a88f6dc100c3/fastapi-0.85.2-py3-none-any.whl")
    version("0.85.1", sha256="de3166b6b1163dc22da4dc4ebdc3192fcbac7700dd1870a1afa44de636a636b5", url="https://pypi.org/packages/bf/54/6eb1882b5cb29e6647df92ee74d0a93dab149234ec914563cab955fa667f/fastapi-0.85.1-py3-none-any.whl")
    version("0.85.0", sha256="1803d962f169dc9f8dde54a64b22eb16f6d81573f54401971f90f0a67234a8b4", url="https://pypi.org/packages/f8/f6/5334a17a8acb95b2b71825db6c8c3d2b984d1d0c31266fcda02480ab62ab/fastapi-0.85.0-py3-none-any.whl")
    version("0.84.0", sha256="91e0bf9bc34c20a493ea18378d052b544570d27777fb6af0fb4f26c56ca25325", url="https://pypi.org/packages/60/9a/a41765e60b34af1ba24b7c6dc4d46eb37821cd3a7d616186997b37cb63b2/fastapi-0.84.0-py3-none-any.whl")
    version("0.83.0", sha256="694a2b6c2607a61029a4be1c6613f84d74019cb9f7a41c7a475dca8e715f9368", url="https://pypi.org/packages/bc/34/6746797c8b5275649f99ed57e5a6dd60f912649c0f8ac985b362efd9e8c7/fastapi-0.83.0-py3-none-any.whl")
    version("0.82.0", sha256="a4269329a7374c78f6e92c195d14cc4ce3a525e25b79e62edf2df8196469743f", url="https://pypi.org/packages/56/c7/e36aa8a7a04a2536b559abd7ced3a69fbabb324b27911b7a4c50276167cf/fastapi-0.82.0-py3-none-any.whl")
    version("0.81.0", sha256="9ac5f5d252b4b394df29accb1ed4bedf30e0e87fc6eb7ec75e1449fa040bfc17", url="https://pypi.org/packages/d0/64/63e77ebc5c641dd3d021acd658de8b8710060c742b3557c02f8b4df272a2/fastapi-0.81.0-py3-none-any.whl")

    variant("all", default=False)

    with default_args(type="run"):
        depends_on("py-anyio@3.7.1:3", when="@0.103.1:0.107")
        depends_on("py-email-validator@2:", when="@0.100:+all")
        depends_on("py-email-validator@1.1.1:", when="@0.87:0.99+all")
        depends_on("py-email-validator@1.1.1:1", when="@0.59:0.86+all")
        depends_on("py-httpx@0.23:", when="@0.87:+all")
        depends_on("py-itsdangerous@1:", when="@0.70:+all")
        depends_on("py-jinja2@2.11.2:", when="@0.70:+all")
        depends_on("py-orjson@3.2.1:", when="@0.59:+all")
        depends_on("py-pydantic@1.7.4:1.7,1.8.2:2.0-beta3,2.0.2:2.0,2.1.1:", when="@0.101:")
        depends_on("py-pydantic@1.7.4:1.7,1.8.2:1", when="@0.96.1:0.99")
        depends_on("py-pydantic@1.6.2:1.6,1.7.4:1.7,1.8.2:1", when="@0.65.1:0.96.0")
        depends_on("py-pydantic-extra-types@2:", when="@0.100.0-beta3:+all")
        depends_on("py-pydantic-settings@2.0.0:", when="@0.100.0-beta3:+all")
        depends_on("py-python-multipart@0.0.7:", when="@0.109.1:+all")
        depends_on("py-python-multipart@0.0.5:", when="@0.87:0.109.0+all")
        depends_on("py-python-multipart@0.0.5", when="@0.59:0.86+all")
        depends_on("py-pyyaml@5.3.1:", when="@0.75.2:+all")
        depends_on("py-requests@2.24:", when="@0.59:0.86+all")
        depends_on("py-starlette@0.36.3:0.36", when="@0.109.2:")
        depends_on("py-starlette@0.35", when="@0.109:0.109.1")
        depends_on("py-starlette@0.29:0.32", when="@0.108")
        depends_on("py-starlette@0.28", when="@0.107")
        depends_on("py-starlette@0.27", when="@0.95.2:0.106")
        depends_on("py-starlette@0.22", when="@0.88:0.89")
        depends_on("py-starlette@0.21", when="@0.87")
        depends_on("py-starlette@0.20.4:0.20", when="@0.85:0.86")
        depends_on("py-starlette@0.19.1:0.19", when="@0.77.1:0.84")
        depends_on("py-typing-extensions@4.8.0:", when="@0.104:")
        depends_on("py-ujson@4.0.1,5.2:", when="@0.75.2:+all")
        depends_on("py-uvicorn@0.12:+standard", when="@0.87:+all")
        depends_on("py-uvicorn@0.12:0.18+standard", when="@0.85:0.86+all")
        depends_on("py-uvicorn@0.12:0.17+standard", when="@0.75.2:0.84+all")
