##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyFastdtw(PythonPackage):
    version("0.3.4", sha256="2350fa6ec36bcad186eaf81f46eff35181baf04e324f522de8aeb43d0243f64f", url="https://pypi.org/packages/99/43/30f2d8db076f216b15c10db663b46e22d1750b1ebacd7af6e62b83d6ab98/fastdtw-0.3.4.tar.gz")

    with default_args(type="run"):
        depends_on("py-numpy", when="@0.3.4:")

