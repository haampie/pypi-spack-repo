# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkExternalaccessory(PythonPackage):
    # BEGIN VERSIONS
    version("10.2", sha256="e62af0029b2fd7e07c17a4abe52b20495dba05cba45d7e901acbd43ad19c4cc3", url="https://pypi.org/packages/54/fa/c9dcd5b9185eba20d6734e4f993368324122e7fd272e2a35061381f30dd5/pyobjc-framework-ExternalAccessory-10.2.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.8:", when="@10:")
        depends_on("py-pyobjc-core@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-cocoa@10.2:", when="@10.2:")
    # END DEPENDENCIES

