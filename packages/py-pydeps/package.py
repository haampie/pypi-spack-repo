##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPydeps(PythonPackage):
    version("1.9.0", sha256="ba9b8c7d72cb4dfd3f4dd6b8a250c240d15824850a415fd428f2660ed371361f", url="https://pypi.org/packages/6b/64/04a9bb1bcc687a5c3b3e14f75d01f9b00f01656917e5bfa6fd3690464f1a/pydeps-1.9.0.tar.gz")
    version("1.7.1", sha256="7eeb8d0ec2713befe81dd0d15eac540e843b1daae13613df1c572528552d6340", url="https://pypi.org/packages/24/36/21e47c6aa9ded60221135921d3fcdf439be75d11bc38c7869328a98d08ae/pydeps-1.7.1.tar.gz")

    with default_args(type="run"):
        depends_on("py-stdlib-list", when="@1.3.7:1.9.3,1.9.14:")

