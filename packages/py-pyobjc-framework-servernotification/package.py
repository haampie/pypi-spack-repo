# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkServernotification(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("8.5.1", sha256="92877ffc70813d01f6eb7a7b40755eb163b9c9b7f22895e3561d6edbea26c392", url="https://pypi.org/packages/dd/fe/4cb4713ee1539c0e1abf4471c0467094d26a245ecb1228cb24bc9850be8d/pyobjc_framework_ServerNotification-8.5.1-py2.py3-none-any.whl")
    version("8.5", sha256="8745dfdca143f3513331b6b118fcb806f9f883d625533fbe67a4037335db7ae1", url="https://pypi.org/packages/a7/26/a1000b714f1ce37cfde2aacd4b7e11b441e2cd76d377bc149dfb10bb300c/pyobjc_framework_ServerNotification-8.5-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-pyobjc-core@8.5.1:", when="@8.5.1:")
        depends_on("py-pyobjc-core@8.5:", when="@8.5:8.5.0")
        depends_on("py-pyobjc-framework-cocoa@8.5.1:", when="@8.5.1:")
        depends_on("py-pyobjc-framework-cocoa@8.5:", when="@8.5:8.5.0")
    # END DEPENDENCIES

