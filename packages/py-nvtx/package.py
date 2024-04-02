# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyNvtx(PythonPackage):
    # BEGIN VERSIONS
    version("0.2.10", sha256="58b89cd69079fda1ceef8441eec5c5c189d6a1ff94c090a3afe03aedd0bbd140", url="https://pypi.org/packages/e6/44/9ce1cc9a47273a91742a86c38b9c4a6d80352175630eb6e1096d85ec17fc/nvtx-0.2.10.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    variant("python", default=False, description="python")
    # END VARIANTS

    # BEGIN DEPENDENCIES
    # END DEPENDENCIES

