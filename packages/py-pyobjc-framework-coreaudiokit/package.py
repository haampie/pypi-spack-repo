# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkCoreaudiokit(PythonPackage):
    # BEGIN VERSIONS
    version("10.2", sha256="38dfafba8eddb655aac352a967c0e713a90e10a4dd40d4ea1abbb4db01c5d33f", url="https://pypi.org/packages/ef/6d/c6fe61ee094ad062eaa04ae12cd5ced4fbdb34b233f12b71eccaaaea7c10/pyobjc-framework-CoreAudioKit-10.2.tar.gz")
    version("10.1", sha256="85472aaee6360940f679a5e068b5a21160f8cee676d9fd0937b43b39c447d78e", url="https://pypi.org/packages/9e/eb/7ca8afd7b31741c44ee9181d184d2edcd6a1714c18682fc3fb2a05462259/pyobjc-framework-CoreAudioKit-10.1.tar.gz")
    version("10.0", sha256="0e604b47fb04303399d6cdeda5e83c0fed53ee61348052d44321ffbe898b08dc", url="https://pypi.org/packages/3d/02/528230c69e35ded84de3e946d72d720d519d4a9693cbbd6d44e8b50e112c/pyobjc-framework-CoreAudioKit-10.0.tar.gz")
    version("9.2", sha256="4d1a3a1612709ffa6a1f5e9c57e3c4c7e42d54e0d9b40c2038a97ca4821690e1", url="https://pypi.org/packages/bc/6a/e08990f4b2dea5acb4bac3a153beb4a0db4944ef39b52447a2c70496a280/pyobjc-framework-CoreAudioKit-9.2.tar.gz")
    version("9.1.1", sha256="93bb29195ef5312ec21f200d758459faacc41fd807bc9ad80a8f49cec6747846", url="https://pypi.org/packages/e6/47/48c55111cef93cf4503ba09016c6c252eb9e3546b4c9a2b3ab845fd1697c/pyobjc-framework-CoreAudioKit-9.1.1.tar.gz")
    version("9.1", sha256="003aab8dfbab4764aa75511c502664992d81d4c28b76012018eabe217aebe859", url="https://pypi.org/packages/e1/51/4f46df2cda604350c2b526f1ffc2841f704f8de481f748cf3cb2574c23e6/pyobjc-framework-CoreAudioKit-9.1.tar.gz")
    version("9.0.1", sha256="61a39f00e25214486be432fd31eb2b9d8e54da9a1361b9b3a1025201876417ef", url="https://pypi.org/packages/23/b2/255a0c61c3d78b8fc2efa3f022b8c2dcb2acce41c117ce5c7e5bf564419b/pyobjc-framework-CoreAudioKit-9.0.1.tar.gz")
    version("9.0", sha256="9f614f8876dcff678ef67e15d377494d420e2abedcaff511c2454944067b5e39", url="https://pypi.org/packages/31/0c/b556cfed7bbb5d958be9190b42ceed20346bf49f2f7e423825a27d08955c/pyobjc-framework-CoreAudioKit-9.0.tar.gz")
    version("8.5.1", sha256="c68e45265c8fc0e03b87f0fd733b0def6a186062db0e537509f0caef2336e179", url="https://pypi.org/packages/f3/43/cebd40132dfc9f57afed92dbc7d5f5289c133de076d842fda701fda0200c/pyobjc-framework-CoreAudioKit-8.5.1.tar.gz")
    version("8.5", sha256="4134ae64aaa3bf40df4a65e0f3ce0499a540aee457722f9ff135b1c083f5a2d6", url="https://pypi.org/packages/6a/9a/eb1973aa58a0340d82d67ffd5d0015e14c23f75690dd9dca7cf82aebeabc/pyobjc-framework-CoreAudioKit-8.5.tar.gz")
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
    # END DEPENDENCIES

