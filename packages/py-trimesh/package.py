##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyTrimesh(PythonPackage):
    version("3.17.1", sha256="a09460ee4e11c32bf9f0643b86241b3e3e2aa86296c4912a0738b76da3034c00", url="https://pypi.org/packages/0e/99/435e48279823f0a833cdbb508b25e1e659af51ed3a1ec2b05551e1dd139a/trimesh-3.17.1-py3-none-any.whl")
    version("2.38.10", sha256="866e73ea35641ff2af73867c891d7f9b90c75ccb8a3c1e8e06e16ff9af1f8c64", url="https://pypi.org/packages/1e/5d/add451660f0f444aeb2b38daa73f336d10b40bc97af164e98f58581c60d6/trimesh-2.38.10.tar.gz")

    with default_args(type="run"):
        depends_on("py-numpy", when="@3.6.2:")
        depends_on("py-setuptools", when="@3.6.2:3.9")

