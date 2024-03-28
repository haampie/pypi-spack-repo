# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyColoredlogs(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("15.0.1", sha256="612ee75c546f53e92e70049c9dbfcc18c935a2b9a53b66085ce9ef6a6e5c0934", url="https://pypi.org/packages/a7/06/3d6badcf13db419e25b07041d9c7b4a2c331d3f4e7134445ec5df57714cd/coloredlogs-15.0.1-py2.py3-none-any.whl")
    version("15.0", sha256="b7f630a8297a66984b6bae0f6a1b0e0afb9f2f6838ea3bfa58f50d3d13e133d6", url="https://pypi.org/packages/84/a6/837dbf6eac344cb74f0ba86b79e8180855570af3e26bcb1ea5f650cf944c/coloredlogs-15.0-py2.py3-none-any.whl")
    version("14.3", sha256="e244a892f9d97ffd2c60f15bf1d2582ef7f9ac0f848d132249004184785702b3", url="https://pypi.org/packages/f3/56/c11e7ef34316b22db4e6d1b9de6e54f332243b72ce63eab676f87744d5ad/coloredlogs-14.3-py2.py3-none-any.whl")
    version("14.2", sha256="4d31b0c9df42d09b24eedcecbbef39c1778c931e1b6f8a275895589d64d22c82", url="https://pypi.org/packages/44/89/d525b2836796e183332ba35e8eb611807dfb8bb858d065956e29f6c2b0af/coloredlogs-14.2-py2.py3-none-any.whl")
    version("14.1", sha256="0acbd320d93921bff11175b93967161af891ebd0d17e9fa5e4f4d07143857e17", url="https://pypi.org/packages/55/ac/87f10999fde56e0d6111a537116cf0fd9e5bed7ee863d30d7d4ce1685862/coloredlogs-14.1-py2.py3-none-any.whl")
    version("14.0", sha256="346f58aad6afd48444c2468618623638dadab76e4e70d5e10822676f2d32226a", url="https://pypi.org/packages/5c/2f/12747be360d6dea432e7b5dfae3419132cb008535cfe614af73b9ce2643b/coloredlogs-14.0-py2.py3-none-any.whl")
    version("12.0", sha256="5b4243294a1f26036a77e8db425595e59464f2c307cf82989ebe07e7bebd1c4f", url="https://pypi.org/packages/cb/47/99aa92cde3c1308195d87c335787a56045254100126ca1251dee19b9d89c/coloredlogs-12.0-py2.py3-none-any.whl")
    version("11.3", sha256="307e4ebd56970efddc887722724e2666bab766f59e9a656f072a9d1734d80657", url="https://pypi.org/packages/c3/41/8bdad684f4c207285e530091171f92a75f37a2af08e1f5cf516a7435c399/coloredlogs-11.3-py2.py3-none-any.whl")
    version("11.2", sha256="252f6282a029b90984a703504306d461e497875355201843abec77b5fcde97be", url="https://pypi.org/packages/9f/68/65862ffcb9e60ae9d7094775572b0826b10dee13a99771eb42bd6db10411/coloredlogs-11.2-py2.py3-none-any.whl")
    version("11.1", sha256="6590fea9bc0e47c543508e5bcc7231da8ba0b97a7cef1be5e99d74a4db11c063", url="https://pypi.org/packages/f9/98/be07b0e2a66b785c1f1e360654a4c1c4e35df31cc95475a3421647a86d2b/coloredlogs-11.1-py2.py3-none-any.whl")
    version("10.0", sha256="34fad2e342d5a559c31b6c889e8d14f97cb62c47d9a2ae7b5ed14ea10a79eff8", url="https://pypi.org/packages/08/0f/7877fc42fff0b9d70b6442df62d53b3868d3a6ad1b876bdb54335b30ff23/coloredlogs-10.0-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-colorama", when="@5.1.1:12 platform=windows")
        depends_on("py-humanfriendly@9.1:", when="@15:")
        depends_on("py-humanfriendly@7.1:", when="@14")
        depends_on("py-humanfriendly@6.1:", when="@11:12")
        depends_on("py-humanfriendly@4.7:", when="@9:10")
    # END DEPENDENCIES

