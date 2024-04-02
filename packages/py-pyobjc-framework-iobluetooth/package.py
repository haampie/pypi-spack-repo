# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkIobluetooth(PythonPackage):
    # BEGIN VERSIONS
    version("10.2", sha256="8c4d6a82d0f550c84dce72188369adb9347ad6ee1c8adef996ee1a8c376c51ee", url="https://pypi.org/packages/ce/ba/cfee8bc9d6df041c5955787feb343b736149e304ba13108bd197b8500d99/pyobjc-framework-IOBluetooth-10.2.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.8:", when="@10:")
        depends_on("py-pyobjc-core@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-cocoa@10.2:", when="@10.2:")
    # END DEPENDENCIES

