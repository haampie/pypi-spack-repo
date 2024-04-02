# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkScenekit(PythonPackage):
    # BEGIN VERSIONS
    version("10.2", sha256="53d2ffac43684bb7834ae570d3537bd15f2a7711b77cc9e8b7b81f63a697ba03", url="https://pypi.org/packages/62/f2/25b7ffd0b86a78992c71e4d814b796dd79a01e7300b699098e1ee572bb7d/pyobjc-framework-SceneKit-10.2.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.8:", when="@10:")
        depends_on("py-pyobjc-core@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-cocoa@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-quartz@10.2:", when="@10.2:")
    # END DEPENDENCIES

