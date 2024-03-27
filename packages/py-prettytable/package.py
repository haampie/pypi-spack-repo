##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPrettytable(PythonPackage):
    version("3.10.0", sha256="6536efaf0757fdaa7d22e78b3aac3b69ea1b7200538c2c6995d649365bddab92", url="https://pypi.org/packages/3d/c4/a32f4bf44faf95accbbd5d7864ddef9e289749a8efbc3adaad4a4671779a/prettytable-3.10.0-py3-none-any.whl")
    version("3.9.0", sha256="a71292ab7769a5de274b146b276ce938786f56c31cf7cea88b6f3775d82fe8c8", url="https://pypi.org/packages/4d/81/316b6a55a0d1f327d04cc7b0ba9d04058cb62de6c3a4d4b0df280cbe3b0b/prettytable-3.9.0-py3-none-any.whl")
    version("3.8.0", sha256="03481bca25ae0c28958c8cd6ac5165c159ce89f7ccde04d5c899b24b68bb13b7", url="https://pypi.org/packages/25/1e/4c284713b092ec384fad4399452f43f6446ad9aabc9c0b3c3c0920cc53b6/prettytable-3.8.0-py3-none-any.whl")
    version("3.7.0", sha256="f4aaf2ed6e6062a82fd2e6e5289bbbe705ec2788fe401a3a1f62a1cea55526d2", url="https://pypi.org/packages/7a/cd/bec5850e23eb005c6fe30fe4c26bafd9a07b3d2524771f22a0fa01270078/prettytable-3.7.0-py3-none-any.whl")
    version("3.6.0", sha256="3b767129491767a3a5108e6f305cbaa650f8020a7db5dfe994a2df7ef7bad0fe", url="https://pypi.org/packages/51/fd/52b6d8a28f8dabf05e5fcbb5ef639d62326a5bccfa93b98fb7e54d414509/prettytable-3.6.0-py3-none-any.whl")
    version("3.5.0", sha256="fe391c3b545800028edf5dbb6a5360893feb398367fcc1cf8d7a5b29ce5c59a1", url="https://pypi.org/packages/fa/4c/9b2bbb92a14a09ed929afa40282c088d8e50f79303eb3873fbeba1d96e89/prettytable-3.5.0-py3-none-any.whl")
    version("3.4.1", sha256="0d23ff81e165077d93367e1379d97893c7a51541483d25bad45b9647660ef06f", url="https://pypi.org/packages/5b/c9/4e7dbae5054c5bbaed9e7aa7a78e1ceff003d0b0699318e5d6993a0a10c9/prettytable-3.4.1-py3-none-any.whl")
    version("3.4.0", sha256="8ea12e615fee421090ca3954c2e006280f7ecdf4adf940dbc1c6ec014d4eca9d", url="https://pypi.org/packages/a7/b7/691a836347df9610c2264e7e60461f9991ca36ce9f2179a38ebc9e4a2682/prettytable-3.4.0-py3-none-any.whl")
    version("3.3.0", sha256="d1c34d72ea2c0ffd6ce5958e71c428eb21a3d40bf3133afe319b24aeed5af407", url="https://pypi.org/packages/5f/ab/64371af206988d7b15c8112c9c277b8eb4618397c01471e52b902a17f59c/prettytable-3.3.0-py3-none-any.whl")
    version("3.2.0", sha256="f6c5ec87c3ef9df5bba1d32d826c1b862ecad0344dddb6082e3562caf71fe085", url="https://pypi.org/packages/96/53/91638391af5a68d27402b920ccc3fdfae51dd3e333476b414393d4478a70/prettytable-3.2.0-py3-none-any.whl")
    version("2.5.0", sha256="1411c65d21dca9eaa505ba1d041bed75a6d629ae22f5109a923f4e719cfecba4", url="https://pypi.org/packages/9e/6d/40a24eaa03ea4418129708fd3f0f17eda73d568f16d4d4fd412566168b4c/prettytable-2.5.0-py3-none-any.whl")
    version("2.4.0", sha256="2492f29e8686bdbcce815a568bff74cb71cbb704747c3abb9c9c6cfe25f985a2", url="https://pypi.org/packages/de/56/554603797416219cae8fd3eae33e5e2d58a7fc73419129b62fa419a67856/prettytable-2.4.0-py3-none-any.whl")
    version("2.3.0", sha256="74ba6d10555c93e2d4697751744207f6baadf77010914b2bcd8d5b3b546f84de", url="https://pypi.org/packages/c2/98/3372c23c561cbaaa05bb60b2c3d30bfdad9ab504bf1ddefc7368b4545958/prettytable-2.3.0-py3-none-any.whl")
    version("2.2.1", sha256="09fb2c7f93e4f93e0235f05ae199ac3f16da3a251b2cfa1c7108b34ede298fa3", url="https://pypi.org/packages/e1/77/821a93d77111aee2525841b6116287f99eeefc482f4f28765fd8d7ef1c64/prettytable-2.2.1-py3-none-any.whl")
    version("0.7.2", sha256="a53da3b43d7a5c229b5e3ca2892ef982c46b7923b51e98f0db49956531211c4f", url="https://pypi.org/packages/23/4a/9785a37ed6425918af69909af715ced0fa261e518601a0c70309a708fd08/prettytable-0.7.2.zip")

    with default_args(type="run"):
        depends_on("py-wcwidth", when="@1:")

