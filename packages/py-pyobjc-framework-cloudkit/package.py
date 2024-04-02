# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkCloudkit(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("10.2", sha256="32bd77c2b9109113b2321feb6ed6d754af99df6569d953371f1547123be80467", url="https://pypi.org/packages/80/e3/2030ff7ec63b3d3ba0aa178bc17a902e2e3f51b9b7747660ccd653aec855/pyobjc_framework_CloudKit-10.2-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.8:", when="@10:")
        depends_on("py-pyobjc-core@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-accounts@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-cocoa@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-coredata@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-corelocation@10.2:", when="@10.2:")
    # END DEPENDENCIES

