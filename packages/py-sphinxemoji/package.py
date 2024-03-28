# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PySphinxemoji(PythonPackage):
    # BEGIN VERSIONS
    version("0.2.0", sha256="27861d1dd7c6570f5e63020dac9a687263f7481f6d5d6409eb31ecebcc804e4c", url="https://pypi.org/packages/5e/d4/03eeedb6346625ec40bd4ab16f3d4971f4f3db6f635dc8b2d0ad605368eb/sphinxemoji-0.2.0.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.9:", when="@0.3:")
    # END DEPENDENCIES

