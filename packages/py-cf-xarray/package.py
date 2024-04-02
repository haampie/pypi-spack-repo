# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyCfXarray(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.9.0", sha256="338ae3e55138b6374f64a70844a1f0dac63811781c456b4c30878874b8b4c2c0", url="https://pypi.org/packages/fd/68/c563ac1b9646579e3b8d47c37442ddaeb46ea983025e348d21b358b20c20/cf_xarray-0.9.0-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.9:", when="@0.8.7:")
        depends_on("py-xarray")
    # END DEPENDENCIES

