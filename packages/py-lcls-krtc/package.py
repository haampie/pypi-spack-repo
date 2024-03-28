# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyLclsKrtc(PythonPackage):
    # BEGIN VERSIONS
    version("0.2.0", sha256="20e6327d488d23e29135be44504bf7df72e4425a518f4222841efcd2cd2985f9", url="https://pypi.org/packages/78/42/e7ccca34ecd16f89e10d4ab28a6aa3b7947aba9fe2026340993d082fd4a2/lcls-krtc-0.2.0.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.9:", when="@0.3:")
    # END DEPENDENCIES

