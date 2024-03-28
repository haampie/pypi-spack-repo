# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkAvfoundation(PythonPackage):
    # BEGIN VERSIONS
    version("10.2", sha256="4d394014f2477c0c6a596dbb01ef5d92944058d0e0d954ce6121a676ae9395ce", url="https://pypi.org/packages/e1/10/f0867dcd21afac4edc6d6435e0ab65743503143a911de1ab80648346d3b4/pyobjc-framework-AVFoundation-10.2.tar.gz")
    version("10.1", sha256="07e065c6904fbd6afc434a79888461cdd4097b4153dd592dcbe9c8bef01ee701", url="https://pypi.org/packages/d6/98/e71002607a3b352bf9e9135b81fa8a43a40cc1cbcbd1e4b876c12158591f/pyobjc-framework-AVFoundation-10.1.tar.gz")
    version("10.0", sha256="40366a8c6bb964e7b7263e8cf060350f69ad365e6a5356d6ccab9f256a9987f7", url="https://pypi.org/packages/7e/6f/5623cecd7e1d57600582b9912caf204f2a1523e69b743b5f2d4fd13b9dc4/pyobjc-framework-AVFoundation-10.0.tar.gz")
    version("9.2", sha256="ecf0db71abad6baf127e454e9995adf372249ec6b99e3ede8b6149460ee39c35", url="https://pypi.org/packages/9f/0c/f91c9bf84a1f175685c65e3d2b4893f88f41cf12b6d5da03cf00b627e34f/pyobjc-framework-AVFoundation-9.2.tar.gz")
    version("9.1.1", sha256="db7505043139693628e2e84092af53c3876ec590ebfea67fd287e460e2427d35", url="https://pypi.org/packages/61/7d/2271773dbd0b4994aae7e7b3f97b1a5adc5d55ad4d7f7f9cd52d0c8f3d2e/pyobjc-framework-AVFoundation-9.1.1.tar.gz")
    version("9.1", sha256="7ff98e38db98f5c8dace1ed9b31f7a5e03a1091995f16bf1f7b0e226d6ba68e0", url="https://pypi.org/packages/2d/de/742e9dee98d2606a801c6c3af21c58d95ad012e5c892815c440ca170cb22/pyobjc-framework-AVFoundation-9.1.tar.gz")
    version("9.1-beta1", sha256="0d6f0e0a25b6a1bc0e2a7bbf2570f314ae261e3a22c35a62604e1f998f781ca9", url="https://pypi.org/packages/8b/54/e8bec89d42dcdcfab62d7d0df39b216cbcf59537b81a7e12e555645e9ace/pyobjc-framework-AVFoundation-9.1b1.tar.gz")
    version("9.0.1", sha256="4afa1d9b2bdf73b8d776f857b217942382c019a709697d266aa9c48b3f9cc620", url="https://pypi.org/packages/0c/66/fb469d5370aca72cf2ab62bfb7d67a9e8f3281c3e3076bdd67b84109aa42/pyobjc-framework-AVFoundation-9.0.1.tar.gz")
    version("9.0", sha256="c7986e4fa46b25bcefb556458ea6c82f3eacce28be9c27da7f5f60b50b9ea3fc", url="https://pypi.org/packages/97/b5/52c9b5cd83de48171be988dac0129d0bcb41f243495aad1356cd1099b068/pyobjc-framework-AVFoundation-9.0.tar.gz")
    version("8.5.1", sha256="99ccd94c5e31a599310b2cee2eb9c0d77c61d1eab4b799157b8982956ca30a24", url="https://pypi.org/packages/41/e9/215fd9060e582d57fec6ba1c0cf8ee87ddd1458e33da4990c7ca7fbd5bac/pyobjc-framework-AVFoundation-8.5.1.tar.gz")
    version("8.5", sha256="5872245447703535c71839ee9db22472bc3dcf4a2468d72fb48b0e29933bb248", url="https://pypi.org/packages/8e/88/8fbfdddec5981a6eacb694f9eb6f86a8ef6a2ea39fedb1aaafbe69aab187/pyobjc-framework-AVFoundation-8.5.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-pyobjc-core@10.2:", when="@10.2:")
        depends_on("py-pyobjc-core@10.1:", when="@10.1")
        depends_on("py-pyobjc-core@10:", when="@10:10.0")
        depends_on("py-pyobjc-framework-cocoa@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-cocoa@10.1:", when="@10.1")
        depends_on("py-pyobjc-framework-cocoa@10:", when="@10:10.0")
        depends_on("py-pyobjc-framework-coreaudio@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-coreaudio@10.1:", when="@10.1")
        depends_on("py-pyobjc-framework-coreaudio@10:", when="@10:10.0")
        depends_on("py-pyobjc-framework-coremedia@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-coremedia@10.1:", when="@10.1")
        depends_on("py-pyobjc-framework-coremedia@10:", when="@10:10.0")
        depends_on("py-pyobjc-framework-quartz@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-quartz@10.1:", when="@10.1")
        depends_on("py-pyobjc-framework-quartz@10:", when="@10:10.0")
    # END DEPENDENCIES

