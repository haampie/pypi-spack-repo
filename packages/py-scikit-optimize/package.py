# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyScikitOptimize(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.9.0", sha256="5a439a18232381fad4bda78e914b616416720708e67f123498d14bd2842d861a", url="https://pypi.org/packages/55/f6/2d9efbd86126c40fe0f8a47611a9e2480b493b6f0ce9751bdf0240cfa091/scikit_optimize-0.9.0-py2.py3-none-any.whl")
    version("0.5.2", sha256="a2304413f7b66b27dfaed64271c370e5e2c926fbc1cbecdb67fe47cd847f9d5c", url="https://pypi.org/packages/f4/44/60f82c97d1caa98752c7da2c1681cab5c7a390a0fdd3a55fac672b321cac/scikit_optimize-0.5.2-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    variant("plots", default=False, description="plots")
    # END VARIANTS

    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-joblib@0.11:", when="@0.7.3:")
        depends_on("py-matplotlib@2.0.0:", when="@0.7.3:+plots")
        depends_on("py-matplotlib", when="@0.5.2:0.7.2+plots")
        depends_on("py-numpy@1.13.3:", when="@0.8.0:0.9")
        depends_on("py-numpy", when="@:0.7.2")
        depends_on("py-pyaml@16:", when="@0.7.3:")
        depends_on("py-scikit-learn@0.20.0:", when="@0.8.0:0.9")
        depends_on("py-scikit-learn@0.19.1:", when="@0.5:0.8.dev")
        depends_on("py-scipy@0.19.1:", when="@0.8.0:0.9")
        depends_on("py-scipy@0.14:", when="@0.5:0.7.2")
    # END DEPENDENCIES

