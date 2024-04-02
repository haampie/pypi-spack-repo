# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkIobluetoothui(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("10.2", sha256="f833efa3b1636f7a6cf8b5b2d25fc566757c2c7c06ee7945023aeb992493d96e", url="https://pypi.org/packages/48/7e/1a2b4aa62d2772b2c90a72f311233b0f30a63880dc826b1be61798c9a7c2/pyobjc_framework_IOBluetoothUI-10.2-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.8:", when="@10:")
        depends_on("py-pyobjc-core@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-iobluetooth@10.2:", when="@10.2:")
    # END DEPENDENCIES

