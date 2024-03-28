# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPytestArraydiff(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.3", sha256="7d981cf9c09178f40d00c7b791a226438a2c1b46f210ddaaaa1c6aa63cae6456", url="https://pypi.org/packages/b2/dd/0096e95a7da9d6cd566c35bd85b97659303007c2e8a3573c5d51fbf5da3d/pytest_arraydiff-0.3-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-numpy", when="@0.2:")
        depends_on("py-pytest", when="@0.2:0.3")
        depends_on("py-six", when="@0.2:0.3")
    # END DEPENDENCIES

