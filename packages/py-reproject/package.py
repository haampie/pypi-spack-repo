##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyReproject(PythonPackage):
    version("0.7.1", sha256="95c0fa49e6b4e36455b91fa09ad1b71b230c990ad91d948af67ea3509a1a4ccb", url="https://pypi.org/packages/45/56/6d1a85dcb38185edaf2ff2a8c7924eddb56a680b41c1d89961a567985066/reproject-0.7.1.tar.gz")

    with default_args(type="run"):
        depends_on("py-astropy@3.2:", when="@0.6:0.7")
        depends_on("py-astropy-healpix@0.2:", when="@0.6:0.7")
        depends_on("py-numpy@1.13.0:", when="@0.6:0.7")
        depends_on("py-scipy@1.1.0:", when="@0.7.1:0.7")

        # marker: platform_machine != "i686" and extra == "test"
        # depends_on("py-sunpy", when="@0.7:0.7.0")

        # marker: platform_machine != "i686" and extra == "testall"
        # depends_on("py-sunpy", when="@0.7.1:0.7")

