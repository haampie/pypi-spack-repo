##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyOauth2client(PythonPackage):
    version("4.1.3", sha256="b8a81cc5d60e2d364f0b1b98f958dbd472887acaf1a5b05e21c28c31a2d6d3ac", url="https://pypi.org/packages/95/a9/4f25a14d23f0786b64875b91784607c2277eff25d48f915e39ff0cff505a/oauth2client-4.1.3-py2.py3-none-any.whl")
    version("4.1.2", sha256="cf061f52f75e91d489bf5c276498f8af2655fe331b454f10022441513cf445a6", url="https://pypi.org/packages/82/d8/3eab58811282ac7271a081ba5c0d4b875ce786ca68ce43e2a62ade32e9a8/oauth2client-4.1.2-py2.py3-none-any.whl")
    version("4.1.1", sha256="ed0c670f09db32444f843d5d2f92df00733751dfec9a28b0fd3f00693ff36a04", url="https://pypi.org/packages/00/fe/533a3356d9885ed589428b84d24710c0d2fbb7d1f9d7c2d6ee633a4156e9/oauth2client-4.1.1-py2.py3-none-any.whl")
    version("4.1.0", sha256="42868bb5b93172ab73413314c821926ba86f92be99051aa0f76d39346689dcdb", url="https://pypi.org/packages/2a/8f/8ad3507de44331c16af8328bd4c38992121226e2ad5947c41eb682ebbdb6/oauth2client-4.1.0-py2.py3-none-any.whl")
    version("4.0.0", sha256="f8ff4ad855b8917cdf213a33719e874d0fab1c26d44b2f08c9dfd7a5781889f5", url="https://pypi.org/packages/c4/c0/cb81aae37893383b1ebc9d8aac1f1cc657141762e7ee3e5deda67af04a3b/oauth2client-4.0.0-py2.py3-none-any.whl")
    version("3.0.0", sha256="5b5b056ec6f2304e7920b632885bd157fa71d1a7f3ddd00a43b1541a8d1a2460", url="https://pypi.org/packages/c0/7b/bc893e35d6ca46a72faa4b9eaac25c687ce60e1fbe978993fe2de1b0ff0d/oauth2client-3.0.0.tar.gz")
    version("2.2.0", sha256="53d40b5a2d7fc5d36289f4848a0d763df479ac50ba5fac05424903b9e4caac26", url="https://pypi.org/packages/5c/d6/42f18bd74bcc35b3579f08d8b7eb04ee8579b9b16a763b6505f8897c0d6e/oauth2client-2.2.0.tar.gz")
    version("2.1.0", sha256="d628c9c925815ce0aca159dd4c26f5bc013a8ef025574dd338314d98c1df4f72", url="https://pypi.org/packages/7d/3d/fbafca0c10e400c80711a18365502b46c949f18d4c40d410ce059895bf2a/oauth2client-2.1.0.tar.gz")
    version("2.0.2", sha256="c9f7bf68e9d0f9ec055f1f2f487e5ea53b97b7a2b82f01d48d9a9bb68239535a", url="https://pypi.org/packages/a7/70/95d5fb8b839c2c33e8ed76cc0cc060bd57d6506746790a753137df9ebd60/oauth2client-2.0.2.tar.gz")
    version("2.0.1", sha256="351def3df312364f0c5e38a682c8d8a70a36d884cf40bd0084a67d7b8f7ed7ac", url="https://pypi.org/packages/1d/2a/ac18cd40654bf8c1b8b60bcdb2c959314c17956f5a0e1d0d02208c702d52/oauth2client-2.0.1.tar.gz")

    with default_args(type="run"):
        depends_on("py-httplib2@0.9.1:", when="@4:")
        depends_on("py-pyasn1@0.1.7:", when="@4:")
        depends_on("py-pyasn1-modules@0.0.5:", when="@4:")
        depends_on("py-rsa@3.1.4:", when="@4:")
        depends_on("py-six@1.6.1:", when="@4:")

