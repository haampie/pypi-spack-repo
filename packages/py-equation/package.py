# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyEquation(PythonPackage):
    # BEGIN VERSIONS
    version("1.2.1", sha256="c8a21dc47d6c748fd19b6485978cf8c42fe31c43db7f44789d95fb5e9752b81c", url="https://pypi.org/packages/fd/0d/ede829e7c0c457b651de2792cd19a739e4885477f59832da54d2cc7a1982/Equation-1.2.01.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    variant("sciconst", default=False, description="sciconst")
    variant("vectormaths", default=False, description="vectormaths")
    # END VARIANTS

    # BEGIN DEPENDENCIES
    # END DEPENDENCIES

