# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyBulker(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.7.3", sha256="9de2b8666f82c8fcfe597bf298d8cdb2920c88e66369c69f9e5bf900497db31d", url="https://pypi.org/packages/fb/3e/abfe2aee8f2c9eb7a4925a776d68ce5f2b209f7bd7065cca61ca053e8ba2/bulker-0.7.3-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-jinja2", when="@0.6:")
        depends_on("py-logmuse@0.2:", when="@0.6:")
        depends_on("py-psutil", when="@0.6:")
        depends_on("py-pyyaml@5.1:", when="@0.6:")
        depends_on("py-ubiquerg@0.5.1:", when="@0.6:")
        depends_on("py-yacman@0.8.4:", when="@0.7.3:")
    # END DEPENDENCIES

