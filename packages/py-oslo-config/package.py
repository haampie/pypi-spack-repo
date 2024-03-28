# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyOsloConfig(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("9.4.0", sha256="8c2049c14cade7adeeda18638531b3b3a40d3c6bcc690535939f64a3c1ec8d63", url="https://pypi.org/packages/9c/82/792303dce5cd50951d27a405ad8251c04dc3ad5a051b6a585a939ae39f4a/oslo.config-9.4.0-py3-none-any.whl")
    version("9.3.0", sha256="5642e75ab8070aee96563670b1c1ee3b6f3cac3c0302fe7fc78973cd4b4e3d29", url="https://pypi.org/packages/0a/d9/f0dd9d239c4c430fde9699e3ca899bb66d62a439f87564ef283a8a4820c7/oslo.config-9.3.0-py3-none-any.whl")
    version("9.2.0", sha256="b98e50b19161fc76f25905ff74043e239258a3ebe799a5f9070d285e3c039dee", url="https://pypi.org/packages/4a/da/08d7bd84a1e9d9230f3a37b13519710464702b8b9659130914d195c671ae/oslo.config-9.2.0-py3-none-any.whl")
    version("9.1.1", sha256="7cd56e0b41b04f64dbc42e83e8164d5ef03466390f1216fbda2cb0e1c535c22c", url="https://pypi.org/packages/ce/15/97fb14b7a1692693610a8e00e2a08e4186d6cdd875b6ac24c912a429b665/oslo.config-9.1.1-py3-none-any.whl")
    version("9.1.0", sha256="0a314e72b2ce56cce03049631c72358ee30c8a7c218e022b3faecda0ebe59a34", url="https://pypi.org/packages/ad/e3/6dc96283be00581a6395938a7b8cb7cf913580cb1cbaff00a473c38a8017/oslo.config-9.1.0-py3-none-any.whl")
    version("9.0.0", sha256="f876bf759f186c854c71417b83b44ba68d69b11ed3a79c324c7737a0bfc962f1", url="https://pypi.org/packages/41/ff/3ae26b2ca2957d82d39ceb5765af88953f5899e534923a0f87ea6201f604/oslo.config-9.0.0-py3-none-any.whl")
    version("8.8.1", sha256="643130555aa66c316d6972a2530087ca8b7f8c42ed25826815536dfa5e1e12eb", url="https://pypi.org/packages/c6/e0/2f61454d706d8c679d4907559b8961d1d7d018cddcc2de237ff362d784e7/oslo.config-8.8.1-py3-none-any.whl")
    version("8.8.0", sha256="b1e2a398450ea35a8e5630d8b23057b8939838c4433cd25a20cc3a36d5df9e3b", url="https://pypi.org/packages/c5/4c/6cfd9274f3fb665f276ec41bd7c98fce20d5ec903bac7b4cd2c30f5832fe/oslo.config-8.8.0-py3-none-any.whl")
    version("8.7.1", sha256="3c5cc681ef106a4573d677510f907ab48f40004dc3aac2298d9a517559491efb", url="https://pypi.org/packages/35/3a/62f4f3e724151d78b97608b8c72a285decdaa91ac2073946381ef042ebb1/oslo.config-8.7.1-py3-none-any.whl")
    version("8.7.0", sha256="5b1b9439bfb76e0091172aee77b509144f22e08127ddee4d10a7eb5407740b07", url="https://pypi.org/packages/59/3b/4178dff77c9e2fa4e0ad589eb6cc704fb620693d15759c4a4a41c4c253ee/oslo.config-8.7.0-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-debtcollector@1.2:", when="@3.6:")
        depends_on("py-netaddr@0.7.18:", when="@4.13:")
        depends_on("py-oslo-i18n@3.15.3:", when="@4.13:")
        depends_on("py-pyyaml@5.1:", when="@8.5:")
        depends_on("py-requests@2.18:", when="@6.4:")
        depends_on("py-rfc3986@1.2:", when="@6.8:")
        depends_on("py-stevedore@1.20:", when="@3.23:")
    # END DEPENDENCIES

