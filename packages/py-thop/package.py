##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyThop(PythonPackage):
    version("0.1.1.post2209072238", sha256="01473c225231927d2ad718351f78ebf7cffe6af3bed464c4f1ba1ef0f7cdda27", url="https://pypi.org/packages/bb/0f/72beeab4ff5221dc47127c80f8834b4bcd0cb36f6ba91c0b1d04a1233403/thop-0.1.1.post2209072238-py3-none-any.whl")
    version("0.1.1.post2207130030", sha256="13517320470e751ba56b59788c902f189640e83b9f0a46f5736c9a928dd4e280", url="https://pypi.org/packages/15/d3/b2c788a51c55a26f3785625128285baf9461078a6a5c03836d9c6c7477c5/thop-0.1.1.post2207130030-py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-torch", when="@:0.0.5,0.0.22.post:0.0.31.post2005141830,0.1:")

