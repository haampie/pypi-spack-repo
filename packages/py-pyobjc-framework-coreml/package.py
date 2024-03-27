##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkCoreml(PythonPackage):
    version("10.2", sha256="a1d7743a91160d096ccd3f5f5d824dafdd6b99d0c4342e8c18852333c9b3318e", url="https://pypi.org/packages/69/99/42c8a299a5b936eadac2c80429991194720514805950c8a13161d4d9df0b/pyobjc-framework-CoreML-10.2.tar.gz")
    version("10.1", sha256="4cda220d5ad5b677a95d4d29256b076b411b692b64219c2dcb81c702fc34d57d", url="https://pypi.org/packages/16/36/1c9e980b141062c046908fb7ff74999aff9497a26eb355332ce62d980873/pyobjc-framework-CoreML-10.1.tar.gz")
    version("10.0", sha256="11b70aaa34d45b2a325231ddc571686b8e5c6404b74eb647c84c0cb2cf51052a", url="https://pypi.org/packages/fe/d2/9a4eb76cbbe677f6be42cef386eb7eb49a2529218f5acbf1a1275fe9e07b/pyobjc-framework-CoreML-10.0.tar.gz")
    version("9.2", sha256="b6d66824ab248a648a98e6f6d3151756e98c9d85ebe5d2a8a3650af5a5e88c5c", url="https://pypi.org/packages/3b/d3/e60f81465d3194eb6f311d415754ca90cd09ff7bcc5ebbacccc7b1cc6bf3/pyobjc-framework-CoreML-9.2.tar.gz")
    version("9.1.1", sha256="93f7682d539b52e60f9309aa26d8a9680a0c589f2bef4de5b3eee26d27934349", url="https://pypi.org/packages/b6/ca/5cee6bcb5ff5d835fd437bbd1ae8554d0f20be6bb273ae06f77a877902c8/pyobjc-framework-CoreML-9.1.1.tar.gz")
    version("9.1", sha256="966751918edd752b9977d9d1729602e7145294033b53c6cb47f368a1aeda8cf4", url="https://pypi.org/packages/d9/75/7e1ff49667f2f0027720847eeb373b483ee29d9863d52b89c3763a700390/pyobjc-framework-CoreML-9.1.tar.gz")
    version("9.0.1", sha256="216731388c85a2d8d00b6d9045e4637b5375c8777fe59795edd8e91a0cb2c4aa", url="https://pypi.org/packages/6b/44/09103a813f1d8e66595435cf703b9f6826c9317f0df82df076f3b9b25475/pyobjc-framework-CoreML-9.0.1.tar.gz")
    version("9.0", sha256="db89c9ee5e32b80be481e7b48a0fd1dccec7184ace62a1eeaaceb621fadc11de", url="https://pypi.org/packages/9a/c4/b6e1b6203915965dfd7a16d3631b92f92fd09257c256d37b2a3331cdb5b2/pyobjc-framework-CoreML-9.0.tar.gz")
    version("8.5.1", sha256="8840c3cb2be40d7d5ab63b418919afbfc73a4a01661814e9f967e9e072b797dd", url="https://pypi.org/packages/5c/61/5df3c3d26da7e15b832f2bf1dc38c64c7f8163df740835066e00e7ca3608/pyobjc-framework-CoreML-8.5.1.tar.gz")
    version("8.5", sha256="9da426d5df78cc232a4ed5d8e5d2b36d2dfd8d5c3cc1cdd92159afa4901f4136", url="https://pypi.org/packages/b6/ec/24aeb037c655d9e5cd5147bea61e7d9ea05d9c5793ca2bfe5fe8685a7b38/pyobjc-framework-CoreML-8.5.tar.gz")

    with default_args(type="run"):
        depends_on("py-pyobjc-core@10.2:", when="@10.2:")
        depends_on("py-pyobjc-core@10.1:", when="@10.1")
        depends_on("py-pyobjc-core@10:", when="@10:10.0")
        depends_on("py-pyobjc-framework-cocoa@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-cocoa@10.1:", when="@10.1")
        depends_on("py-pyobjc-framework-cocoa@10:", when="@10:10.0")

