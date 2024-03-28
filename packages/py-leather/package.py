# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyLeather(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.4.0", sha256="18290bc93749ae39039af5e31e871fcfad74d26c4c3ea28ea4f681f4571b3a2b", url="https://pypi.org/packages/a1/30/9ec597c962c5249ebd5c580386e4b5f2884cd943af42634291ee3b406415/leather-0.4.0-py2.py3-none-any.whl")
    version("0.3.4", sha256="5e741daee96e9f1e9e06081b8c8a10c4ac199301a0564cdd99b09df15b4603d2", url="https://pypi.org/packages/eb/44/44da0f7c2a23b9fc38e2693ac86926375937880acfdb44307a3ccf762b68/leather-0.3.4-py2.py3-none-any.whl")
    version("0.3.3", sha256="e0bb36a6d5f59fbf3c1a6e75e7c8bee29e67f06f5b48c0134407dde612eba5e2", url="https://pypi.org/packages/45/f4/692a53df6708caca1c6d088c6d9003940f164f98bd9df2bdc86233641e9c/leather-0.3.3-py3-none-any.whl")
    version("0.3.2", sha256="2ab311449434a6391f89469cc32f6482299dcdc4e4d6a7bf8c790aece796afcd", url="https://pypi.org/packages/96/1a/027bb1c4f49fb6cf1ca34dc873e79390939b097222bf6d45d387de444f0e/leather-0.3.2-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-six@1.6.1:", when="@0.3.4:0.3")
    # END DEPENDENCIES

