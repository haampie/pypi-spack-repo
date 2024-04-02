# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyFasterCocoEval(PythonPackage):
    # BEGIN VERSIONS
    version("1.4.3", sha256="f961059badc60aeab7f05bc58a4070c3038abcdf79da953a6c90dc2d55441e74", url="https://pypi.org/packages/aa/46/7b404ee246edb4680a2482a97d14f4bee03b3f5bcfbe555fe5e4f966df05/faster-coco-eval-1.4.3.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-numpy", when="@1.4:")
        depends_on("py-pandas", when="@1.4.2:")
        depends_on("py-pillow", when="@1.4:")
        depends_on("py-plotly", when="@1.4:")
    # END DEPENDENCIES

