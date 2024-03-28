# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyDnspython(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("2.6.1", sha256="5ef3b9680161f6fa89daf8ad451b5f1a33b18ae8a1c6778cdf4b43f08c0a6e50", url="https://pypi.org/packages/87/a1/8c5287991ddb8d3e4662f71356d9656d91ab3a36618c3dd11b280df0d255/dnspython-2.6.1-py3-none-any.whl")
    version("2.6.0", sha256="44c40af3bffed66e3307cea9ab667fd583e138ecc0777b18f262a9dae034e5fa", url="https://pypi.org/packages/d2/e6/d44f13fcd60ea2533bd391a262cb79743ab4c1e11d9c6100067782e4f4ff/dnspython-2.6.0-py3-none-any.whl")
    version("2.5.0", sha256="6facdf76b73c742ccf2d07add296f178e629da60be23ce4b0a9c927b1e02c3a6", url="https://pypi.org/packages/b6/83/4a684a63d395007670bc95c1947c07045fe66141574e2f7e9e347df8499a/dnspython-2.5.0-py3-none-any.whl")
    version("2.4.2", sha256="57c6fbaaeaaf39c891292012060beb141791735dbb4004798328fc2c467402d8", url="https://pypi.org/packages/f6/b4/0a9bee52c50f226a3cbfb54263d02bb421c7f2adc136520729c2c689c1e5/dnspython-2.4.2-py3-none-any.whl")
    version("2.4.1", sha256="5b7488477388b8c0b70a8ce93b227c5603bc7b77f1565afe8e729c36c51447d7", url="https://pypi.org/packages/71/30/deee2ffb94194437c730a1c6230d9310ab5f73926a2549cdab91453616bb/dnspython-2.4.1-py3-none-any.whl")
    version("2.4.0", sha256="46b4052a55b56beea3a3bdd7b30295c292bd6827dd442348bc116f2d35b17f0a", url="https://pypi.org/packages/8f/a7/061a2659015c7e92e32270276dd61d0e21ec1c92a1599807c2d357f24d54/dnspython-2.4.0-py3-none-any.whl")
    version("2.3.0", sha256="89141536394f909066cabd112e3e1a37e4e654db00a25308b0f130bc3152eb46", url="https://pypi.org/packages/12/86/d305e87555430ff4630d729420d97dece3b16efcbf2b7d7e974d11b0d86c/dnspython-2.3.0-py3-none-any.whl")
    version("2.2.1", sha256="a851e51367fb93e9e1361732c1d60dab63eff98712e503ea7d92e6eccb109b4f", url="https://pypi.org/packages/9b/ed/28fb14146c7033ba0e89decd92a4fa16b0b69b84471e2deab3cc4337cc35/dnspython-2.2.1-py3-none-any.whl")
    version("2.2.0", sha256="081649da27ced5e75709a1ee542136eaba9842a0fe4c03da4fb0a3d3ed1f3c44", url="https://pypi.org/packages/90/ad/013786c1a6ffa9de70bcd852c8a40e8798e25d823ce8497d907e6cd450da/dnspython-2.2.0-py3-none-any.whl")
    version("2.1.0", sha256="95d12f6ef0317118d2a1a6fc49aac65ffec7eb8087474158f42f26a639135216", url="https://pypi.org/packages/f5/2d/ae9e172b4e5e72fa4b3cfc2517f38b602cc9ba31355f9669c502b4e9c458/dnspython-2.1.0-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-httpcore@0.17.3:", when="@2.4.0")
        depends_on("py-sniffio@1.1:", when="@2.4:2.4.0")
    # END DEPENDENCIES

