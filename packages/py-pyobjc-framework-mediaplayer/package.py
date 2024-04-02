# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkMediaplayer(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("10.2", sha256="c501ea19380bfbf6b04fbe909fcfe9a78c5ff2a9b58dae87be259066b1ae3521", url="https://pypi.org/packages/ae/01/7baaf79097dce18981152413aafc751a2fa7f1aed024c130a262c7b3d84d/pyobjc_framework_MediaPlayer-10.2-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.8:", when="@10:")
        depends_on("py-pyobjc-core@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-avfoundation@10.2:", when="@10.2:")
    # END DEPENDENCIES

