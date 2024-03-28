# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPylatex(PythonPackage):
    # BEGIN VERSIONS
    version("1.4.1", sha256="d3c12efb8b260771260443dce78d1e9089c09f9d0b92e6273dfca0bf5e7302fb", url="https://pypi.org/packages/8a/76/015a1d785221d9b0d2ad80759d892a6d9d0a8a05daffc52202311ea3d652/PyLaTeX-1.4.1.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    variant("docs", default=False)
    variant("matplotlib", default=False)
    variant("matrices", default=False)
    variant("quantities", default=False)
    # END VARIANTS

    # BEGIN DEPENDENCIES
    # END DEPENDENCIES

