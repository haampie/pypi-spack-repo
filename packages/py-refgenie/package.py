# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyRefgenie(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.12.1", sha256="cb831e99dcaedfc1cfbcfd8a6579b764a5b52912fdf3190adc030727fab8a126", url="https://pypi.org/packages/73/7f/024700960ef5238f5af119efdc422e14c0be3c0beafa0ea99f705c63f930/refgenie-0.12.1-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-logmuse@0.2.6:", when="@0.9.2:")
        depends_on("py-piper@0.12.1:", when="@0.9.2:")
        depends_on("py-pyfaidx@0.5.5.2:", when="@0.9.2:")
        depends_on("py-refgenconf@0.12.2:", when="@0.12.1:")
        depends_on("py-yacman@0.8.3:", when="@0.12.1:")
    # END DEPENDENCIES

