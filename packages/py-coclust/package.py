# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyCoclust(PythonPackage):
    # BEGIN VERSIONS
    version("0.2.1", sha256="47800cc71b91fcf5551252dca865ac2d917891afc458972c3a0bca0de4643cfb", url="https://pypi.org/packages/5d/44/ad5a69c7187c2b7bcf2c45596e9052811a3be52f4fcaa6709937c5146ee2/coclust-0.2.1.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    variant("alldeps", default=False, description="alldeps")
    # END VARIANTS

    # BEGIN DEPENDENCIES
    # END DEPENDENCIES

