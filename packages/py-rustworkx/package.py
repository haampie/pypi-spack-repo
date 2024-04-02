# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyRustworkx(PythonPackage):
    # BEGIN VERSIONS
    version("0.12.1", sha256="13a19a2f64dff086b3bffffb294c4630100ecbc13634b4995d9d36a481ae130e", url="https://pypi.org/packages/17/e6/924967efd523c0bfed2868b62c334a3339f21fba0ac4b447089731312159/rustworkx-0.12.1.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.7:", when="@:0.13")
    # END DEPENDENCIES

