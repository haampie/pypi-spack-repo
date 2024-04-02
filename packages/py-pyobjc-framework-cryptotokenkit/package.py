# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkCryptotokenkit(PythonPackage):
    # BEGIN VERSIONS
    version("10.2", sha256="c0adfde2d53da7df1f8827bdf0cbf4419590151dd1041711ab2f66a32bd986f5", url="https://pypi.org/packages/a1/76/61044c432e6935b51e83417f39d76a1dc4ac01b4ecda455da5dde73d7065/pyobjc-framework-CryptoTokenKit-10.2.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.8:", when="@10:")
        depends_on("py-pyobjc-core@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-cocoa@10.2:", when="@10.2:")
    # END DEPENDENCIES

