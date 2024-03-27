##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyLightgbm(PythonPackage):
    version("3.1.1", sha256="dbc4d3105bd176d395c6ff5f5f65351ce9bc2ad60585c60f4829ad9f6e814807", url="https://pypi.org/packages/80/28/fecd02e7856e36afcdc71ee968b1b3859b3bc784e042991d5520e4d7be2c/lightgbm-3.1.1-py2.py3-none-win_amd64.whl")

    with default_args(type="run"):
        depends_on("py-numpy", when="@2.0.6:")
        depends_on("py-scikit-learn@:0.22-rc3,0.22.1:", when="@3")
        depends_on("py-scipy", when="@2.0.6:")
        depends_on("py-wheel", when="@3.1.1:3")

