# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkCorebluetooth(PythonPackage):
    # BEGIN VERSIONS
    version("10.2", sha256="fb69d2c61082935b2b12827c1ba4bb22146eb3d251695fa1d58bbd5835260729", url="https://pypi.org/packages/8a/44/8a76096e3443fed282db423b3a89e28d1ed2d07dd30e9b132e334b0aa929/pyobjc-framework-CoreBluetooth-10.2.tar.gz")
    version("10.1", sha256="81f50fcd9ee24332f1ad85798d489cfc05be739fcc1389caa6d682e034215efd", url="https://pypi.org/packages/cf/49/d9f702c01ca1a959e35fe1c0cf43012360de41edb7fbdaeca57962ba302a/pyobjc-framework-CoreBluetooth-10.1.tar.gz")
    version("10.0", sha256="dddc9020cd2ca008c7037c61026641fff5d91a608b9e3bda51d4ba6afbb04e3c", url="https://pypi.org/packages/dd/aa/59c89c9b7e538d6cf68d1d71100ce98d10a8580bacbad5cce206b2b1e884/pyobjc-framework-CoreBluetooth-10.0.tar.gz")
    version("9.2", sha256="cb2481b1dfe211ae9ce55f36537dc8155dbf0dc8ff26e0bc2e13f7afb0a291d1", url="https://pypi.org/packages/f1/7a/239d5b1ac63056bb3e754c1f189f3e17051f3d2c3368c339d15b34f2ac48/pyobjc-framework-CoreBluetooth-9.2.tar.gz")
    version("9.1.1", sha256="4e5a256450bd9626311af64b6cf6752d0d9e7bc80242a915dea075180b350ca6", url="https://pypi.org/packages/fc/e2/b2fa61a2f40278d5d1e9f3a2e825bdfc8d9c5d065152c0833e3b79936418/pyobjc-framework-CoreBluetooth-9.1.1.tar.gz")
    version("9.1", sha256="4c886119cc2e345750bdefdc48184764ea9a1eebcd43cdf6c630d1bdfbfc34d8", url="https://pypi.org/packages/4f/24/cecefa5a2a179af9468140b88622fd233862e45df405558838ec46a8afea/pyobjc-framework-CoreBluetooth-9.1.tar.gz")
    version("9.0.1", sha256="bf008d7bfe13cda12a43ed82346acfad262e90824086b145394c154531b51841", url="https://pypi.org/packages/d2/62/8745469594a344d96bcd8862904f912a60718d3c7099ef4fcfe3c8c05544/pyobjc-framework-CoreBluetooth-9.0.1.tar.gz")
    version("9.0", sha256="bcad28f35db0aa33b559cc5b6cc1ac0622d6bdaea367a4f6a849013258840e3f", url="https://pypi.org/packages/aa/2d/813238d7569084ea3007a3d35e1aeeef5e551c3bd0c60804d30c82debb39/pyobjc-framework-CoreBluetooth-9.0.tar.gz")
    version("8.5.1", sha256="b4f621fc3b5bf289db58e64fd746773b18297f87a0ffc5502de74f69133301c1", url="https://pypi.org/packages/3f/c8/db0fe2e46b501c4572d0d78c04c5e49df751661743ca44697ee913d0e378/pyobjc-framework-CoreBluetooth-8.5.1.tar.gz")
    version("8.5", sha256="d83928083b0fc1aa9f653b3bbc4c22558559adbd82689aa461f4ccb295669dd2", url="https://pypi.org/packages/90/7a/9e374286ea0013da443e2ac53a129adcdb4632879322f06e1205466deb6b/pyobjc-framework-CoreBluetooth-8.5.tar.gz")
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

