# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkContacts(PythonPackage):
    # BEGIN VERSIONS
    version("10.2", sha256="5a9de975f41c7dac3c219b4c60cd08b8ba385685db7997c8622f19e0a43e6857", url="https://pypi.org/packages/1c/20/7428cf84dbae9cf8ae6d44cb88cb7711ba94ed0a98123d8e1f2a30d3d857/pyobjc-framework-Contacts-10.2.tar.gz")
    version("10.1", sha256="949d61ff7f4f07956949f8945ad627ffa89cce3d10af9442591e519791a25cc4", url="https://pypi.org/packages/2c/a0/84e78fad871e5951d4f3233c519dcf38134cc58d06e5644cb046217839c5/pyobjc-framework-Contacts-10.1.tar.gz")
    version("10.0", sha256="7130d83be467c4bb877716a73b2e1a7768f19f2c43bf3bbff2d9ae412008d4a8", url="https://pypi.org/packages/1b/ed/10028928b6e86405388760ee366663e776a76cc074c3b33bb5847f7ebdf9/pyobjc-framework-Contacts-10.0.tar.gz")
    version("9.2", sha256="1e5ae6a612cae95c010eb5ccf6c2d70a97faf25c7d62b4146fc51424d7fc4b60", url="https://pypi.org/packages/b6/e0/3af081a26f545c39e79101653f80047965266ab9ccc8b432130801a00dc7/pyobjc-framework-Contacts-9.2.tar.gz")
    version("9.1.1", sha256="1ef8547fefe97bffd898c5768cb51a42ab13829443fd3e1fac8cfdf2c435bd83", url="https://pypi.org/packages/a6/1b/904de0e08662feced99708d182bee760a807845e308430f7e844747bc2cd/pyobjc-framework-Contacts-9.1.1.tar.gz")
    version("9.1", sha256="bf1c87595508ff503bcf06126f37047e20b0b460938d828114ab25de3148fa76", url="https://pypi.org/packages/9b/49/452987ee757c018b686b9c5cdcd4bde3fdc130b4a59d9cc14ad645ad4d80/pyobjc-framework-Contacts-9.1.tar.gz")
    version("9.0.1", sha256="b58f12b9b42b1c33215ebb90663b8e44d53001f2c169e889008ddc715b349e5f", url="https://pypi.org/packages/6b/22/857efaf972a562313525279e01bb4e41f18be90a3958b796aee9646c4446/pyobjc-framework-Contacts-9.0.1.tar.gz")
    version("9.0", sha256="3c16f586ecd73387c5c3628521fd4d3f579ab6a053e7eb5fbd801ba2a7b97192", url="https://pypi.org/packages/f2/06/2daa00129a3e7bee6407f2cf71bef3b42ab5ee6071103499d3269882e3b2/pyobjc-framework-Contacts-9.0.tar.gz")
    version("8.5.1", sha256="0717049d3789436d830fed907d6e3b239df8f9cd7e1e4d86dd3d205479e61ced", url="https://pypi.org/packages/49/e8/dd96df3ec328ba018d2564ad6e70f7612353584fa5478f0060c0f6f83e7d/pyobjc-framework-Contacts-8.5.1.tar.gz")
    version("8.5", sha256="2f82b3986582f7a5417579d2c3ed52aeeb5ab7f364ac527a664c762e8ca2c855", url="https://pypi.org/packages/d3/c1/af84467271b91fd1c0d16772b11f7e4f4cd6db4f4f1e236ab45a6f124a36/pyobjc-framework-Contacts-8.5.tar.gz")
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

