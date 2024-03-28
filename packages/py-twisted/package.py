# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyTwisted(PythonPackage):
    # BEGIN VERSIONS
    version("24.3.0", sha256="039f2e6a49ab5108abd94de187fa92377abe5985c7a72d68d0ad266ba19eae63", url="https://pypi.org/packages/f8/f3/ff962a66ed957f4b51a669f25f6d0026a51dda1d25e3766a63d9a5aaf81e/twisted-24.3.0-py3-none-any.whl")
    version("23.10.0", sha256="4ae8bce12999a35f7fe6443e7f1893e6fe09588c8d2bed9c35cdce8ff2d5b444", url="https://pypi.org/packages/24/83/8d34d264c72d5450cd3d3ef31c885bb36b94635aa8e9e223581793d9d6c8/twisted-23.10.0-py3-none-any.whl")
    version("23.8.0", sha256="b8bdba145de120ffb36c20e6e071cce984e89fba798611ed0704216fb7f884cd", url="https://pypi.org/packages/2a/e3/9fe9cf016d32d050a2eec518c2f5156f7623b42e1ef3f2fa3e80c0ef654c/twisted-23.8.0-py3-none-any.whl")
    version("22.10.0", sha256="86c55f712cc5ab6f6d64e02503352464f0400f66d4f079096d744080afcccbd0", url="https://pypi.org/packages/ac/63/b5540d15dfeb7388fbe12fa55a902c118fd2b324be5430cdeac0c0439489/Twisted-22.10.0-py3-none-any.whl")
    version("22.8.0", sha256="8d4718d1e48dcc28933f8beb48dc71cfe77a125e37ad1eb7a3d0acc49baf6c99", url="https://pypi.org/packages/86/83/e066b4a37e184906ba76e5d3a54a20d893b13d2fac4b35ab5b2545096111/Twisted-22.8.0-py3-none-any.whl")
    version("22.4.0", sha256="f9f7a91f94932477a9fc3b169d57f54f96c6e74a23d78d9ce54039a7f48928a2", url="https://pypi.org/packages/db/99/38622ff95bb740bcc991f548eb46295bba62fcb6e907db1987c4d92edd09/Twisted-22.4.0-py3-none-any.whl")
    version("22.2.0", sha256="5c63c149eb6b8fe1e32a0215b1cef96fabdba04f705d8efb9174b1ccf5b49d49", url="https://pypi.org/packages/2b/ba/17bff991d6f1df1d123611ef2a0e72636ae400e7e75eddbe85b944567d0a/Twisted-22.2.0-py3-none-any.whl")
    version("22.1.0", sha256="ccd638110d9ccfdc003042aa3e1b6d6af272eaca45d36e083359560549e3e848", url="https://pypi.org/packages/7c/2b/df1c552adff67d9ec348295a76b6496178d6ca0dc6a033fd8ee681accdea/Twisted-22.1.0-py3-none-any.whl")
    version("21.7.0", sha256="13c1d1d2421ae556d91e81e66cf0d4f4e4e1e4a36a0486933bee4305c6a4fb9b", url="https://pypi.org/packages/b5/0c/7a1a943edce164c77c98f044175d801b572bb36936e9b4d5805a850525e7/Twisted-21.7.0-py3-none-any.whl")
    version("21.2.0", sha256="aab38085ea6cda5b378b519a0ec99986874921ee8881318626b0a3414bb2631e", url="https://pypi.org/packages/f2/16/3eb9c66a7bfb5220c7bcbaaac33d359fe8a157b028959cd210983749b2e0/Twisted-21.2.0-py3-none-any.whl")
    version("15.4.0", sha256="78862662fa9ae29654bc2b9d349c3f1d887e6b2ed978512c4442d53ea861f05c", url="https://pypi.org/packages/d1/d2/75b77dd5305141e274739c7a68e4116a4db4e459bfe33af3294acb24e908/Twisted-15.4.0.tar.bz2")
    version("15.3.0", sha256="025729751cf898842262375a40f70ae1d246daea88369eab9f6bb96e528bf285", url="https://pypi.org/packages/b7/c3/bf81048b2adb01de6907d8d039732aed17d6c69755fc4b59f0e4bc1641a6/Twisted-15.3.0.tar.bz2")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-attrs@21.3:", when="@23:")
        depends_on("py-attrs@19.2:", when="@21:21.2,21.7.0-rc3:22")
        depends_on("py-automat@0.8:", when="@21:21.2,21.7.0-rc3:")
        depends_on("py-constantly@15.1:", when="@18.4.0:18.4,18.7.0:18.7,21:21.2,21.7.0-rc3:")
        depends_on("py-hyperlink@17.1.1:", when="@18.4.0:18.4,18.7.0:18.7,21:21.2,21.7.0-rc3:")
        depends_on("py-incremental@22.10.0:", when="@23:")
        depends_on("py-incremental@21:", when="@21.7.0-rc3:22")
        depends_on("py-incremental@16.10.1:", when="@18.4.0:18.4,18.7.0:18.7,21:21.2")
        depends_on("py-pyhamcrest@1.9:", when="@18.7.0:18.7")
        depends_on("py-twisted-iocpsupport@1.0.2:", when="@22: platform=windows")
        depends_on("py-twisted-iocpsupport@1:", when="@21:21.2,21.7.0-rc3:21 platform=windows")
        depends_on("py-typing-extensions@4.2:", when="@23.10:")
        depends_on("py-typing-extensions@3.10:", when="@23:23.8")
        depends_on("py-typing-extensions@3.6.5:", when="@21.7.0-rc3:22")
        depends_on("py-zope-interface@5:", when="@23:")
        depends_on("py-zope-interface@4.4.2:", when="@18.4.0:18.4,18.7.0:18.7,21:21.2,21.7.0-rc3:22")
        depends_on("py-zope-interface@3.6:", when="@15.3,16.1.1:16.4.0")
    # END DEPENDENCIES

