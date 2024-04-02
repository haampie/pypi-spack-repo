# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyAstropyIersData(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.2024.3.18.0.29.47", sha256="43527f8e52b0309360357d3aef6e888b9f2417fc8b4e66313709802a242e0f81", url="https://pypi.org/packages/ed/19/caa9195acddf60b76020eda8b287b4fbe14068408685381cdfd6ef30ddd4/astropy_iers_data-0.2024.3.18.0.29.47-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.8:")
    # END DEPENDENCIES

