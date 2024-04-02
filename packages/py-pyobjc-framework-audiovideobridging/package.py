# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkAudiovideobridging(PythonPackage):
    # BEGIN VERSIONS
    version("10.2", sha256="94d77284aae3a151124aa170074c2902537f540debb076376d49f5ee54fb9ce1", url="https://pypi.org/packages/35/d9/12788ed1536442af93b252d5ad2cce6dbfe888256fb4bebc69f0c215539b/pyobjc-framework-AudioVideoBridging-10.2.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.8:", when="@10:")
        depends_on("py-pyobjc-core@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-cocoa@10.2:", when="@10.2:")
    # END DEPENDENCIES

