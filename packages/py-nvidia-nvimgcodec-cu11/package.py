##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyNvidiaNvimgcodecCu11(PythonPackage):
    version("0.2.0.7", sha256="909f96878561f6cfe0099f6cc26c57f3295de2ebfd0334022e0b29aab75e250b", url="https://pypi.org/packages/c8/9f/1cdcefbc5f916440b4ed92a7141914cc45da154ffa9c9ae9c5fa0e6359f2/nvidia_nvimgcodec_cu11-0.2.0.7-py3-none-manylinux2014_aarch64.whl")

    with default_args(type="run"):
        depends_on("python@:3.12.0")

