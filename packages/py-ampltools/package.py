# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyAmpltools(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.4.6", sha256="a0c7a21a0492f6809bb866f9887b8ad29b28ce43ea0c2f564562eb883bca34e9", url="https://pypi.org/packages/2e/ce/5d7ac093633c8b73e7bfdf34cee14b5dea44e322bf2c938acdfadbb0d735/ampltools-0.4.6-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-requests")
    # END DEPENDENCIES

