##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkIobluetoothui(PythonPackage):
    version("10.2", sha256="f833efa3b1636f7a6cf8b5b2d25fc566757c2c7c06ee7945023aeb992493d96e", url="https://pypi.org/packages/48/7e/1a2b4aa62d2772b2c90a72f311233b0f30a63880dc826b1be61798c9a7c2/pyobjc_framework_IOBluetoothUI-10.2-py2.py3-none-any.whl")
    version("10.1", sha256="809eeb98ce71d0d4a7538fb77f14d1e7cd2c2b91c10605fb8c0d69dbac205de5", url="https://pypi.org/packages/4c/b8/f8e9652e9d4dd6a63a494492eddf5e346bf61256601bb2ed7eb41cd67946/pyobjc_framework_IOBluetoothUI-10.1-py2.py3-none-any.whl")
    version("10.0", sha256="d8e15a2eb39f9d76613fb6ea241ef5c4bd94ae2f21e0fc15661ae44090bea43f", url="https://pypi.org/packages/53/e3/d9c380a0456e1a22f9b729c2df18f875a2a60e0cf794993c3ff93c519962/pyobjc_framework_IOBluetoothUI-10.0-py2.py3-none-any.whl")
    version("9.2", sha256="598369fe3dc8e9557ac58a7ac58f66ca79d7a005f85bd0937ce536928200b5d2", url="https://pypi.org/packages/fd/0a/82c7baf9e35e802869a21ecfa5b1503ee567336ddbc4e11d05c35b91c8e0/pyobjc_framework_IOBluetoothUI-9.2-py2.py3-none-any.whl")
    version("9.1.1", sha256="a2643b3b77572d408fdfb865d118707defd7ebe788b01ef81f6ff10597f05216", url="https://pypi.org/packages/89/08/d2f1d6b485276610b1d0d4edeca49b5715812414ea1b6a7d62c918ea0f79/pyobjc_framework_IOBluetoothUI-9.1.1-py2.py3-none-any.whl")
    version("9.1", sha256="730fa8f0e51b9aac10b1dfcf7f1bb7c0430aad822b8c053ed1fccf06dafe0430", url="https://pypi.org/packages/7a/a7/50473d9b2aed3bb1aee613b496628e87656126265bbae966449479398e5c/pyobjc_framework_IOBluetoothUI-9.1-py2.py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-pyobjc-core@10.2:", when="@10.2:")
        depends_on("py-pyobjc-core@10.1:", when="@10.1")
        depends_on("py-pyobjc-core@10:", when="@10:10.0")
        depends_on("py-pyobjc-core@9.2:", when="@9.2:9")
        depends_on("py-pyobjc-core@9.1.1:", when="@9.1.1:9.1")
        depends_on("py-pyobjc-core@9.1:", when="@9.1:9.1.0")
        depends_on("py-pyobjc-framework-iobluetooth@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-iobluetooth@10.1:", when="@10.1")
        depends_on("py-pyobjc-framework-iobluetooth@10:", when="@10:10.0")
        depends_on("py-pyobjc-framework-iobluetooth@9.2:", when="@9.2:9")
        depends_on("py-pyobjc-framework-iobluetooth@9.1.1:", when="@9.1.1:9.1")
        depends_on("py-pyobjc-framework-iobluetooth@9.1:", when="@9.1:9.1.0")

