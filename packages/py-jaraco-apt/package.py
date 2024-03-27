##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyJaracoApt(PythonPackage):
    version("2.0", sha256="1eb251473912a0584cc942f7d97a44824b0d14eceb88d1569d7443b88c0eaa7d", url="https://pypi.org/packages/9d/43/0d473b0f074a781d74ac486aecf496ae230898bc7ab45e3181206e2d66da/jaraco.apt-2.0-py2.py3-none-any.whl")
    version("1.3", sha256="4bc92f2307fb6c4119e641425b30f1a60c0e0563949bedd9dba254f5271d6f88", url="https://pypi.org/packages/4d/f7/9aa2826f473dae2c55882893099c00897ecafa5c9d7ec596a85c632f162a/jaraco.apt-1.3-py2.py3-none-any.whl")
    version("1.2", sha256="0f4f316a211c1f59bc32036246e99cf976ab33d5f379ae6bd45f04e604c3e7d4", url="https://pypi.org/packages/f1/ac/1426dd87fc47b413a4fed97bd31a3ff366a7e5de48ded71f5570640fce93/jaraco.apt-1.2-py2.py3-none-any.whl")
    version("1.1", sha256="7714695570d5709c77d61d69a3a0d20641624cf142848d95fd57d67a6583e705", url="https://pypi.org/packages/07/81/b42f46f107c8906cd1876d00c3de1ba08249b631e2e9fbe82fb5ec21975f/jaraco.apt-1.1.tar.gz")
    version("1.0", sha256="2e9b2927f23828f70ac784b97eda30648746d4aa0dda193ed80414ce5cc14682", url="https://pypi.org/packages/93/b9/1a257c8fc8aaafb67a9f85cf01252fce984089ddd6de2987f91d0e0a443e/jaraco.apt-1.0.zip")

    with default_args(type="run"):
        depends_on("py-six", when="@1.2:")

