# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyHttpx(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("1.0.0-beta0", sha256="2f57e72cee80879eaccde550fd1192d827d26662c6f3a65b89acdaaba03a4c89", url="https://pypi.org/packages/96/ef/4d9878e3fa50d0f439fe9ed3f26c5bb7d8298a4293d0499e1476b8b8d038/httpx-1.0.0b0-py3-none-any.whl")
    version("0.27.0", sha256="71d5465162c13681bff01ad59b2cc68dd838ea1f10e51574bac27103f00c91a5", url="https://pypi.org/packages/41/7b/ddacf6dcebb42466abd03f368782142baa82e08fc0c1f8eaa05b4bae87d5/httpx-0.27.0-py3-none-any.whl")
    version("0.26.0", sha256="8915f5a3627c4d47b73e8202457cb28f1266982d1159bd5779d86a80c0eab1cd", url="https://pypi.org/packages/39/9b/4937d841aee9c2c8102d9a4eeb800c7dad25386caabb4a1bf5010df81a57/httpx-0.26.0-py3-none-any.whl")
    version("0.25.2", sha256="a05d3d052d9b2dfce0e3896636467f8a5342fb2b902c819428e1ac65413ca118", url="https://pypi.org/packages/a2/65/6940eeb21dcb2953778a6895281c179efd9100463ff08cb6232bb6480da7/httpx-0.25.2-py3-none-any.whl")
    version("0.25.1", sha256="fec7d6cc5c27c578a391f7e87b9aa7d3d8fbcd034f6399f9f79b45bcc12a866a", url="https://pypi.org/packages/82/61/a5fca4a1e88e40969bbd0cf0d981f3aa76d5057db160b94f49603fc18740/httpx-0.25.1-py3-none-any.whl")
    version("0.25.0", sha256="181ea7f8ba3a82578be86ef4171554dd45fec26a02556a744db029a0a27b7100", url="https://pypi.org/packages/33/0d/d9ce469af019741c8999711d36b270ff992ceb1a0293f73f9f34fdf131e9/httpx-0.25.0-py3-none-any.whl")
    version("0.24.1", sha256="06781eb9ac53cde990577af654bd990a4949de37a28bdb4a230d434f3a30b9bd", url="https://pypi.org/packages/ec/91/e41f64f03d2a13aee7e8c819d82ee3aa7cdc484d18c0ae859742597d5aa0/httpx-0.24.1-py3-none-any.whl")
    version("0.24.0", sha256="447556b50c1921c351ea54b4fe79d91b724ed2b027462ab9a329465d147d5a4e", url="https://pypi.org/packages/4e/c1/692013f1e6115a061a14f6c7d05947515a1eb7b85ef6e9bf0ffbf0e92738/httpx-0.24.0-py3-none-any.whl")
    version("0.23.3", sha256="a211fcce9b1254ea24f0cd6af9869b3d29aba40154e947d2a07bb499b3e310d6", url="https://pypi.org/packages/ac/a2/0260c0f5d73bdf06e8d3fc1013a82b9f0633dc21750c9e3f3cb1dba7bb8c/httpx-0.23.3-py3-none-any.whl")
    version("0.23.2", sha256="106cded342a44e443060fab70ef327139248c61939e77d73964560c8d8b57069", url="https://pypi.org/packages/a2/0f/4ecb0da51df4593f1ad86fb9ebd7af6efabbbc89ca80af5a38d42bea472c/httpx-0.23.2-py3-none-any.whl")
    version("0.23.1", sha256="0b9b1f0ee18b9978d637b0776bfd7f54e2ca278e063e3586d8f01cda89e042a8", url="https://pypi.org/packages/e1/74/cdce73069e021ad5913451b86c2707b027975cf302016ca557686d87eb41/httpx-0.23.1-py3-none-any.whl")
    version("0.22.0", sha256="e35e83d1d2b9b2a609ef367cc4c1e66fd80b750348b20cc9e19d1952fc2ca3f6", url="https://pypi.org/packages/2f/d3/6a990516a43a522a72da356c4a91c03e09c0cddce8106e7e1215c120011f/httpx-0.22.0-py3-none-any.whl")
    version("0.15.2", sha256="a2bd6eb6d52f0fbd3b082fc8a37b1f50d6112352a83aa04a60f4107f723b018e", url="https://pypi.org/packages/fc/2c/edea45026079eb4c790aed3d40eea7f0bca199f5f82358d2407cc467efe7/httpx-0.15.2-py3-none-any.whl")
    version("0.11.1", sha256="1d3893d3e4244c569764a6bae5c5a9fbbc4a6ec3825450b5696602af7a275576", url="https://pypi.org/packages/46/a9/36b9e193567d879e2da3dd57c755bdf12aa4c2485b1a4610c5799f387ae5/httpx-0.11.1-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    variant("http2", default=False)
    # END VARIANTS

    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-anyio", when="@0.25.1:0")
        depends_on("py-certifi", when="@0.7.5:")
        depends_on("py-chardet@3", when="@0.7.5:0.14")
        depends_on("py-charset-normalizer", when="@0.19:0.22,1:")
        depends_on("py-h11@0.8:0.9", when="@0.10:0.12")
        depends_on("py-h2@3:", when="@0.19:+http2")
        depends_on("py-h2@3", when="@0.14:0.18+http2")
        depends_on("py-h2@3", when="@0.7.5:0.12")
        depends_on("py-hstspreload", when="@0.9:0.13")
        depends_on("py-httpcore@1:", when="@0.25.2:0")
        depends_on("py-httpcore", when="@0.25.1")
        depends_on("py-httpcore@0.18:0", when="@0.25:0.25.0")
        depends_on("py-httpcore@0.15:0.17", when="@0.24")
        depends_on("py-httpcore@0.15:0.16", when="@0.23.1:0.23")
        depends_on("py-httpcore@0.14.5:0.14", when="@0.22")
        depends_on("py-httpcore@0.13.3:0.13", when="@0.18.2:0.20,1:")
        depends_on("py-httpcore@0.11", when="@0.15")
        depends_on("py-idna", when="@0.24:0")
        depends_on("py-idna@2", when="@0.7.5:0.14.1")
        depends_on("py-rfc3986@1.3:1+idna2008", when="@0.14.2:0.23,1:")
        depends_on("py-rfc3986@1.3:1", when="@0.9:0.14.1")
        depends_on("py-sniffio", when="@0.13.0:")
        depends_on("py-sniffio@1:", when="@0.9:0.12")
        depends_on("py-urllib3@1", when="@0.11:0.12")
    # END DEPENDENCIES

