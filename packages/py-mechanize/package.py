##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyMechanize(PythonPackage):
    version("0.4.3", sha256="4e8a7703bef5d43b5c753e64e27451b4e66fdc32554b31f5563ad1a82f3142bc", url="https://pypi.org/packages/bc/68/5ab6f96dfbdae2182e214cf9cc4790f2810c695c04034cc067b0e4ffa2b7/mechanize-0.4.3-py2.py3-none-any.whl")
    version("0.2.5", sha256="84b9d9dfe34a039dab75adf33e226631f29a5267a0fdfa99a8ff035a021507f4", url="https://pypi.org/packages/ca/fd/edbcc1abd5bbfc0e19fb3a8d3eebfd11d7d1ce9c8f24c0f54e8db09956b3/mechanize-0.2.5.zip")

    with default_args(type="run"):
        depends_on("py-html5lib@0.999999999:", when="@0.3.2:")

