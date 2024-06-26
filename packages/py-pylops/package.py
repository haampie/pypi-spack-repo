# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPylops(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("1.12.0", sha256="c90ad90b116f2e9a60f2cd80900797f45a310f0b50a70d1849e1dca21073a4b2", url="https://pypi.org/packages/66/55/97ff3ade2299ff0a09a5a104d32897f916299116ae75bc150c0f4c5eb1c7/pylops-1.12.0-py3-none-any.whl")
    version("1.11.1", sha256="533533919f1c6e29f46c3b12d047c150017babe927011ceb885bbc1cad3042dd", url="https://pypi.org/packages/b4/24/6c3221cafcf48420fb3778bd17a74d4f3c3f600b36abc20b6e32ae25fc3c/pylops-1.11.1-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    variant("advanced", default=False, description="advanced")
    # END VARIANTS

    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-llvmlite", when="@1.4:+advanced")
        depends_on("py-numba", when="@1.4:+advanced")
        depends_on("py-numpy@1.15.0:", when="@1.4:1")
        depends_on("py-pyfftw", when="@1.4:+advanced")
        depends_on("py-pywavelets", when="@1.8:+advanced")
        depends_on("py-scikit-fmm", when="@1.4:+advanced")
        depends_on("py-scipy@1.4.0:", when="@1.11:")
        depends_on("py-spgl1", when="@1.5:+advanced")
    # END DEPENDENCIES

