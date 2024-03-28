# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkWebkit(PythonPackage):
    # BEGIN VERSIONS
    version("10.2", sha256="3717104dbc901a1bd46d97886c5adb6eb32798ff4451c4544e04740e41706083", url="https://pypi.org/packages/6f/76/1c7376b7f4a90095904b8f91a6db1aadde99066ffca999e6ffc1dd83830d/pyobjc-framework-WebKit-10.2.tar.gz")
    version("10.1", sha256="311974b626facee73cab5a7e53da4cc8966cbe60b606ba11fd0f3547e0ba1762", url="https://pypi.org/packages/9a/d9/32006ca1789fa4277fe685c559b344813d68e1dbc9e1782f2e85956bf0d4/pyobjc-framework-WebKit-10.1.tar.gz")
    version("10.0", sha256="847a69aeeb2e743c5ff838628f3a0031e538de4e011e29df52272955ed0b11df", url="https://pypi.org/packages/72/76/b20a65ed50468335880e962e3fc925d4df2ccd193c10bbb69d766c10af88/pyobjc-framework-WebKit-10.0.tar.gz")
    version("9.2", sha256="86761cba8c18c3d2ecbd3ca7ab8b92c8b2eae8514741ec63527b536b671ab296", url="https://pypi.org/packages/87/34/1a04b818bdefc2bf273038a8d83eeebf51301603c2f7df3b892d3533ed23/pyobjc-framework-WebKit-9.2.tar.gz")
    version("9.1.1", sha256="bc6ba0ca6ed9ebcb4c5fc338410a81f50b4da08e4bab4bfe5853612e8e5e79aa", url="https://pypi.org/packages/d9/50/9c23f6542b5418cdcd8c389f5d65e9a11b3983c6a9ec864a3c1ef9fd77b1/pyobjc-framework-WebKit-9.1.1.tar.gz")
    version("9.1", sha256="5bf1bb05ea3436b365cf1b36579fb2d3b5d1ac4aaf1689759edf62b00fd9160e", url="https://pypi.org/packages/e1/6a/bfea65fa819ad3230ebc9621295390555cf6b885f0c582e3c31136d623eb/pyobjc-framework-WebKit-9.1.tar.gz")
    version("9.0.1", sha256="82ed0cb273012b48f7489072d6e00579f42d54bc4543471c262db3e5c4bb9e87", url="https://pypi.org/packages/51/0b/2a81b67cade04e50ade902a512ed5bf7400f760753b58a464785c160205f/pyobjc-framework-WebKit-9.0.1.tar.gz")
    version("9.0", sha256="0624f3da6c55e425d20fcbb0f1ef08a421486bd9d0bb0f9fd14604b82133b36b", url="https://pypi.org/packages/b7/61/4e0ab0548a0313cd657a339885ada625a6b98f4daddce3e8514afd2eebb4/pyobjc-framework-WebKit-9.0.tar.gz")
    version("8.5.1", sha256="a6259c3dab67076359bb63f85cfaaf8dd1ba9d4a169c5d335070291629945312", url="https://pypi.org/packages/e7/07/585ce33b6946f9000ca4d1ca56cca2bae94541d167d26d7ce80da6595d42/pyobjc-framework-WebKit-8.5.1.tar.gz")
    version("8.5", sha256="b9c6d654be8a9be56abf72219b53ec40255ff77dcb610ab31d546632cccd740d", url="https://pypi.org/packages/46/0b/b41f7fe8dfed9adc4534a01b7c76c11787033df9654d02e1b7233710cdfa/pyobjc-framework-WebKit-8.5.tar.gz")
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

