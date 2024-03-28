# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyCvxopt(PythonPackage):
    # BEGIN VERSIONS
    version("1.2.5", sha256="94ec8c36bd6628a11de9014346692daeeef99b3b7bae28cef30c7490bbcb2d72", url="https://pypi.org/packages/ad/0a/706e021ac6164c2cb587870de345d30fed7e0258af67a9f28ccb7fb3d1d4/cvxopt-1.2.5.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    variant("dsdp", default=False)
    variant("fftw", default=False)
    variant("glpk", default=False)
    variant("gsl", default=False)
    # END VARIANTS

    # BEGIN DEPENDENCIES
    # END DEPENDENCIES

