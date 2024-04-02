# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkBackgroundassets(PythonPackage):
    # BEGIN VERSIONS
    version("10.2", sha256="97ad7b0c693e406950c0c4af2edc9320eac9aef7fdf33274903f526b4682fcb7", url="https://pypi.org/packages/4e/b0/d8400cf00af060d0ad5163ed423aaba15779276a557f29099814f68d9c5c/pyobjc-framework-BackgroundAssets-10.2.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.8:", when="@10:")
        depends_on("py-pyobjc-core@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-cocoa@10.2:", when="@10.2:")
    # END DEPENDENCIES

