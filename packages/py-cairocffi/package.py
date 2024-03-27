##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyCairocffi(PythonPackage):
    version("1.6.1", sha256="aa78ee52b9069d7475eeac457389b6275aa92111895d78fbaa2202a52dac112e", url="https://pypi.org/packages/17/be/a5d2c16317c6a890502725970589ae7f06cfc66b2e6916ba0a86973403c8/cairocffi-1.6.1-py3-none-any.whl")
    version("1.6.0", sha256="fec979f3e904c1a38350b06dcc91d3c15f9a4954e618a068761622e3a0d5058c", url="https://pypi.org/packages/9b/59/dcc2f8f719e1609fdddad7885649a9d3b9969317110e7dbd0b8040d5d473/cairocffi-1.6.0-py3-none-any.whl")
    version("1.5.1", sha256="071ab7b72e3533300b0bfd55a52056b4ffdc1ed6e656779e2aced9b709b8a295", url="https://pypi.org/packages/9f/d1/b26207d3a93dbdbee3b1492d59668f88953e9f28b74853e376a7a4f04e83/cairocffi-1.5.1.tar.gz")
    version("1.5.0", sha256="d105b49009d9b4970a459e38ff030cb5dfc8c8ee231e867d28f77ee9df44495e", url="https://pypi.org/packages/28/d6/59ed0aa7f642142db493744c909a59a45e7350277d8987ccfc56cc5244d9/cairocffi-1.5.0.tar.gz")
    version("1.4.0", sha256="509339b32ccd8d7b00c2204c32736cde78db53a32e6a162d312478d25626cd9a", url="https://pypi.org/packages/f4/10/82a8384882b4a7096256ee5c3fba65b6a0be67f08e8de130cd3627edb12f/cairocffi-1.4.0.tar.gz")
    version("1.3.0", sha256="ba505b4dd3a2ae41f6b5f2e1adc7d8560ae81b4b599d8641000db50bde0a68e5", url="https://pypi.org/packages/22/fa/0f9d14303fea27b0b0ae80a709b3c4ae29720457bfb372bc05ea31ae6df1/cairocffi-1.3.0-py3-none-any.whl")
    version("1.2.0", sha256="9a979b500c64c8179fec286f337e8fe644eca2f2cd05860ce0b62d25f22ea140", url="https://pypi.org/packages/84/ca/0bffed5116d21251469df200448667e90acaa5131edea869b44a3fbc73d0/cairocffi-1.2.0.tar.gz")
    version("1.1.0", sha256="f1c0c5878f74ac9ccb5d48b2601fcc75390c881ce476e79f4cfedd288b1b05db", url="https://pypi.org/packages/f7/99/b3a2c6393563ccbe081ffcceb359ec27a6227792c5169604c1bd8128031a/cairocffi-1.1.0.tar.gz")
    version("1.0.2", sha256="01ac51ae12c4324ca5809ce270f9dd1b67f5166fe63bd3e497e9ea3ca91946ff", url="https://pypi.org/packages/0f/0f/7e21b5ddd31b610e46a879c0d21e222dd0fef428c1fc86bbd2bd57fed8a7/cairocffi-1.0.2.tar.gz")
    version("1.0.1", sha256="9ca49d9bb0a52bd6a8263de137b4818e0889f3cd8d933165fb122669924ae3b9", url="https://pypi.org/packages/3e/f1/0d1dad825f6ec75d3d79d5673e7b836e7a23bf57fde0028fb8bf252d4259/cairocffi-1.0.1.tar.gz")

    with default_args(type="run"):
        depends_on("py-cffi@1.1:", when="@1:1.0.0,1.3,1.6:")

