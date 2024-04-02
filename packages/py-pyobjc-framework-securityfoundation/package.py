# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkSecurityfoundation(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("10.2", sha256="296f7f9ff96a35c19e4aef7621a567c0efe584aafd20ac25a2839dd96bf46a04", url="https://pypi.org/packages/9d/3e/fc6f4c09ffc57816b642ac246de563366508ed888e4e1bc50cd3d24151d3/pyobjc_framework_SecurityFoundation-10.2-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.8:", when="@10:")
        depends_on("py-pyobjc-core@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-cocoa@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-security@10.2:", when="@10.2:")
    # END DEPENDENCIES

