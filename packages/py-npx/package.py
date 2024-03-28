# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyNpx(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.1.0", sha256="5e07deadbf43096d8e1ec63dcd51b34e8d638e8e7e4a95d465e143e5701a0308", url="https://pypi.org/packages/4b/c8/4d8f80bf78c38268274b29c45a1a99ade4ade02b4d8c444ddbcc5fbaf1dd/npx-0.1.0-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-numpy@1.20.0:", when="@0.0.17:")
    # END DEPENDENCIES

