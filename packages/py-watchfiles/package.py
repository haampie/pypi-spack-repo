##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyWatchfiles(PythonPackage):
    version("0.21.0", sha256="c76c635fabf542bb78524905718c39f736a98e5ab25b23ec6d4abede1a85a6a3", url="https://pypi.org/packages/66/79/0ee412e1228aaf6f9568aa180b43cb482472de52560fbd7c283c786534af/watchfiles-0.21.0.tar.gz")
    version("0.20.0", sha256="728575b6b94c90dd531514677201e8851708e6e4b5fe7028ac506a200b622019", url="https://pypi.org/packages/ef/48/02d2d2cbf54e134810b2cb40ac79fdb8ce08476184536a4764717a7bc9f4/watchfiles-0.20.0.tar.gz")
    version("0.19.0", sha256="d9b073073e048081e502b6c6b0b88714c026a1a4c890569238d04aca5f9ca74b", url="https://pypi.org/packages/b3/17/d9453f774dd079fbe7d51565d58006f5059fc17c2fbcf952ef176fbb8657/watchfiles-0.19.0.tar.gz")
    version("0.18.1", sha256="4ec0134a5e31797eb3c6c624dbe9354f2a8ee9c720e0b46fc5b7bab472b7c6d4", url="https://pypi.org/packages/5e/6a/2760278f309655cc7305392b0bb664738104202bf5d50396eb138258c5ca/watchfiles-0.18.1.tar.gz")
    version("0.18.0", sha256="bbe10d134eef1666451382015e48f092c941a6d4562a98ffa1a288f79a897c46", url="https://pypi.org/packages/86/77/93890b16c82d08137b95cef4629914e41df78480108b04ab447e9adb13c5/watchfiles-0.18.0.tar.gz")
    version("0.17.0", sha256="ae7c57ef920589a40270d5ef3216d693f4e6f8864d8fc8b6cb7885ca98ad2a61", url="https://pypi.org/packages/64/4a/d3916ad0c51aaf2ce9e24a71a49ae2274009e370962852bd9de4170cbea4/watchfiles-0.17.0.tar.gz")
    version("0.16.1", sha256="aed7575e24434c8fec2f2bbb0cecb1521ea1240234d9108db7915a3424d92394", url="https://pypi.org/packages/49/91/a9fbbe005ebb36fc17f78cf0dbe54ba71423375a7d6d6c75c01328fee6f0/watchfiles-0.16.1.tar.gz")
    version("0.15.0", sha256="cab62510f990d195986302aa6a48ed636d685b099927049120d520c96069fa49", url="https://pypi.org/packages/fa/9c/0b193edd1fe3ce2d8cdc109f578c5eded48151c6ab7bef8415619b8a5a9f/watchfiles-0.15.0.tar.gz")
    version("0.14.1", sha256="babcc3a3502879224e33ba5f25adfbf37a4f22898977c2d96d0ed3eee99eca8a", url="https://pypi.org/packages/c7/ff/dace40df6b334bf1bf0a3d56273e5ea08a590d9d342c63f54e6cb014cdf6/watchfiles-0.14.1.tar.gz")
    version("0.14", sha256="e9d8ff971eb5e5636602c2ae1853b110da7864efead54905aa3db5a999074619", url="https://pypi.org/packages/61/22/23c64fff847713349f56fe9c9a559e22e6d3190379ba66baf40ac1ad2c06/watchfiles-0.14.tar.gz")

    with default_args(type="run"):
        depends_on("python@3.10:", when="@0.0.1:0.0.2,0.0.8:0.0")
        depends_on("py-anyio@3.0.0:", when="@0.18.1:")
        depends_on("py-anyio@3.0.0:3", when="@0.15:0.18.0")

