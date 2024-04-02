# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyLibcst(PythonPackage):
    # BEGIN VERSIONS
    version("0.4.9", sha256="01786c403348f76f274dbaf3888ae237ffb73e6ed6973e65eba5c1fc389861dd", url="https://pypi.org/packages/fa/4d/366f6fede5c5121fdda08db85a79f8b602a24378394cd9f87c917232d578/libcst-0.4.9.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.7:", when="@0.4.2:1.0")
    # END DEPENDENCIES

