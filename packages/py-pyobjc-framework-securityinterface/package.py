# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkSecurityinterface(PythonPackage):
    # BEGIN VERSIONS
    version("10.2", sha256="43930539fed05e74f3c692f5ee7848681e7e65c44387af300447514fe8e23ab6", url="https://pypi.org/packages/bf/08/1583580501c6451094619a888764ffa71088de09549872f6dda0c92bbbb2/pyobjc-framework-SecurityInterface-10.2.tar.gz")
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

