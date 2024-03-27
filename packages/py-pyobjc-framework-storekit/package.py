##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkStorekit(PythonPackage):
    version("10.2", sha256="44cf0b5fe605b9e5dc6aed2ae9e09d807d04d5f2eaf78afb8c04e3f109a0d680", url="https://pypi.org/packages/57/b6/122f3990665aa63beeae13487d079362c1e35d7ad76c63f95f95bb050d72/pyobjc-framework-StoreKit-10.2.tar.gz")
    version("10.1", sha256="4e91d77d1b9745eca6730ddf6cde964e2bd956fafad303591f671ebd1d4de64b", url="https://pypi.org/packages/f1/e8/551028597307d7678df93e7264e38d7a9d2846e85957b01cce5d84338c75/pyobjc-framework-StoreKit-10.1.tar.gz")
    version("10.0", sha256="5835de40067e2ea4374babb41da4ebc0bbe087b770c352bdababfa6871e9590a", url="https://pypi.org/packages/3a/46/2a5dc77e5c426124617c2bca7c860fc43861937406d1b23506d280c60b1d/pyobjc-framework-StoreKit-10.0.tar.gz")
    version("9.2", sha256="da690f3a9b96a7ed454a0cde872fc4557629005c384832c1a8b6e57ee1051ec5", url="https://pypi.org/packages/6f/0a/a38c6f6d55a2edc4ec7eea61bc3176698cbbd0ff81538d4b23011434af03/pyobjc-framework-StoreKit-9.2.tar.gz")
    version("9.1.1", sha256="644e73b2aad93a3d7f03933acdc00a4e77ed86e5ce840cd1c0a8be4a4e7531d3", url="https://pypi.org/packages/d2/0b/67daed1cb924860c853cc98704d8f5c1455cb10ad41030dde03d6b401ed1/pyobjc-framework-StoreKit-9.1.1.tar.gz")
    version("9.1", sha256="13f511479c6ee88dc90eeef4b21dd453c828cd852fdcb0b5baf97172c4119b9a", url="https://pypi.org/packages/8b/e1/63652bef97b80bf9915837dd639be28b4a365accc5d8012386762018f021/pyobjc-framework-StoreKit-9.1.tar.gz")
    version("9.0.1", sha256="f6dc49a17b6befb4d4d891c26080265edc1c260dbf14e66bca1ad037a72a7adc", url="https://pypi.org/packages/4c/03/e63b6eba0def94e4f5f6476edfab0d692a42920b8787ff9e38512206fe28/pyobjc-framework-StoreKit-9.0.1.tar.gz")
    version("9.0", sha256="583541a76588e93e6ef863c83ca10af645009a8394dd13652d0e378b949bca49", url="https://pypi.org/packages/8e/11/68fcb9d27d201abb9c8fe08b87b3a98848e8cb445ec2ba106d54657d871d/pyobjc-framework-StoreKit-9.0.tar.gz")
    version("8.5.1", sha256="3048bb3faf870675d7357edf3555f894ce7aa062a3667a4bbb88160899c8db41", url="https://pypi.org/packages/1e/d1/b7b96c6522e05abcc9f0df7efd459dd23db675c4228c53b0ee201543d03b/pyobjc-framework-StoreKit-8.5.1.tar.gz")
    version("8.5", sha256="466486f3a2fc316e5db2324e85666ca814ad2a1ee963382ec8d24bd2aaac6dbc", url="https://pypi.org/packages/15/c4/cfbb22a45b27034370ddae47ad3e27493fee89942fdf5351680f4169cac1/pyobjc-framework-StoreKit-8.5.tar.gz")

    with default_args(type="run"):
        depends_on("py-pyobjc-core@10.2:", when="@10.2:")
        depends_on("py-pyobjc-core@10.1:", when="@10.1")
        depends_on("py-pyobjc-core@10:", when="@10:10.0")
        depends_on("py-pyobjc-framework-cocoa@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-cocoa@10.1:", when="@10.1")
        depends_on("py-pyobjc-framework-cocoa@10:", when="@10:10.0")

