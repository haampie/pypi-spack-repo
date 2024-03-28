# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyFlattenDict(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.3.0", sha256="96038f9a0a09dca205112ae890e1f2159cfdf2af173397b2aa93d1bb9d055890", url="https://pypi.org/packages/9f/30/02e342a45b85c17cdf8238c7e9b612998fc59c7314e13fcd00fbb806dafb/flatten_dict-0.3.0-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-pathlib2@2.3:", when="@0.2:0.3")
        depends_on("py-six@1.12:", when="@0.2:")
    # END DEPENDENCIES

