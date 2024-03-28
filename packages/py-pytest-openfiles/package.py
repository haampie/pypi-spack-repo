# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPytestOpenfiles(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.5.0", sha256="b02389b5666d552e236ccf8d4e971abe97b320653ee77316de23db181dbe4f3a", url="https://pypi.org/packages/c5/85/039b16aed2c8017033d96c8d35ded2e0b2d165b0fd7f38bfe04bb0b669a7/pytest_openfiles-0.5.0-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-psutil", when="@0.4:")
        depends_on("py-pytest@4.6:", when="@0.5:")
    # END DEPENDENCIES

