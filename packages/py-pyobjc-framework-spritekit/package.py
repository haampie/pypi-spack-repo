# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkSpritekit(PythonPackage):
    # BEGIN VERSIONS
    version("10.2", sha256="31b3e639a617c456574df8f3ce18275eff613cf49e98ea8df974cda05d13a7fc", url="https://pypi.org/packages/6b/5e/1206b83c86f1148dc08e870e712cea38a95269347298b83c41c1726c6b1e/pyobjc-framework-SpriteKit-10.2.tar.gz")
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

