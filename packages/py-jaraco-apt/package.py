# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyJaracoApt(PythonPackage):
    # BEGIN VERSIONS
    version("2.0", sha256="1eb251473912a0584cc942f7d97a44824b0d14eceb88d1569d7443b88c0eaa7d", url="https://pypi.org/packages/9d/43/0d473b0f074a781d74ac486aecf496ae230898bc7ab45e3181206e2d66da/jaraco.apt-2.0-py2.py3-none-any.whl")
    version("1.3", sha256="4bc92f2307fb6c4119e641425b30f1a60c0e0563949bedd9dba254f5271d6f88", url="https://pypi.org/packages/4d/f7/9aa2826f473dae2c55882893099c00897ecafa5c9d7ec596a85c632f162a/jaraco.apt-1.3-py2.py3-none-any.whl")
    version("1.2", sha256="0f4f316a211c1f59bc32036246e99cf976ab33d5f379ae6bd45f04e604c3e7d4", url="https://pypi.org/packages/f1/ac/1426dd87fc47b413a4fed97bd31a3ff366a7e5de48ded71f5570640fce93/jaraco.apt-1.2-py2.py3-none-any.whl")
    version("1.1", sha256="6e477b175ebe70b266ffad0459738417d044367d1aceb361047c4afa0a0e5ebf", url="https://pypi.org/packages/1f/a3/bef8c085413cce44848948f35b5ed34ad9824c975de99c2fd6b580c683e4/jaraco.apt-1.1-py2.py3-none-any.whl")
    version("1.0", sha256="2e9b2927f23828f70ac784b97eda30648746d4aa0dda193ed80414ce5cc14682", url="https://pypi.org/packages/93/b9/1a257c8fc8aaafb67a9f85cf01252fce984089ddd6de2987f91d0e0a443e/jaraco.apt-1.0.zip")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-six", when="@1.2:")
    # END DEPENDENCIES

