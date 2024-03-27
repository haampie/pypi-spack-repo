##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkUniformtypeidentifiers(PythonPackage):
    version("10.2", sha256="25b72005063a88c5e67bf91d1355973f4bbf3dd7c1b3fb8eb00503020a837b33", url="https://pypi.org/packages/e3/e3/26b6cc8205f971cb3e541eabe2d24357c12cc5e3cdff6da639956eb08145/pyobjc_framework_UniformTypeIdentifiers-10.2-py2.py3-none-any.whl")
    version("10.1", sha256="4c867b298956d74398d2b6354bd932dc109431d9726c8ea2fc9c83e6946a2a7d", url="https://pypi.org/packages/de/47/49269b373d196f184ad4cc88ac157e403fb3c176e62255ecc9de9aa6a02d/pyobjc_framework_UniformTypeIdentifiers-10.1-py2.py3-none-any.whl")
    version("10.0", sha256="04ddee19fcac2cb3f56c69a6a70fe889515d2f03cc2fcecfb5e414c5bf588032", url="https://pypi.org/packages/5c/fc/f037ef5b925ff24d83f0b69ef4cd76bb88455712dc5b8ee93f86cb04593b/pyobjc_framework_UniformTypeIdentifiers-10.0-py2.py3-none-any.whl")
    version("9.2", sha256="390a175f8ee279cef540151d4f55ec20a71faca2b5a0070eddd5cc9d943d3f02", url="https://pypi.org/packages/72/a1/05bb4ccb0f6d20057c01d3f31b5b7a5dc70f8515f00597e74e11f0996654/pyobjc_framework_UniformTypeIdentifiers-9.2-py2.py3-none-any.whl")
    version("9.1.1", sha256="1f623bb8b5abf80e631797916b37b9b4e8b398305ffbae53f5bee50c10783b6d", url="https://pypi.org/packages/7c/c4/164cf3a15b7b1ede5fbff3133b5f71915c9f022206e9db3b417b81f0fc10/pyobjc_framework_UniformTypeIdentifiers-9.1.1-py2.py3-none-any.whl")
    version("9.1", sha256="763ae9b2ad58699d5ac1655f337bb582e921fc657434c3802ada5afd32115aa0", url="https://pypi.org/packages/c5/9b/ee7cd326252205b4d8f508186803c6e3088e5ce5eb55818999d928c35807/pyobjc_framework_UniformTypeIdentifiers-9.1-py2.py3-none-any.whl")
    version("9.0.1", sha256="32ec96c1f99678cb1052d90c9582d78b3f61fcfb485a7b30f034345839370cce", url="https://pypi.org/packages/88/5c/14262423628120ca1376dabe87fb2f15bf6c7dd01f0ec963726c255efd6b/pyobjc_framework_UniformTypeIdentifiers-9.0.1-py2.py3-none-any.whl")
    version("9.0", sha256="e75f30405e8516f7c0f720a1c046235bb7b519db1bbe67b0ed15d02ce416324c", url="https://pypi.org/packages/ff/32/42bf6080b5781fc0b19a922392e375cc6e4fc69013fa7761161bbcdc376e/pyobjc_framework_UniformTypeIdentifiers-9.0-py2.py3-none-any.whl")
    version("8.5.1", sha256="2e0da660ca916ca771edca9520c9ec9a7f23e4d5907c80dbb9f342b0ea85a5a3", url="https://pypi.org/packages/4d/4e/274e2985b1c543e97ba21d3a5f65b1747d2f2e34f2657b54a16ecb4a9d46/pyobjc_framework_UniformTypeIdentifiers-8.5.1-py2.py3-none-any.whl")
    version("8.5", sha256="b20d9bc73a9d291e7ce99ecc1ef69145256bed67b06f80d3b909d54823d9772c", url="https://pypi.org/packages/88/47/9c96dd76af2354c50cc359abe668ebd25360fafd2fca52b41753a0585a56/pyobjc_framework_UniformTypeIdentifiers-8.5-py2.py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-pyobjc-core@10.2:", when="@10.2:")
        depends_on("py-pyobjc-core@10.1:", when="@10.1")
        depends_on("py-pyobjc-core@10:", when="@10:10.0")
        depends_on("py-pyobjc-core@9.2:", when="@9.2:9")
        depends_on("py-pyobjc-core@9.1.1:", when="@9.1.1:9.1")
        depends_on("py-pyobjc-core@9.1:", when="@9.1:9.1.0")
        depends_on("py-pyobjc-core@9.0.1:", when="@9.0.1:9.0")
        depends_on("py-pyobjc-core@9:", when="@9:9.0.0")
        depends_on("py-pyobjc-core@8.5.1:", when="@8.5.1:8")
        depends_on("py-pyobjc-core@8.5:", when="@8.5:8.5.0")
        depends_on("py-pyobjc-framework-cocoa@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-cocoa@10.1:", when="@10.1")
        depends_on("py-pyobjc-framework-cocoa@10:", when="@10:10.0")
        depends_on("py-pyobjc-framework-cocoa@9.2:", when="@9.2:9")
        depends_on("py-pyobjc-framework-cocoa@9.1.1:", when="@9.1.1:9.1")
        depends_on("py-pyobjc-framework-cocoa@9.1:", when="@9.1:9.1.0")
        depends_on("py-pyobjc-framework-cocoa@9.0.1:", when="@9.0.1:9.0")
        depends_on("py-pyobjc-framework-cocoa@9:", when="@9:9.0.0")
        depends_on("py-pyobjc-framework-cocoa@8.5.1:", when="@8.5.1:8")
        depends_on("py-pyobjc-framework-cocoa@8.5:", when="@8.5:8.5.0")

