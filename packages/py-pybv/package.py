# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPybv(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.8.0", sha256="a2e36a965dc69a9287dadf047dbb30407274d5da50e21d3d6a27a3cfe06dc373", url="https://pypi.org/packages/b4/cf/1dccbab4e6eefc2967feb928762bcf2c380caf1bdd0e68d09e672e7a60e0/pybv-0.8.0-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.7:3", when="@0.6:")
        depends_on("py-numpy@1.18.1:", when="@0.7:")
    # END DEPENDENCIES

