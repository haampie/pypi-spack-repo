# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyConfigspace(PythonPackage):
    # BEGIN VERSIONS
    version("0.4.20", sha256="2e4ca06f5a6a61e5322a73dd7545468c79f2a3e8385cab92fdada317af41d9e9", url="https://pypi.org/packages/58/5f/aa942c9a2bdf1cd4689cea6bb4877dd1b1d359df187e4d3ab258a0dd50fe/ConfigSpace-0.4.20.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.7:", when="@0.4.20:")
    # END DEPENDENCIES

