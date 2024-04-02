# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkCoreservices(PythonPackage):
    # BEGIN VERSIONS
    version("10.2", sha256="90fa09e68e840fdd229b33354f4b2e55e9f95a221fcc30612f4bd92cdc530518", url="https://pypi.org/packages/2f/eb/5b87d6b59745386df3d30a57d4b13d6708fdc4fd3bf62b224f509f5b9cb3/pyobjc-framework-CoreServices-10.2.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.8:", when="@10:")
        depends_on("py-pyobjc-core@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-cocoa@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-fsevents@10.2:", when="@10.2:")
    # END DEPENDENCIES

