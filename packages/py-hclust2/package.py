# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyHclust2(PythonPackage):
    # BEGIN VERSIONS
    version("1.0.0", sha256="9667f1d16628940aedd3d1d571b956a6f77795018e3ea4dd83f234419eb0096d", url="https://pypi.org/packages/75/c8/91024c40f51224711e8e0eba7d5df3bfae698530f0d2a283b7d2d35b1f9e/hclust2-1.0.0.tar.gz")
    version("0.99", sha256="39de3c2bee3c380dfc0a9d0dfd5fc353893c4e1097f6d0609c43542b7dd6541c", url="https://pypi.org/packages/cb/83/0e9d0dabd44459d2a59985ea5e68094da4da147a8eb8e7466bcd7fa2a53a/hclust2-0.99-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-matplotlib", when="@:0")
        depends_on("py-numpy", when="@:0")
        depends_on("py-pandas", when="@:0")
        depends_on("py-scipy", when="@:0")
    # END DEPENDENCIES

