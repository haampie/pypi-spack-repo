# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyNvidiaDaliCuda110(PythonPackage):
    # BEGIN VERSIONS
    version("1.36.0", sha256="1373e2dfed77e3bd423afb3b3abd2ca42ed2ef6650addb44abf24a5b0cfe7a26", url="https://pypi.org/packages/f0/72/9b9cf635e77f52b4016ec705e7b73aaee1fffdc4700bb973d06614ae9a77/nvidia_dali_cuda110-1.36.0.tar.gz")
    version("1.19.0", sha256="cfa86cc019a362e355284f15021a4006c923af2520a21b563901f02a24ca4f65", url="https://pypi.org/packages/c3/15/6b536628dae6c55977e7e41837576cdfad19c1a95cecb70a4806e815bd6a/nvidia_dali_cuda110-1.19.0.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@:3.12", when="@1.36:")
        depends_on("python@:3.10", when="@1:1.19")
        depends_on("py-astunparse@1.6:", when="@1.36:")
        depends_on("py-dm-tree", when="@1.36:")
        depends_on("py-gast@0.3.3:", when="@1.36:")
        depends_on("py-nvidia-nvimgcodec-cu11", when="@1.36:")
    # END DEPENDENCIES

