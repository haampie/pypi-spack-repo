# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyThop(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.1.1.post2209072238", sha256="01473c225231927d2ad718351f78ebf7cffe6af3bed464c4f1ba1ef0f7cdda27", url="https://pypi.org/packages/bb/0f/72beeab4ff5221dc47127c80f8834b4bcd0cb36f6ba91c0b1d04a1233403/thop-0.1.1.post2209072238-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-torch", when="@:0.0.31.post2005141830,0.1:")
    # END DEPENDENCIES

