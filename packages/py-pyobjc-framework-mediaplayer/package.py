# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkMediaplayer(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("10.2", sha256="c501ea19380bfbf6b04fbe909fcfe9a78c5ff2a9b58dae87be259066b1ae3521", url="https://pypi.org/packages/ae/01/7baaf79097dce18981152413aafc751a2fa7f1aed024c130a262c7b3d84d/pyobjc_framework_MediaPlayer-10.2-py2.py3-none-any.whl")
    version("10.1", sha256="10e25a8682cd0d1d8fc0041f0a34e8acf785b541d8c1ebe493c2d17caeef5648", url="https://pypi.org/packages/1a/2c/81be269087283a209b9db8d791c937b8b750d7d864429a12969263e837bd/pyobjc_framework_MediaPlayer-10.1-py2.py3-none-any.whl")
    version("10.0", sha256="19afc844bc204e008eac5f59699b93bae84e6235fa030d72651200414b019fc2", url="https://pypi.org/packages/12/62/10ea9f3f232dbc44b22c870bef2d69961878d64c5f7ce8c9991d16add9d7/pyobjc_framework_MediaPlayer-10.0-py2.py3-none-any.whl")
    version("9.2", sha256="d0f6c908dd561ca2023f2c0b136f1ab35b679ca150217bdc081d7fbb5bae384d", url="https://pypi.org/packages/83/da/5c2cec7a248af189769f9e21a42be5dbf018015a2afe0b354e697c5486ec/pyobjc_framework_MediaPlayer-9.2-py2.py3-none-any.whl")
    version("9.1.1", sha256="403d6d1e63d5665df37234d01feaf59381d8f6bfed6ae13a7357c05045b5a2ed", url="https://pypi.org/packages/88/36/f99519528102d0bdafb5624734afd5fa4a6cd529e38e2929f71e8522d2f1/pyobjc_framework_MediaPlayer-9.1.1-py2.py3-none-any.whl")
    version("9.1", sha256="f845818067fd2aa14437998d4ccb333e44fedbe3514ccb2851f62f97e5367dd2", url="https://pypi.org/packages/06/fa/fc78b970be87a8dd0c485a8725bd1014b6831879ce22d1df31b375c37238/pyobjc_framework_MediaPlayer-9.1-py2.py3-none-any.whl")
    version("9.0.1", sha256="3a97addaef70959c0a9eaa820c95cfa61b0a0b080a3f159e3b68953326dbf621", url="https://pypi.org/packages/32/4a/88c3e95e0fbaa5e4aa3e4e1400d302889ef7ba5175a16097d88d634d95d3/pyobjc_framework_MediaPlayer-9.0.1-py2.py3-none-any.whl")
    version("9.0", sha256="b2b8b3f935346c147685d146137984773fcbc0a4fccdfcc3526cca9e60140637", url="https://pypi.org/packages/64/7c/eeba7cd42a9af3f8babf0fea0b229355696337314d1946ce161b0e63d693/pyobjc_framework_MediaPlayer-9.0-py2.py3-none-any.whl")
    version("8.5.1", sha256="804c5cd961221918e4a1ed90b0e7925f6f5283b36739d1ff7f84cdd3ba3305b8", url="https://pypi.org/packages/7d/a0/3a24324e15bf84b4acb40c20cb51da074214a2a3c556ad2cfee5805a5b9f/pyobjc_framework_MediaPlayer-8.5.1-py2.py3-none-any.whl")
    version("8.5", sha256="45495c6c32adb94c6c672726837e14ba507a6b8455b76eabf170faa921edc136", url="https://pypi.org/packages/6f/39/4bd63b4156a0ff79c0b79ca86d1d7fc4e3678198930630e0d9e6653e5d85/pyobjc_framework_MediaPlayer-8.5-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
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
        depends_on("py-pyobjc-framework-avfoundation@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-avfoundation@10.1:", when="@10.1")
        depends_on("py-pyobjc-framework-avfoundation@10:", when="@10:10.0")
        depends_on("py-pyobjc-framework-avfoundation@9.2:", when="@9.2:9")
        depends_on("py-pyobjc-framework-avfoundation@9.1.1:", when="@9.1.1:9.1")
        depends_on("py-pyobjc-framework-avfoundation@9.1:", when="@9.1:9.1.0")
        depends_on("py-pyobjc-framework-avfoundation@9.0.1:", when="@9.0.1:9.0")
        depends_on("py-pyobjc-framework-avfoundation@9:", when="@9:9.0.0")
        depends_on("py-pyobjc-framework-avfoundation@8.5.1:", when="@8.5.1:8")
        depends_on("py-pyobjc-framework-avfoundation@8.5:", when="@8.5:8.5.0")
    # END DEPENDENCIES

