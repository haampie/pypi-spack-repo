##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyOpenmesh(PythonPackage):
    version("1.2.1", sha256="6fd3fa41a68148e4a7523f562426aa9758bf65ccc6642abcf79c37bae9c6af3c", url="https://pypi.org/packages/66/34/fd86bf3ca48d010f3a588fa997595c13162bc07563382f9a4d5ec8855dfb/openmesh-1.2.1.tar.gz")
    version("1.1.3", sha256="c1d24abc85b7b518fe619639f89750bf19ed3b8938fed4dd739a72f1e6f8b0f6", url="https://pypi.org/packages/f8/12/22c3353c44478c504f2fa18c0a51991734f908bd8218fb655e60f5f398e5/openmesh-1.1.3.tar.gz")

    with default_args(type="run"):
        depends_on("py-numpy", when="@1.1.3")

