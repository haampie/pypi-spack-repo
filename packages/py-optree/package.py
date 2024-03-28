# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyOptree(PythonPackage):
    # BEGIN VERSIONS
    version("0.10.0", sha256="dc7e8880f997365083191784d141c790833877af71aec8825c7f2b7f7f43c98e", url="https://pypi.org/packages/02/2f/0cd6aea70fd3058c782e9b4a223121cb3d1a696bc12d376943b37dce60e9/optree-0.10.0.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-typing-extensions@4:", when="@0.9.2:")
    # END DEPENDENCIES

