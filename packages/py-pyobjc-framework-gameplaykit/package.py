##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkGameplaykit(PythonPackage):
    version("10.2", sha256="068ee6f3586f4033d25ed3b0451eab8f388b2970be1dfbe39be01accca7a9b2e", url="https://pypi.org/packages/ae/5b/ec8707e9a84d85cd219da45fa098890cf69e13be4dd447e8fc37d0352ca6/pyobjc-framework-GameplayKit-10.2.tar.gz")
    version("10.1", sha256="12a5d1dc59668df155436250476af029b1765ca68e7a1e2d440158e7130232a3", url="https://pypi.org/packages/86/29/63d522811fe2adf3fa19f4e66fc89e40c8f350e1423ab107cd564c17f2de/pyobjc-framework-GameplayKit-10.1.tar.gz")
    version("10.0", sha256="7e5cf3197a53344638a1957e1827cd86018cf7549a6da73193346cd8c40b1d52", url="https://pypi.org/packages/25/ee/8de2e3b6c1c12a8f7702c2d0498dec2430d7ccc61abc9d7980b8c2848bbb/pyobjc-framework-GameplayKit-10.0.tar.gz")
    version("9.2", sha256="17742e19f0e00c2a0df9d5183d2b6a15451fd2d736b1245eaca845e67037d8fd", url="https://pypi.org/packages/cf/27/e50933947ccfd54f0bb306a81770164ea391675b3e844167abee038f3033/pyobjc-framework-GameplayKit-9.2.tar.gz")
    version("9.1.1", sha256="20008c5142f8bf43b9f8c25c7a0f5ac50e01fb6f9d6aeb14b0109a79845cf2ee", url="https://pypi.org/packages/50/2d/7bcce646520049dee37226331db001c8d471667974331ca737861621421c/pyobjc-framework-GameplayKit-9.1.1.tar.gz")
    version("9.1", sha256="082b46e29fbe51a2c41a9446a927fad4f3a290b2ebc2721d09d24a70dd99f703", url="https://pypi.org/packages/b8/d9/78f5310241adbb58aa5b716afc7fbc88ad5adcbc42c4fac6ba27bffa625d/pyobjc-framework-GameplayKit-9.1.tar.gz")
    version("9.0.1", sha256="a5419cf0d93dfc3cf3937ffbcdb6bf8a4d0ff0f2bab04e3932ec92428c269195", url="https://pypi.org/packages/fa/f1/60ade23248be85d185dc9e789683e55393d0ab6d2c48e4dc79101577f596/pyobjc-framework-GameplayKit-9.0.1.tar.gz")
    version("9.0", sha256="625211d30f3b7d318101506ad36cf9a93a18eb50f7adcf518ada22bb1eec7c19", url="https://pypi.org/packages/bb/0b/791ac33dcb1058ba67c5f4589bdbb8908d6e208bb07f081e969a62b8409e/pyobjc-framework-GameplayKit-9.0.tar.gz")
    version("8.5.1", sha256="979331ff68223cae39ecdb6518c8ba2c2042bafb93f62906f812d0f91984c30c", url="https://pypi.org/packages/4c/e3/f7d8691eb0f39915c34a28bec8290b0124a0cfb39eaf2dad82aa62cbf7d3/pyobjc-framework-GameplayKit-8.5.1.tar.gz")
    version("8.5", sha256="18872cb334e070b2c843f17d8fc5351c1957042cfdc653d73f4bd0dd33ca83b0", url="https://pypi.org/packages/b5/80/183ae316f5d05ce39b1bfc5cbadbf368179b51bf94895f3c124594721033/pyobjc-framework-GameplayKit-8.5.tar.gz")

    with default_args(type="run"):
        depends_on("py-pyobjc-core@10.2:", when="@10.2:")
        depends_on("py-pyobjc-core@10.1:", when="@10.1")
        depends_on("py-pyobjc-core@10:", when="@10:10.0")
        depends_on("py-pyobjc-framework-cocoa@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-cocoa@10.1:", when="@10.1")
        depends_on("py-pyobjc-framework-cocoa@10:", when="@10:10.0")
        depends_on("py-pyobjc-framework-spritekit@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-spritekit@10.1:", when="@10.1")
        depends_on("py-pyobjc-framework-spritekit@10:", when="@10:10.0")

