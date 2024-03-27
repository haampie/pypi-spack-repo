##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyXtb(PythonPackage):
    version("22.1", sha256="7a59e7b783fc6e8b7328f55211de681e535a83991b07c4bab73494063f5e9018", url="https://pypi.org/packages/a8/36/a0b21a9efe55fbdea9d9a3ffc31046cf5291d15da52ea36967d37104c3b7/xtb-22.1.tar.gz")

    with default_args(type="run"):
        depends_on("py-cffi")
        depends_on("py-numpy")

