# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkCorelocation(PythonPackage):
    # BEGIN VERSIONS
    version("10.2", sha256="59497cc210023479e03191495c880e61fb6f44ad6c435ed1c8dd8def39f3aada", url="https://pypi.org/packages/e5/f3/3a7008caff53b84df92fface16f9bb66a2d4bcddb79261b57bd374479ad3/pyobjc-framework-CoreLocation-10.2.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.8:", when="@10:")
        depends_on("py-pyobjc-core@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-cocoa@10.2:", when="@10.2:")
    # END DEPENDENCIES

