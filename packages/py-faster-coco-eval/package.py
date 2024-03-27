##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyFasterCocoEval(PythonPackage):
    version("1.4.3", sha256="f961059badc60aeab7f05bc58a4070c3038abcdf79da953a6c90dc2d55441e74", url="https://pypi.org/packages/aa/46/7b404ee246edb4680a2482a97d14f4bee03b3f5bcfbe555fe5e4f966df05/faster-coco-eval-1.4.3.tar.gz")
    version("1.4.2", sha256="782e41da85989f9e0e5c6217e0123abbd47d86539e8e9fa661cf4094ab6f42a3", url="https://pypi.org/packages/b1/10/2f5831e604e9d5a73002fc822b20e5fab2eaa7597410562f7d6e516ab047/faster-coco-eval-1.4.2.tar.gz")
    version("1.4.1", sha256="11f69c4a1e788d0758dffc15d4a0bda29ece2fc72ae7611eff70cc01690772be", url="https://pypi.org/packages/6b/c5/3819d565bf651645790509f34d179d0a476316bb51426c4583c16a8a681a/faster-coco-eval-1.4.1.tar.gz")
    version("1.4.0", sha256="468f80270884ad72b4f177a6513a368f7304fb212bca5e944dc618322b55d9b7", url="https://pypi.org/packages/6c/98/217ad8646f90d37c212279ddc8fd75741409bd9faf8a2b2cc788e50df02a/faster-coco-eval-1.4.0.tar.gz")
    version("1.3.3", sha256="cf27e0ee9b8ec5dd3d85ff21d5e55c7697fa8d26b24ed6fce61af352d1fe13b5", url="https://pypi.org/packages/18/81/a1998fd5cfb0fd9277654b747901c0912ab56a175edb2c0688221a0a01ce/faster-coco-eval-1.3.3.tar.gz")

    with default_args(type="run"):
        depends_on("py-numpy", when="@1.4:")
        depends_on("py-pandas", when="@1.4.2:")
        depends_on("py-pillow", when="@1.4:")
        depends_on("py-plotly", when="@1.4:")

