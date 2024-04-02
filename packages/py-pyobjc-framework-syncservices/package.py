# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkSyncservices(PythonPackage):
    # BEGIN VERSIONS
    version("10.2", sha256="1c76073484924201336e6aab40f10358573bc640a92ed4066b8062c748957576", url="https://pypi.org/packages/b0/d6/bc6bca1b287612b899913e688d72b95a2e1a24107132b24bc66e7531edc9/pyobjc-framework-SyncServices-10.2.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.8:", when="@10:")
        depends_on("py-pyobjc-core@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-cocoa@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-coredata@10.2:", when="@10.2:")
    # END DEPENDENCIES

