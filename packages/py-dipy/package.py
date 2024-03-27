##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyDipy(PythonPackage):
    version("1.7.0", sha256="59bb647128aae7793215c813bb8ea35dae260ac9f0d938c724064f0af5a05cc3", url="https://pypi.org/packages/1a/62/6f1751dbf39790bfc170449c311fa36f97353d993fd057d1e39d47fc5153/dipy-1.7.0.tar.gz")
    version("1.4.1", sha256="b4bf830feae751f3f985d54cb71031fc35cea612838320f1f74246692b8a3cc0", url="https://pypi.org/packages/ad/c1/2af22bd7d96c3b3b17636417aa48e379bd9e028c323a1a442333d9b05175/dipy-1.4.1.tar.gz")

    with default_args(type="run"):
        depends_on("python@3.9:", when="@1.9:")

