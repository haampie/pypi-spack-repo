# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyContextily(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("1.0.1", sha256="945b31a3fab38a31f06379cefa6d625d02ac56610c3a4dedd5b5b7dc82a8cb7a", url="https://pypi.org/packages/93/2a/22b34b6129303c594c21cb80ded800ebd6d13037f00d162d9b3a3785d5ea/contextily-1.0.1-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-geopy", when="@1:")
        depends_on("py-joblib", when="@1.0-rc2:")
        depends_on("py-matplotlib", when="@1.0-rc2:")
        depends_on("py-mercantile", when="@1:")
        depends_on("py-pillow", when="@1:")
        depends_on("py-rasterio", when="@1:")
        depends_on("py-requests", when="@1:")
    # END DEPENDENCIES

