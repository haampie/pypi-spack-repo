##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyLeather(PythonPackage):
    version("0.4.0", sha256="18290bc93749ae39039af5e31e871fcfad74d26c4c3ea28ea4f681f4571b3a2b", url="https://pypi.org/packages/a1/30/9ec597c962c5249ebd5c580386e4b5f2884cd943af42634291ee3b406415/leather-0.4.0-py2.py3-none-any.whl")
    version("0.3.4", sha256="5e741daee96e9f1e9e06081b8c8a10c4ac199301a0564cdd99b09df15b4603d2", url="https://pypi.org/packages/eb/44/44da0f7c2a23b9fc38e2693ac86926375937880acfdb44307a3ccf762b68/leather-0.3.4-py2.py3-none-any.whl")
    version("0.3.3", sha256="076d1603b5281488285718ce1a5ce78cf1027fe1e76adf9c548caf83c519b988", url="https://pypi.org/packages/a0/44/1acad8bfe958874c66825a4bdddbd277a549580b88c5daf3a4c128c521b0/leather-0.3.3.tar.gz")
    version("0.3.2", sha256="ba531a6723903ef387b9c6eadff0db7cd39da01066198f53cb985e8343a61284", url="https://pypi.org/packages/19/b1/b19f6f896808e850ea482195cf71b962059c2ac9932720cfae8ec31483ed/leather-0.3.2.tar.gz")

    with default_args(type="run"):
        depends_on("py-six@1.6.1:", when="@0.3.4:0.3")

