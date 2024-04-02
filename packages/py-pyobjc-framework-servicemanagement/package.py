# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkServicemanagement(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("10.2", sha256="e5a1c1746788d0e125cc87cbe0749b2b824fb7a08bc4344c06c9ac6007859187", url="https://pypi.org/packages/89/06/3a51828dba366bba110f6a67d5561348aab96a55aa41ee618ee65a65b388/pyobjc_framework_ServiceManagement-10.2-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.8:", when="@10:")
        depends_on("py-pyobjc-core@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-cocoa@10.2:", when="@10.2:")
    # END DEPENDENCIES

