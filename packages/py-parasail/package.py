##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyParasail(PythonPackage):
    version("1.3.3", sha256="be0a12b5d9b4fef6b5f7001879b01ff67c40f934ccef0726aa523cc4e1859f63", url="https://pypi.org/packages/7a/1e/ebec262cd894b6ab7f2f85950a6fa3fd6a3de1a5c83a9ef9a8c058af3b07/parasail-1.3.3-py2.py3-none-win_amd64.whl")

    with default_args(type="run"):
        depends_on("py-numpy", when="@1.0.1,1.1:")

