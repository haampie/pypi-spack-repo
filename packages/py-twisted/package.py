##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyTwisted(PythonPackage):
    version("21.7.0", sha256="13c1d1d2421ae556d91e81e66cf0d4f4e4e1e4a36a0486933bee4305c6a4fb9b", url="https://pypi.org/packages/b5/0c/7a1a943edce164c77c98f044175d801b572bb36936e9b4d5805a850525e7/Twisted-21.7.0-py3-none-any.whl")
    version("15.4.0", sha256="78862662fa9ae29654bc2b9d349c3f1d887e6b2ed978512c4442d53ea861f05c", url="https://pypi.org/packages/d1/d2/75b77dd5305141e274739c7a68e4116a4db4e459bfe33af3294acb24e908/Twisted-15.4.0.tar.bz2")
    version("15.3.0", sha256="025729751cf898842262375a40f70ae1d246daea88369eab9f6bb96e528bf285", url="https://pypi.org/packages/b7/c3/bf81048b2adb01de6907d8d039732aed17d6c69755fc4b59f0e4bc1641a6/Twisted-15.3.0.tar.bz2")

    with default_args(type="run"):
        depends_on("py-attrs@19.2:", when="@21:21.2,21.7.0-rc3:22")
        depends_on("py-automat@0.8:", when="@21:21.2,21.7.0-rc3:")
        depends_on("py-constantly@15.1:", when="@18.4.0:18.4,18.7.0:18.7,21:21.2,21.7.0-rc3:")
        depends_on("py-hyperlink@17.1.1:", when="@18.4.0:18.4,18.7.0:18.7,21:21.2,21.7.0-rc3:")
        depends_on("py-incremental@21:", when="@21.7.0-rc3:22")
        depends_on("py-pyhamcrest@1.9:", when="@18.7.0:18.7")
        depends_on("py-twisted-iocpsupport@1:", when="@21:21.2,21.7.0-rc3:21 platform=windows")
        depends_on("py-typing-extensions@3.6.5:", when="@21.7.0-rc3:22")
        depends_on("py-zope-interface@4.4.2:", when="@18.4.0:18.4,18.7.0:18.7,21:21.2,21.7.0-rc3:22")
        depends_on("py-zope-interface@3.6:", when="@15.3,16.1.1:16.4.0")

