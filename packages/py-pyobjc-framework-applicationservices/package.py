# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkApplicationservices(PythonPackage):
    # BEGIN VERSIONS
    version("10.2", sha256="f83d6ed3320afb6648be6defafe0f05bac00d0281fc84ee4766ff977309b659f", url="https://pypi.org/packages/87/cf/9445914f4daa0c7a335a24e443107da9c3c726e6c4220a261f5d6b23ad24/pyobjc-framework-ApplicationServices-10.2.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.8:", when="@10:")
        depends_on("py-pyobjc-core@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-cocoa@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-coretext@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-quartz@10.2:", when="@10.2:")
    # END DEPENDENCIES

