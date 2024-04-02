# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkAddressbook(PythonPackage):
    # BEGIN VERSIONS
    version("10.2", sha256="d6969fcbde1d78ec9fa0ebcefc2f453090e35d7590c4b4baf62174e060de6bce", url="https://pypi.org/packages/a4/71/2a4b96d82e240c8b8d5ff266e36edabd51fad5648dfdf365b1e2f9d5b2cb/pyobjc-framework-AddressBook-10.2.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.8:", when="@10:")
        depends_on("py-pyobjc-core@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-cocoa@10.2:", when="@10.2:")
    # END DEPENDENCIES

