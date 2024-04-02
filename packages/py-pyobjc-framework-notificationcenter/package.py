# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkNotificationcenter(PythonPackage):
    # BEGIN VERSIONS
    version("10.2", sha256="3771c7a8b8e839d07c7cb51eef2e83666254bdd88bd873b0ba7e385245cda684", url="https://pypi.org/packages/23/76/4e24d50cab85ea0736b09b3ec5d52d206168121658febbb337f2ac2bbd99/pyobjc-framework-NotificationCenter-10.2.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.8:", when="@10:")
        depends_on("py-pyobjc-core@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-cocoa@10.2:", when="@10.2:")
    # END DEPENDENCIES

