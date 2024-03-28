# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPathPy(PythonPackage):
    # BEGIN VERSIONS
    version("12.0.1", sha256="e107a3a8834a97be2a047f4b641822afc76a2b78352610102782732e6b389aa3", url="https://pypi.org/packages/40/62/1464f08672cac67e529967ba83b46f38da5d0ca48ac1ce2a9e7d7680ea10/path.py-12.0.1-py3-none-any.whl")
    version("5.2", sha256="d82923a04b527ff9d6e0161c29d295db4c35d63bb97f4f1071e5b550d7ba3358", url="https://pypi.org/packages/26/01/24b69353a7260052cf1592f94991cf56b58b3f72687df6cfb54ff1e1b165/path.py-5.2.zip")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-importlib-metadata@0.5:", when="@11.4:12.0")
    # END DEPENDENCIES

