# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkCinematic(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("10.2", sha256="962af237b284605ecd30d584d2d7fb75fda40e429327578de5d651644d0316da", url="https://pypi.org/packages/78/14/d55614179056c5acd13ca5f1ea9bf229e90adb9faa17191143368ed1b868/pyobjc_framework_Cinematic-10.2-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.8:")
        depends_on("py-pyobjc-core@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-avfoundation@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-cocoa@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-coremedia@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-metal@10.2:", when="@10.2:")
    # END DEPENDENCIES

