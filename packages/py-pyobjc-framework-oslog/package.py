# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkOslog(PythonPackage):
    # BEGIN VERSIONS
    version("10.2", sha256="2377637a0de7dd60f610caab4bcd7efa165d23dba4ac896fd542f1fab2fc588a", url="https://pypi.org/packages/ef/76/f808e7ca93f38a2552329e3eca85b2047910e61d12f1b3ceb7b7a752fd5e/pyobjc-framework-OSLog-10.2.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.8:", when="@10:")
        depends_on("py-pyobjc-core@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-cocoa@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-coremedia@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-quartz@10.2:", when="@10.2:")
    # END DEPENDENCIES

