# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyWatchfiles(PythonPackage):
    # BEGIN VERSIONS
    version("0.18.1", sha256="4ec0134a5e31797eb3c6c624dbe9354f2a8ee9c720e0b46fc5b7bab472b7c6d4", url="https://pypi.org/packages/5e/6a/2760278f309655cc7305392b0bb664738104202bf5d50396eb138258c5ca/watchfiles-0.18.1.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.10:", when="@0.0.1:0.0.2,0.0.8:0.0")
        depends_on("py-anyio@3.0.0:", when="@0.18.1:")
    # END DEPENDENCIES

