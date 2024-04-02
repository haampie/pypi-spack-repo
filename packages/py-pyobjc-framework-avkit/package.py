# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkAvkit(PythonPackage):
    # BEGIN VERSIONS
    version("10.2", sha256="6497a5109a29235a7fd8bddcb6d79bd495ccd9373b41e84ca3f012a642e5b880", url="https://pypi.org/packages/34/cc/4413f44b57f0a95165701ecc62089a4bb463585b6f6c71957f931818b01f/pyobjc-framework-AVKit-10.2.tar.gz")
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

