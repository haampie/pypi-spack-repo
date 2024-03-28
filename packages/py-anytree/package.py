# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyAnytree(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("2.8.0", sha256="14c55ac77492b11532395049a03b773d14c7e30b22aa012e337b1e983de31521", url="https://pypi.org/packages/a8/65/be23d8c3ecd68d40541d49812cd94ed0f3ee37eb88669ca15df0e43daed1/anytree-2.8.0-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-six@1.9:", when="@2.5,2.7:2.7.0,2.7.3:2.8")
    # END DEPENDENCIES

