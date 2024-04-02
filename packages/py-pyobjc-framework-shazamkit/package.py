# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkShazamkit(PythonPackage):
    # BEGIN VERSIONS
    version("10.2", sha256="f3359be7a0ffe0084d047b8813dd9e9b5339a0970baecad89cbe85513e838e74", url="https://pypi.org/packages/5c/ef/080d25bdeec9147d4dc029c9f15d4291c73db311473d5c6dd14f4f82128f/pyobjc-framework-ShazamKit-10.2.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.8:", when="@10:")
        depends_on("py-pyobjc-core@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-cocoa@10.2:", when="@10.2:")
    # END DEPENDENCIES

