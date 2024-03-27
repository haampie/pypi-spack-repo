##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyWradlib(PythonPackage):
    version("1.5.0", sha256="9bf0742d7235ea830e83c2269f6b5d1afd83d92696efce0a7bcdb0c4f6604784", url="https://pypi.org/packages/cb/d8/875538f938f69804049b4ef5df7fe22209e81685882a3287394752aa3306/wradlib-1.5.0.tar.gz")

    with default_args(type="run"):
        depends_on("python@3.9:", when="@1.19:")

