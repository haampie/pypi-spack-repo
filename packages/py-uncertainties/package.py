##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyUncertainties(PythonPackage):
    version("3.1.7", sha256="4040ec64d298215531922a68fa1506dc6b1cb86cd7cca8eca848fcfe0f987151", url="https://pypi.org/packages/13/f7/9d94eeea3f6475456fb5c6b72d3a3cc652c1ecd342c5491274cbfc9ebaab/uncertainties-3.1.7-py2.py3-none-any.whl")
    version("3.1.6", sha256="cb4a66d5ceda006475ec845bf43ee8956c26138b08f93c41851c25a4ffe19a33", url="https://pypi.org/packages/4e/5c/33cbc5423d0a647b3ad7f93cdabb77b1b3eb5abbc3f2dadbd53b7ea4795f/uncertainties-3.1.6-py2.py3-none-any.whl")
    version("3.1.5", sha256="9c031773afa85e4bc8067f3be257c718eb7dbef7dffd604aeb315ded85c9c325", url="https://pypi.org/packages/45/41/fc7e7b73b603e7c2c9e040b7aa8caf4a88d74b6faa567601ed82b6f0d8e1/uncertainties-3.1.5-py2.py3-none-any.whl")
    version("3.1.4", sha256="342703c36eabf99251b35fbd30d748d6220451fc88f586924bdec91cfe6bc6c0", url="https://pypi.org/packages/b0/e0/fc200da8190729dcb685ae4877ed6936d31d64aeccb8cc355d9ec982681d/uncertainties-3.1.4-py2.py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-future", when="@3.1.4:")

