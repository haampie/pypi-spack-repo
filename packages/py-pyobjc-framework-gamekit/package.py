# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkGamekit(PythonPackage):
    # BEGIN VERSIONS
    version("10.2", sha256="0ef877db88e8888ecf682b09b9fb1ee6b879f23d521ce3a738a1b0fb2b885974", url="https://pypi.org/packages/0c/e0/89bec2f22f568644254db7f5469f2cc6cf1a2ba3ff3dbcb8a354300359cc/pyobjc-framework-GameKit-10.2.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.8:", when="@10:")
        depends_on("py-pyobjc-core@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-cocoa@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-quartz@10.2:", when="@10.2:")
    # END DEPENDENCIES

