# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkLibxpc(PythonPackage):
    # BEGIN VERSIONS
    version("10.2", sha256="04deac1f9dbd1c19c10d175846017f8e8e51d2b52a2674482638d6b289e883a6", url="https://pypi.org/packages/3b/3e/ccfc601a392fa62bf5dac0c13f4d2227fe8a13b66f07bcbd4e1705a89aab/pyobjc-framework-libxpc-10.2.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.8:", when="@10:")
        depends_on("py-pyobjc-core@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-cocoa@10.2:", when="@10.2:")
    # END DEPENDENCIES

