##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPythonJenkins(PythonPackage):
    version("1.5.0", sha256="0b57097456839a3901562cd67582e3672b5e39c200c0653e477450534c80c9d3", url="https://pypi.org/packages/ab/22/7099a997bdbaa1105758b577c7c35705a68bda40226e8c0df2415245a081/python_jenkins-1.5.0-py2.py3-none-any.whl")
    version("1.0.2", sha256="54aba30cf49f78f9eb64e9717ad8049dacf090731a3e0c27e6035f9ec52ff78e", url="https://pypi.org/packages/49/41/c52270f1b738ffe1ca4432577d1dffd521c3dfec505f2af55ac2f94d16f1/python-jenkins-1.0.2.tar.gz")

    with default_args(type="run"):
        depends_on("py-multi-key-dict", when="@0.4.9:")
        depends_on("py-pbr@0.8.2:", when="@0.4.14:")
        depends_on("py-requests", when="@1:")
        depends_on("py-six@1.3:", when="@0.4.9:")

