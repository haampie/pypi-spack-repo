# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkUsernotifications(PythonPackage):
    # BEGIN VERSIONS
    version("10.2", sha256="3a1b7d77c95dff109f904451525752ece3c38f38cfa0825fd01735388c2b0264", url="https://pypi.org/packages/be/a5/9fc721a019096bf5caad76e0a288ed9b08d123166e04e5477154ec90930a/pyobjc-framework-UserNotifications-10.2.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.8:", when="@10:")
        depends_on("py-pyobjc-core@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-cocoa@10.2:", when="@10.2:")
    # END DEPENDENCIES

