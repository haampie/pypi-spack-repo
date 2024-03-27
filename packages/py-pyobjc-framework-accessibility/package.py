##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkAccessibility(PythonPackage):
    version("10.2", sha256="275c9ac0df1350bf751dbddc81d98f7702cf03ad66e0271876cef9aa70ca5c24", url="https://pypi.org/packages/b7/4d/18675cb9bb0f1f281fd53d77d5cef2a2ce9268fc6d3a4b6c5f10241ed0a7/pyobjc-framework-Accessibility-10.2.tar.gz")
    version("10.1", sha256="70b812cf2b04b57a520c3fde9df4184c2783795fb355b416a8058114e52ad24a", url="https://pypi.org/packages/ee/09/ed9eb85f68fe1a17ebeb9197ad797368bf6b51381286b491439160129774/pyobjc-framework-Accessibility-10.1.tar.gz")
    version("10.0", sha256="5aa152201ccc235a6bbba271b698de42445a4a058b8dceca982d70384c195255", url="https://pypi.org/packages/d0/16/a8f3b857a2b626a6ad5d6d418c3ae423b14141e77b141cd25d844a9d6de4/pyobjc-framework-Accessibility-10.0.tar.gz")
    version("9.2", sha256="830755932071f1fce79ce9a515b2fa91aa922c1b48bafb0504a3fc45723587a0", url="https://pypi.org/packages/19/86/c0e36fe4ce415cc86f1343476d09711406f37b978d4d3a786f617fd3df65/pyobjc-framework-Accessibility-9.2.tar.gz")
    version("9.1.1", sha256="f013bbe542d5a648578cff20bb8f25490482d34d14cd40a6637759c98f5c049c", url="https://pypi.org/packages/8f/fa/625d9dd8823a54921213d5afca3b031d3e99e4cf545033d18caa5a21a4a4/pyobjc-framework-Accessibility-9.1.1.tar.gz")
    version("9.1", sha256="c9d1296364ddc23e6b502c8fe7ecde847051ba495f390681719bb95501800094", url="https://pypi.org/packages/5b/1d/c1e23afac3876811e60be77191e57eb8d6913893ae40be63a7544975d898/pyobjc-framework-Accessibility-9.1.tar.gz")
    version("9.0.1", sha256="3dd6bdff7597e454846e6171a6c58da3e414bef1fc155ae4255d49a91da527c3", url="https://pypi.org/packages/d8/50/0c8415ff1f45721caae3ddd05615eb116d2907994dce26b5734c93b96fa9/pyobjc-framework-Accessibility-9.0.1.tar.gz")
    version("9.0", sha256="1a3ff40f9ff1a3a1385e57384636a5a9dad88fc3288875516a35e78e4c71ca0e", url="https://pypi.org/packages/28/41/a74a7fc47c5c255c95c5bf2180fb47fed3e56aafeed6a1cb4bb6d445a2c0/pyobjc-framework-Accessibility-9.0.tar.gz")
    version("8.5.1", sha256="8f68f5c85eeaa14baa24e439570a577b14bdab78a34140c1a22c17cf7e63560d", url="https://pypi.org/packages/1f/b0/b5f6314872e6a4f98497409f88324adc8b490afaf306b69b89a8b3c95a0f/pyobjc-framework-Accessibility-8.5.1.tar.gz")
    version("8.5", sha256="cfe60c131891ff43fc2b2a94f8135f2d6c42800eb027d1b70886bae249eb77da", url="https://pypi.org/packages/1f/02/00c0f23847bb8d2752a988490dedf36e4e3bcfe254aaa277f09057979723/pyobjc-framework-Accessibility-8.5.tar.gz")

    with default_args(type="run"):
        depends_on("py-pyobjc-core@10.2:", when="@10.2:")
        depends_on("py-pyobjc-core@10.1:", when="@10.1")
        depends_on("py-pyobjc-core@10:", when="@10:10.0")
        depends_on("py-pyobjc-framework-cocoa@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-cocoa@10.1:", when="@10.1")
        depends_on("py-pyobjc-framework-cocoa@10:", when="@10:10.0")
        depends_on("py-pyobjc-framework-quartz@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-quartz@10.1:", when="@10.1")
        depends_on("py-pyobjc-framework-quartz@10:", when="@10:10.0")

