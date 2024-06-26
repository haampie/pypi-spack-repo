# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyts(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.12.0", sha256="acd66b0cf1fd17d9ce6449335f5da30701f65fdee185d4b918726b62ca6af79d", url="https://pypi.org/packages/55/6e/fedefe4a1564943824e2dc4baa4cc5ed0862a4fe25ea3b69b4e3b9134bcf/pyts-0.12.0-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-joblib@0.12:", when="@0.11:0.12")
        depends_on("py-numba@0.48:", when="@0.11:0.12")
        depends_on("py-numpy@1.17.5:", when="@0.11:0.12")
        depends_on("py-scikit-learn@0.22.1:", when="@0.11:0.12")
        depends_on("py-scipy@1.3.0:", when="@0.11:0.12")
    # END DEPENDENCIES

