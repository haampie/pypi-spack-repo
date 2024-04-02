# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkVirtualization(PythonPackage):
    # BEGIN VERSIONS
    version("10.2", sha256="49eb8d0ec3017c2194620f0698e95ccf20b8b706c73ab3b1b50902c57f0f86ff", url="https://pypi.org/packages/1b/a5/1ba95f18c50589c8ce0224f3fb9a369bb03d31e8f5b4b3315a16f7b4e15b/pyobjc-framework-Virtualization-10.2.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.8:", when="@10:")
        depends_on("py-pyobjc-core@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-cocoa@10.2:", when="@10.2:")
    # END DEPENDENCIES

