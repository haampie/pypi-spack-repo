# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyUproot3Methods(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.10.1", sha256="10e4be8dbcabdf3efb5cce185b0b8ede2ed8390e875750649c6f1c277c26d28c", url="https://pypi.org/packages/3f/57/598207abeb64bf3e0af3fdc19217e56936b6bebabaac6ee270fb151790ce/uproot3_methods-0.10.1-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-awkward0")
        depends_on("py-numpy@1.13.1:")
    # END DEPENDENCIES

