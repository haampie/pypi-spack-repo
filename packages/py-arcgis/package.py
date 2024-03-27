##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyArcgis(PythonPackage):
    version("1.8.4", sha256="f1445dac25d3d4c03755d716c74a0930881c6be3cd36d22c6ff5ac754f9842d7", url="https://pypi.org/packages/90/c9/bc09a1e0081b6fa7075cd8df1567816dcf91ddff6dd4ab0b28400db7e1f2/arcgis-1.8.4.tar.gz")

    with default_args(type="run"):
        depends_on("python@3.9:3.11", when="@2.2:")
        depends_on("python@:3.9", when="@2.0.1:2.1")

