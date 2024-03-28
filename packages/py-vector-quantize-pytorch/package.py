# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyVectorQuantizePytorch(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.3.9", sha256="524f5a8cdad54b039ebc86320bef3dc2da633100af34e70bea1ddf09458bcfa2", url="https://pypi.org/packages/f4/e3/4fddac6653e017ce643448beb8a2af4a437ecd58aa663f859d065b2a8e00/vector_quantize_pytorch-0.3.9-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-einops", when="@0.3:1.0.2")
        depends_on("py-torch", when="@0.2:")
    # END DEPENDENCIES

