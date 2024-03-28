# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyOsloUtils(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("7.1.0", sha256="1d6504526c33cc10ae2c72565d0446a82d2acd43eaa5e6f3fd901d78400a2da0", url="https://pypi.org/packages/f0/bb/d61363eae3418f7862a2d14f96b803d5c395237a929e7fe35e5a1a4b0e23/oslo.utils-7.1.0-py3-none-any.whl")
    version("7.0.0", sha256="dbb724041a2ea0c342d524c4d7c7f07c8bc5016f4762d38c6a41b2ef805b3a8e", url="https://pypi.org/packages/87/98/a105b1e55d81ad791703786281d4dc48c301255b2d251f925cbc395a0ab4/oslo.utils-7.0.0-py3-none-any.whl")
    version("6.3.0", sha256="6bac2e56650f502caae6c0e8ba6e5eda3d7a16743d115f8836cad54538dd667f", url="https://pypi.org/packages/cf/ef/741be3e7f64774c5fdf0370e8937e9d5e3374aa4683208a34734fb04c8dc/oslo.utils-6.3.0-py3-none-any.whl")
    version("6.2.1", sha256="46718f7a0071422af4748cc4615f4189486e5752f9a12057f53d9025672f4974", url="https://pypi.org/packages/5f/b5/8dde38e597e4b00bbf080fd8c1c27f9fd7704f49f1904f0b48e5e7d8ef31/oslo.utils-6.2.1-py3-none-any.whl")
    version("6.2.0", sha256="30ba9fd431be468cd17b5d7c1a0ae6d63bb63aaaf97bf590123f13c6d95254a3", url="https://pypi.org/packages/f8/cf/a8edcd5cfef1b0368370121d112c65cf2f652ee3f7a113a0d2ad9f32f7fc/oslo.utils-6.2.0-py3-none-any.whl")
    version("6.1.0", sha256="b34648b1eb311dc3461e84a3bb75ed677fb0a49024def708057881e51759d5d6", url="https://pypi.org/packages/7a/09/0853c0a1b2c803055bdc9d68a84b6216eca53111f667d6e928b928dac8a5/oslo.utils-6.1.0-py3-none-any.whl")
    version("6.0.2", sha256="925862abbeed6a199b6eef47d02bbd56a411d0e296d2f52a88e3400b467d2ed0", url="https://pypi.org/packages/08/8a/56853efe447f96574d9e1003458a8e8bee26c119f1606e943dcb3c047d02/oslo.utils-6.0.2-py3-none-any.whl")
    version("6.0.1", sha256="5ae4179cfad4396098ca9f14afe21e4d088e25a1a8f0db45559d8a4d767a052d", url="https://pypi.org/packages/1f/92/8f011f61fa186d4de159d97fed69fd2d1a27cef4e745177399b3b49e6a65/oslo.utils-6.0.1-py3-none-any.whl")
    version("6.0.0", sha256="36b34f0d609bce50b48b0af8d78200f8083171d90f18ee7c1b929f93e36d1e43", url="https://pypi.org/packages/d5/79/95a080ea46002f92e4b196b859ac879c830c62ef238ac123011f7b29ddf5/oslo.utils-6.0.0-py3-none-any.whl")
    version("5.0.0", sha256="f964ef290f1d43aa6daafdcf3c32f55332f38e878f0e2649edcaf8384f455d57", url="https://pypi.org/packages/c7/52/567fc48611230cff7022a11e239ad82e9cc0d80d42aaf76fe94367b1fe87/oslo.utils-5.0.0-py3-none-any.whl")
    version("4.9.2", sha256="ff38bc69bbed11103ceb5d06ac47454fe439ee9351ed2640d47c1b2cc71b2ea5", url="https://pypi.org/packages/0e/28/2acc0e9726c8eff4c9539d3dbf3cb4845e9eb5bc99f26002510e13d7f6f8/oslo.utils-4.9.2-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-debtcollector@1.2:", when="@3.5:")
        depends_on("py-iso8601@0.1.11:", when="@3.10:")
        depends_on("py-netaddr@0.7.18:", when="@3.30:")
        depends_on("py-netifaces@0.10.4:", when="@1.1.1:1.4.0,1.4.2:3.0,3.2:")
        depends_on("py-oslo-i18n@3.15.3:", when="@3.30:")
        depends_on("py-packaging@20.4:", when="@4.3:")
        depends_on("py-pbr@2:2.0,3:", when="@3.25.1:5")
        depends_on("py-pyparsing@2.1:", when="@3.22.1:")
        depends_on("py-pytz@2013.6:", when="@7.1: ^python@:3.8")
        depends_on("py-pytz@2013.6:", when="@1.6:7.0")
        depends_on("py-pyyaml@3.13:", when="@6.3:")
        depends_on("py-tzdata@2022.4:", when="@7.1: ^python@3.9:")
        depends_on("py-tzdata@2022.4:", when="@6.2:7.0")
    # END DEPENDENCIES

