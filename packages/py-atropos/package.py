##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyAtropos(PythonPackage):
    version("1.1.22", sha256="05e40cb9337421479c692e1154b962fbf811d7939b72c197a024929b7ae88b78", url="https://pypi.org/packages/3d/c2/12a5e8653374992e706c5b42c3d2ac00aec5b5fade89f50109411efe6189/atropos-1.1.22.tar.gz")

    with default_args(type="run"):
        depends_on("py-cython@0.25.2:", when="@1.1.22:1.1.28,1.1.32:2.0.0-alpha6")

