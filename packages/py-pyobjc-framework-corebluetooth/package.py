# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkCorebluetooth(PythonPackage):
    # BEGIN VERSIONS
    version("10.2", sha256="fb69d2c61082935b2b12827c1ba4bb22146eb3d251695fa1d58bbd5835260729", url="https://pypi.org/packages/8a/44/8a76096e3443fed282db423b3a89e28d1ed2d07dd30e9b132e334b0aa929/pyobjc-framework-CoreBluetooth-10.2.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.8:", when="@10:")
        depends_on("py-pyobjc-core@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-cocoa@10.2:", when="@10.2:")
    # END DEPENDENCIES

