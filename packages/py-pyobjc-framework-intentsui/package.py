# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkIntentsui(PythonPackage):
    # BEGIN VERSIONS
    version("10.2", sha256="4b9ca6f868b6cb7945ef4c285e73d220433efc35dfcad6b4a356bfce55e96c09", url="https://pypi.org/packages/af/ae/5f671f2906d4fcfaf9955bad758e7b29278fb3c5f91a65fd78548c5ece74/pyobjc-framework-IntentsUI-10.2.tar.gz")
    version("10.1", sha256="01948fbd8f956a79d3c2e27f75bc9954ad12cb4113982f58654122cfa8095ebb", url="https://pypi.org/packages/73/d9/a2dde732d4d25beef0677d41d6451f42266ae753f7f6964ab5f54121d125/pyobjc-framework-IntentsUI-10.1.tar.gz")
    version("10.0", sha256="27dbc84df229700c8e187ba9bfc089fe7dea63cfa20ee7e3c3f09c9f8b8c37d0", url="https://pypi.org/packages/1f/04/46186a9be93c413863dcfde86003262f65abdd8840d339037c2732c9a504/pyobjc-framework-IntentsUI-10.0.tar.gz")
    version("9.2", sha256="a6c1816e385ece9c6f540125beacb645c284169bd0d3489e3ec0f7023d6e5c64", url="https://pypi.org/packages/8c/af/60f40541feb5f7b6ab641247a2f9321620eafb0e9987c5763cd0a6c3ee7d/pyobjc-framework-IntentsUI-9.2.tar.gz")
    version("9.1.1", sha256="39b5b5485dd6391bafaa0bf8481a3a18bb7d626e899c8f71c4acdc319f3ca5fe", url="https://pypi.org/packages/84/fd/157b145f9acc4b788a9e90588478477dc553547695555d00d6375948fa40/pyobjc-framework-IntentsUI-9.1.1.tar.gz")
    version("9.1", sha256="178f4dc45669b0bb4afaec16b9f3f907131947282757cc675fc6b930410dde43", url="https://pypi.org/packages/63/08/b129d540832ed90b677805788ecc4d292a3cf539e253293de8ec465e0f41/pyobjc-framework-IntentsUI-9.1.tar.gz")
    version("9.0.1", sha256="f25a4eb6afa8d7c33450a6e718576178d23af00bad522ca20554bd869bc35038", url="https://pypi.org/packages/87/77/1f20cdff9f7fa2c7a8df8b927d9ed159872b3f959583aacf84a2d51acd7a/pyobjc-framework-IntentsUI-9.0.1.tar.gz")
    version("9.0", sha256="52751678e93b68c900d34751a0677bbd90241faf1138a74d079212ae41037fd0", url="https://pypi.org/packages/31/22/32147adb5c3bd46424c019d9e33f8c6548ffea0a8b8a9be24ea6a6d83a52/pyobjc-framework-IntentsUI-9.0.tar.gz")
    version("8.5.1", sha256="895e4bd9401640cb948323e9ccee21327e93a471d7e2c9b4ebabd6255ef02ea6", url="https://pypi.org/packages/d2/8f/f71e3d3727f6841ddbfaadb93c7e546f851fc1e7a8e1ab1b34445e65226c/pyobjc-framework-IntentsUI-8.5.1.tar.gz")
    version("8.5", sha256="402ab099d20979d1b739dcc29a88e5c07c1fcfcbdc5706eb8f6958f8b2e0f653", url="https://pypi.org/packages/61/b4/023528fed005688ba35ddbdf34132bcda51e82dbdb1d8d8e612a9de571e8/pyobjc-framework-IntentsUI-8.5.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-pyobjc-core@10.2:", when="@10.2:")
        depends_on("py-pyobjc-core@10.1:", when="@10.1")
        depends_on("py-pyobjc-core@10:", when="@10:10.0")
        depends_on("py-pyobjc-framework-intents@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-intents@10.1:", when="@10.1")
        depends_on("py-pyobjc-framework-intents@10:", when="@10:10.0")
    # END DEPENDENCIES

