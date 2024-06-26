# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyRoifile(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("2024.1.10", sha256="0dde8f4d0971439cc373250b8a312c0acf662249560161d61a191d0d09af1aa1", url="https://pypi.org/packages/d2/9a/edfa8073b0e656d358f0ca66bd09cc1caaafc1208b6004a39053883f4674/roifile-2024.1.10-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    variant("all", default=False, description="all")
    # END VARIANTS

    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.9:", when="@2023.8:")
        depends_on("py-matplotlib", when="@2023.5:+all")
        depends_on("py-numpy", when="@2023.5:")
        depends_on("py-tifffile", when="@2023.5:+all")
    # END DEPENDENCIES

