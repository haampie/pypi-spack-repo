# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PySmoteVariants(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.7.3", sha256="51425df3ae21f941f050def8363c02ead350941a74c0f17d072a7108c254b95c", url="https://pypi.org/packages/ee/94/9e7a507de0628dc8b9eedc38535472d0a086cbda86d2e85d126f9dd889a1/smote_variants-0.7.3-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-joblib")
        depends_on("py-keras")
        depends_on("py-metric-learn")
        depends_on("py-minisom")
        depends_on("py-mkl")
        depends_on("py-numpy", when="@0.7.3:")
        depends_on("py-pandas")
        depends_on("py-scikit-learn")
        depends_on("py-scipy")
        depends_on("py-seaborn")
        depends_on("py-statistics")
        depends_on("py-tensorflow")
    # END DEPENDENCIES

