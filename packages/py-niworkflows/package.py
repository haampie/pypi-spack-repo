# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyNiworkflows(PythonPackage):
    # BEGIN VERSIONS
    version("1.4.0", sha256="d4e59070fde0290e0bfeece120ff1d2ff1f9573e3f2e6a719fe463c913af25ec", url="https://pypi.org/packages/44/09/78e7ebc0f09a7509b849b6971b7222ceefe39769a3b8929258721071e16a/niworkflows-1.4.0.tar.gz")
    version("1.3.5", sha256="92e24f3462fb3ad4d8ee724506fba05da2b3ca0626850dd2e637a553e17d69b8", url="https://pypi.org/packages/83/6b/5677313ba8707a38f88a2efad2af549394903437c386c097dd78ad0b36e1/niworkflows-1.3.5.tar.gz")
    version("1.0.4", sha256="34bfa5561e6f872dbd85bb30a1b44c5e1be525167abe3932aee8ac06d15f6ed9", url="https://pypi.org/packages/d6/38/7757d3bd28bba00d21921e60e309fbf263a15dd65b83e22e7434ef6b07c7/niworkflows-1.0.4.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    variant("ants", default=False)
    variant("fsl", default=False)
    # END VARIANTS

    # BEGIN DEPENDENCIES
    # END DEPENDENCIES

