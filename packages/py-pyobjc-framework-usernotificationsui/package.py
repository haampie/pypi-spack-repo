# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkUsernotificationsui(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("10.2", sha256="b0909b11655a7ae14e54ba6f80f1c6d34d46de5e8b565d0a51c22f87604ad3d3", url="https://pypi.org/packages/9e/11/facf4e8c84a65c16f04a7c6fbdd4bf4d30889b5c174c7a17f6904387fd3b/pyobjc_framework_UserNotificationsUI-10.2-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.8:", when="@10:")
        depends_on("py-pyobjc-core@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-cocoa@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-usernotifications@10.2:", when="@10.2:")
    # END DEPENDENCIES

