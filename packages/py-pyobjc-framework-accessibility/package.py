# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkAccessibility(PythonPackage):
    # BEGIN VERSIONS
    version("10.2", sha256="275c9ac0df1350bf751dbddc81d98f7702cf03ad66e0271876cef9aa70ca5c24", url="https://pypi.org/packages/b7/4d/18675cb9bb0f1f281fd53d77d5cef2a2ce9268fc6d3a4b6c5f10241ed0a7/pyobjc-framework-Accessibility-10.2.tar.gz")
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

