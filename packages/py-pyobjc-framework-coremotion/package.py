# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkCoremotion(PythonPackage):
    # BEGIN VERSIONS
    version("10.2", sha256="1e1827f2f811ada123dd42809bc86f04a4c1ae3cec619ccf0f05a9387412bec1", url="https://pypi.org/packages/48/b1/addac94215e42ae1cd1cf50a1b8418d04dc02a172487ae3fa4666dc3c698/pyobjc-framework-CoreMotion-10.2.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.8:", when="@10:")
        depends_on("py-pyobjc-core@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-cocoa@10.2:", when="@10.2:")
    # END DEPENDENCIES

