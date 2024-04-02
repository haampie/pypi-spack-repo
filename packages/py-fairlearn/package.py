# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyFairlearn(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.10.0", sha256="772224097f8c073168bde44e659d7a2107f96d608063a738df9c985e17dab30f", url="https://pypi.org/packages/28/f2/bb5b2874498e023ebecc2e1b66d8c3d4cc5fd688837cbb9f4f79c323a8f0/fairlearn-0.10.0-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.8:", when="@0.8:")
        depends_on("py-numpy@1.24.4:", when="@0.10:")
        depends_on("py-pandas@2.0.3:", when="@0.10:")
        depends_on("py-scikit-learn@1.2.1:", when="@0.10:")
        depends_on("py-scipy@1.9.3:", when="@0.10:")
    # END DEPENDENCIES

