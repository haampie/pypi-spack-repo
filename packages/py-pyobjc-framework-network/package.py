# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkNetwork(PythonPackage):
    # BEGIN VERSIONS
    version("10.2", sha256="b39bc26f89cf9fc56cc9c4a99099aef68c388d45b62dc1ec16772ee290b225d4", url="https://pypi.org/packages/a6/1e/0cea1fa634e05a1488cdee39c8a4e00cf55a2fef0b30dc089b48bbcf2cc8/pyobjc-framework-Network-10.2.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.8:", when="@10:")
        depends_on("py-pyobjc-core@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-cocoa@10.2:", when="@10.2:")
    # END DEPENDENCIES

