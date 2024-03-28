# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkSyncservices(PythonPackage):
    # BEGIN VERSIONS
    version("10.2", sha256="1c76073484924201336e6aab40f10358573bc640a92ed4066b8062c748957576", url="https://pypi.org/packages/b0/d6/bc6bca1b287612b899913e688d72b95a2e1a24107132b24bc66e7531edc9/pyobjc-framework-SyncServices-10.2.tar.gz")
    version("10.1", sha256="644d394b84468fa6178b5aa609771252ca416ca2be2bac5501222b3c5151846d", url="https://pypi.org/packages/c6/e5/198590bbde83390a6e63d932c157bb2812ffd5ad58d624ad62656bdd516e/pyobjc-framework-SyncServices-10.1.tar.gz")
    version("10.0", sha256="3060a5b66c42a276b3a5765f7c41fe6a80491685977b0f78b67ef2e8f2325673", url="https://pypi.org/packages/6c/e1/0e262b043ab749844866bf2f308758980e1a61cea32c97136940653d8097/pyobjc-framework-SyncServices-10.0.tar.gz")
    version("9.2", sha256="490791ee4f0a0cbab161aac7a2a65b603c12577f25b225de2f0f598ef28bac95", url="https://pypi.org/packages/0a/78/cfe5d78e0cf6d8a0672c15dc2501142e050caa53d1b25dfb70488a1ce601/pyobjc-framework-SyncServices-9.2.tar.gz")
    version("9.1.1", sha256="c5bcf2ab212120977f9b5dfce26f1b6f5cf4e21619cd98456fc7c5d8dd535896", url="https://pypi.org/packages/e3/ac/75feb5c012c648bacb2cf6680da3d1df871daa55e23b09b9a6d7c552fafe/pyobjc-framework-SyncServices-9.1.1.tar.gz")
    version("9.1", sha256="12b5264dc10e95e9eea97509c8383e264504bf6721767a573da82c084a1d0efb", url="https://pypi.org/packages/a6/30/f737e99545b3a3b58da767eb8e33b2b3ed46567c9bfa9dc6eeb55cbf08f6/pyobjc-framework-SyncServices-9.1.tar.gz")
    version("9.0.1", sha256="9a038f6d857f92f9a4c34329905821726405c07f7be0e0f4a958f423e925633a", url="https://pypi.org/packages/1d/ce/6d56a2269b33840c05b50a51b70528dc5c0da9a18b338001cd50725ff08f/pyobjc-framework-SyncServices-9.0.1.tar.gz")
    version("9.0", sha256="3a62d69cd2f599ded5d616869c0f870e52f5574f5073c0e379744764d5138d98", url="https://pypi.org/packages/5c/ef/d920624f2b4270ba7cf6278bdd536036d694ecbf4efbe94a8d48ad2f04d4/pyobjc-framework-SyncServices-9.0.tar.gz")
    version("8.5.1", sha256="7eb9740709105bafc9d29eb3e400084aa9db34aaa578954fd2ad4484161aede5", url="https://pypi.org/packages/4a/58/50422a9dceaf318fdce78b3119c10c5e0cf92ea36dad929f5d315f0f6c68/pyobjc-framework-SyncServices-8.5.1.tar.gz")
    version("8.5", sha256="97d690570bb3d71b115b3b40a9983d7822b621e4c99bfd1e789c47ebceba8ce9", url="https://pypi.org/packages/5e/16/ea2fd44e5af6ad6a8821bfef6be90dbffec508d6c001331327c4815d8ae9/pyobjc-framework-SyncServices-8.5.tar.gz")
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
        depends_on("py-pyobjc-framework-coredata@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-coredata@10.1:", when="@10.1")
        depends_on("py-pyobjc-framework-coredata@10:", when="@10:10.0")
    # END DEPENDENCIES

