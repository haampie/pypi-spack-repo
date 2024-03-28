# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPytestMetadata(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("1.11.0", sha256="576055b8336dd4a9006dd2a47615f76f2f8c30ab12b1b1c039d99e834583523f", url="https://pypi.org/packages/e5/12/bfb677aad996cc994efb9c61289a4994d60079587e85155738859fd3b68e/pytest_metadata-1.11.0-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@:3.10", when="@2.0.1")
        depends_on("py-pytest@2.9:", when="@1.4:1")
    # END DEPENDENCIES

