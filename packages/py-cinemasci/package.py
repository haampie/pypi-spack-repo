# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyCinemasci(PythonPackage):
    # BEGIN VERSIONS
    version("1.7.0", sha256="70e1fa494bcbefdbd9e8859cdf1b01163a94ecffcdfa3da1011e4ef2fcee6169", url="https://pypi.org/packages/0e/02/c346d5afee3dac0f3608b2ee7e7e73c3eca9019c4a4201b444dade90324c/cinemasci-1.7.0.tar.gz")
    version("1.3", sha256="c024ca9791de9d78e5dad3fd11e8f87d8bc1afa5830f2697d7ec4116a5d23c20", url="https://pypi.org/packages/54/15/a8f74245529e92558c9f615d7bd789dd7a97def4c275d2480997cea412b2/cinemasci-1.3.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    variant("mpi", default=False)
    # END VARIANTS

    # BEGIN DEPENDENCIES
    # END DEPENDENCIES

