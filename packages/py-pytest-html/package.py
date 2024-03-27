##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPytestHtml(PythonPackage):
    version("3.2.0", sha256="868c08564a68d8b2c26866f1e33178419bb35b1e127c33784a28622eb827f3f3", url="https://pypi.org/packages/81/e1/35ae038e10ba11758e7d572f656ea7b99795f3d37d20aa40a5d7e8050091/pytest_html-3.2.0-py3-none-any.whl")
    version("3.1.1", sha256="b7f82f123936a3f4d2950bc993c2c1ca09ce262c9ae12f9ac763a2401380b455", url="https://pypi.org/packages/75/36/6d3c3011751beefafcc7df6255c67b3739c0f8767691d21cbd7c9464aac8/pytest_html-3.1.1-py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-py@1.8.2:", when="@3.2:3")
        depends_on("py-pytest@5:6.0.0-rc1,6.0.1:", when="@3")
        depends_on("py-pytest-metadata", when="@1.14:3")

