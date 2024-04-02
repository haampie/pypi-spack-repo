# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyBackportsFunctoolsLruCache(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("2.0.0", sha256="0a754323a46847735a112677fb8807b45f6d824d02a5795a50905218ac56a0d6", url="https://pypi.org/packages/c6/c6/4761a2ccb03d650ca803b11a7cdd69ff0696926d3fea218c8ca22c808448/backports.functools_lru_cache-2.0.0-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.8:", when="@2:")
    # END DEPENDENCIES

