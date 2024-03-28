# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkVirtualization(PythonPackage):
    # BEGIN VERSIONS
    version("10.2", sha256="49eb8d0ec3017c2194620f0698e95ccf20b8b706c73ab3b1b50902c57f0f86ff", url="https://pypi.org/packages/1b/a5/1ba95f18c50589c8ce0224f3fb9a369bb03d31e8f5b4b3315a16f7b4e15b/pyobjc-framework-Virtualization-10.2.tar.gz")
    version("10.1", sha256="48f2484a7627caa246f55daf203927f10600e615e620a2d9ca22e483ed0bb9b4", url="https://pypi.org/packages/7d/4a/0e539044c839cd3f67d62edfe280447874b9cfc2702fe3def844a6f0b247/pyobjc-framework-Virtualization-10.1.tar.gz")
    version("10.0", sha256="6387103c8285fe1226f1f35583a11c3aa208d0fea994923cfb405413985cac91", url="https://pypi.org/packages/72/35/3eed1dcc20032939f83151bfe24fbb102ada2975901c304cf017ce38a10d/pyobjc-framework-Virtualization-10.0.tar.gz")
    version("9.2", sha256="a0e2df5f77eefd9867d69f2fa086903466b901ba9343a6ec2fe34cdda6bf4399", url="https://pypi.org/packages/7e/58/cb15abb219994bd9b678b48d07193c9b86dfae9525d39f31393e92ad6cd9/pyobjc-framework-Virtualization-9.2.tar.gz")
    version("9.1.1", sha256="2bdad1b0a5b5e4bd4a0e90bf5a4971705d9b8e0bb7b330a5bf4b76bdbfb1a680", url="https://pypi.org/packages/ac/99/44c2609abd7748bc436c00357037e355c2e480aa8fa400368204f526beb2/pyobjc-framework-Virtualization-9.1.1.tar.gz")
    version("9.1", sha256="a787ba0ef33d7e23a6670b760eb80aeff7353d840d5a7d776728fd5b8a9d15f4", url="https://pypi.org/packages/03/ae/c12ad31f0698d81e882a68369387bc8dfb54ca8eba7260a41c2221353519/pyobjc-framework-Virtualization-9.1.tar.gz")
    version("9.0.1", sha256="98ecb1e7b8021013edd2905c63d23dfd5cea58c8baaf67715060c84b120a2e95", url="https://pypi.org/packages/16/99/267c82d0cb71f8e78298194277494e2c11186c07d50f971c3841ebd91405/pyobjc-framework-Virtualization-9.0.1.tar.gz")
    version("9.0", sha256="e95b4cb949f91457f0f0e00f4c590f6bffe078f3ecb22646f8caca8449d8041d", url="https://pypi.org/packages/92/21/2bb4ae15f092e3597f75dd0ddeea1ee07bcc77f55b2bd813afdcbbebbaa9/pyobjc-framework-Virtualization-9.0.tar.gz")
    version("8.5.1", sha256="5f437efd52ec9545ba7a74c758f3fffc8534576a6102bb182b4a2d901b1c7c35", url="https://pypi.org/packages/7d/d3/3632c3f73db9c8323533ea9e2c3ecd7ce91ef76d724ecf7265826cd7e68a/pyobjc-framework-Virtualization-8.5.1.tar.gz")
    version("8.5", sha256="3059716d543abb10031b1e98e53302c9353d8519f5b7fa9732f8337623cbf5a7", url="https://pypi.org/packages/09/c7/5d24a22116f56d912c57f5759f367e8b304fbf1835cfb5ed024ab8f1f6aa/pyobjc-framework-Virtualization-8.5.tar.gz")
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
    # END DEPENDENCIES

