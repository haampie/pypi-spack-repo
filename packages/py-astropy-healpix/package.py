# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyAstropyHealpix(PythonPackage):
    # BEGIN VERSIONS
    version("0.5", sha256="5ae15da796a840f221fb83e25de791e827b6921bc21a365d99bc1a59c7c0cdad", url="https://pypi.org/packages/99/13/603db11e5107638cc68e101ccab75ab5632b395dc414e088ca2f8148c9fc/astropy-healpix-0.5.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.9:", when="@1:")
    # END DEPENDENCIES

