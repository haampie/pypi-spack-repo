# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkContactsui(PythonPackage):
    # BEGIN VERSIONS
    version("10.2", sha256="2dd5f1993c36caf13527de0890c6c49c08a339e58bc3b3fa303d5a04b672b418", url="https://pypi.org/packages/26/ed/aecdafd1111939e6419cb6e7373c863ae9fe8f612849653504eaf96edb1c/pyobjc-framework-ContactsUI-10.2.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.8:", when="@10:")
        depends_on("py-pyobjc-core@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-cocoa@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-contacts@10.2:", when="@10.2:")
    # END DEPENDENCIES

