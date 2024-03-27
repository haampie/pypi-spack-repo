##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyChemfiles(PythonPackage):
    version("0.10.3", sha256="ffcf09675cfe0b9091a01a898df0c20e128bc68d4a01840d6552b6f663cfca79", url="https://pypi.org/packages/4e/03/71755e68b57d6f9e9aa6971a69d4dd663a6cc373400cbb3ed3003c402d35/chemfiles-0.10.3-py2.py3-none-win_amd64.whl")

    with default_args(type="run"):
        depends_on("py-numpy")

