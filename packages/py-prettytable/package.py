# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPrettytable(PythonPackage):
    # BEGIN VERSIONS
    version("3.7.0", sha256="f4aaf2ed6e6062a82fd2e6e5289bbbe705ec2788fe401a3a1f62a1cea55526d2", url="https://pypi.org/packages/7a/cd/bec5850e23eb005c6fe30fe4c26bafd9a07b3d2524771f22a0fa01270078/prettytable-3.7.0-py3-none-any.whl")
    version("3.4.1", sha256="0d23ff81e165077d93367e1379d97893c7a51541483d25bad45b9647660ef06f", url="https://pypi.org/packages/5b/c9/4e7dbae5054c5bbaed9e7aa7a78e1ceff003d0b0699318e5d6993a0a10c9/prettytable-3.4.1-py3-none-any.whl")
    version("3.2.0", sha256="f6c5ec87c3ef9df5bba1d32d826c1b862ecad0344dddb6082e3562caf71fe085", url="https://pypi.org/packages/96/53/91638391af5a68d27402b920ccc3fdfae51dd3e333476b414393d4478a70/prettytable-3.2.0-py3-none-any.whl")
    version("2.4.0", sha256="2492f29e8686bdbcce815a568bff74cb71cbb704747c3abb9c9c6cfe25f985a2", url="https://pypi.org/packages/de/56/554603797416219cae8fd3eae33e5e2d58a7fc73419129b62fa419a67856/prettytable-2.4.0-py3-none-any.whl")
    version("2.2.1", sha256="09fb2c7f93e4f93e0235f05ae199ac3f16da3a251b2cfa1c7108b34ede298fa3", url="https://pypi.org/packages/e1/77/821a93d77111aee2525841b6116287f99eeefc482f4f28765fd8d7ef1c64/prettytable-2.2.1-py3-none-any.whl")
    version("0.7.2", sha256="a53da3b43d7a5c229b5e3ca2892ef982c46b7923b51e98f0db49956531211c4f", url="https://pypi.org/packages/23/4a/9785a37ed6425918af69909af715ced0fa261e518601a0c70309a708fd08/prettytable-0.7.2.zip")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-wcwidth", when="@1:")
    # END DEPENDENCIES

