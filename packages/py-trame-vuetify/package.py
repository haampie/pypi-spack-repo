# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyTrameVuetify(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("2.4.3", sha256="a3d05d714b78241d61fb5c76f65754e4b26afae67a3667a2daf47b399035f69c", url="https://pypi.org/packages/4d/3d/96d8f6259996d8ee71fcb6b32ad8d50012609617d70106d14b1f1329f21d/trame_vuetify-2.4.3-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-trame-client")
    # END DEPENDENCIES

