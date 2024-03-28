# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkCinematic(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("10.2", sha256="962af237b284605ecd30d584d2d7fb75fda40e429327578de5d651644d0316da", url="https://pypi.org/packages/78/14/d55614179056c5acd13ca5f1ea9bf229e90adb9faa17191143368ed1b868/pyobjc_framework_Cinematic-10.2-py2.py3-none-any.whl")
    version("10.1", sha256="73408d3bfd9b08389eb6787b0b5df4fe9c351c936fa9b1f95a9c723951e9a988", url="https://pypi.org/packages/ca/48/b8273ecbd929b0591dc9203cd474b054303e36cc74ec6ec00a99cef378a1/pyobjc_framework_Cinematic-10.1-py2.py3-none-any.whl")
    version("10.0", sha256="667197227d10add7869dbcfd8396faa251682ff62a702c125ddaf7566469c25b", url="https://pypi.org/packages/c4/e0/3bcbb1af41e3058f43cec6d98e4e2da08f07801d6e54d27b92a89a2e2de2/pyobjc_framework_Cinematic-10.0-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-pyobjc-core@10.2:", when="@10.2:")
        depends_on("py-pyobjc-core@10.1:", when="@10.1")
        depends_on("py-pyobjc-core@10:", when="@:10.0")
        depends_on("py-pyobjc-framework-avfoundation@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-avfoundation@10.1:", when="@10.1")
        depends_on("py-pyobjc-framework-avfoundation@10:", when="@:10.0")
        depends_on("py-pyobjc-framework-cocoa@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-cocoa@10.1:", when="@10.1")
        depends_on("py-pyobjc-framework-cocoa@10:", when="@:10.0")
        depends_on("py-pyobjc-framework-coremedia@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-coremedia@10.1:", when="@10.1")
        depends_on("py-pyobjc-framework-coremedia@10:", when="@:10.0")
        depends_on("py-pyobjc-framework-metal@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-metal@10.1:", when="@10.1")
        depends_on("py-pyobjc-framework-metal@10:", when="@:10.0")
    # END DEPENDENCIES

