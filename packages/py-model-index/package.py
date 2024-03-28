# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyModelIndex(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.1.11", sha256="a2a4d4431cd44e571d31e223cc4b0432663a62689de453bdb666e56a514b0e07", url="https://pypi.org/packages/0f/a6/4d4cbbef704f186d143e2859296a610a355992e4eae71582bd598093b36a/model_index-0.1.11-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-click")
        depends_on("py-markdown")
        depends_on("py-ordered-set")
        depends_on("py-pyyaml")
    # END DEPENDENCIES

