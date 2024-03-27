##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPytestFlakes(PythonPackage):
    version("4.0.3", sha256="70e8739f6500fd706bdc60bc097c3a25dc82ca195e2a50a1971405a451e19ae7", url="https://pypi.org/packages/3f/b0/bbebeebda9c8c55618b092320b3e77ffc6ff36cd2757540c980683919854/pytest_flakes-4.0.3-py2.py3-none-any.whl")
    version("4.0.2", sha256="6733db47937d9689032876359e5ee0ee6926e3638546c09220e2f86b3581d4c1", url="https://pypi.org/packages/4e/79/8a734df2cf59c806bf2b8231eaa9963ed7688d14df23460020f5c3986916/pytest-flakes-4.0.2.tar.gz")

    with default_args(type="run"):
        depends_on("py-pyflakes", when="@4.0.1,4.0.3:")
        depends_on("py-pytest@5:", when="@4.0.3:")

