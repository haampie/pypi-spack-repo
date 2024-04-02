# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkMapkit(PythonPackage):
    # BEGIN VERSIONS
    version("10.2", sha256="35dfe7aa5ec9e51abc47d6ceb0f83d3c2b5876258591a568e85e2db8218427c4", url="https://pypi.org/packages/33/2b/e30a760dd6c6b7a123f5182ef52a2220dc06daf207ca5bf9963b755cf07f/pyobjc-framework-MapKit-10.2.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.8:", when="@10:")
        depends_on("py-pyobjc-core@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-cocoa@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-corelocation@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-quartz@10.2:", when="@10.2:")
    # END DEPENDENCIES

