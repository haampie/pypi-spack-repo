# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PySqlalchemyUtils(PythonPackage):
    # BEGIN VERSIONS
    version("0.41.1", sha256="6c96b0768ea3f15c0dc56b363d386138c562752b84f647fb8d31a2223aaab801", url="https://pypi.org/packages/73/d8/3863fdfe6b27f6c0dffc650aaa2929f313b33aea615b102279fd46ab550b/SQLAlchemy_Utils-0.41.1-py3-none-any.whl")
    version("0.36.8", sha256="fb66e9956e41340011b70b80f898fde6064ec1817af77199ee21ace71d7d6ab0", url="https://pypi.org/packages/14/68/e5301c4c960c79a32333b8805e52cb69d3d237aa869a773b4157ccb3eb26/SQLAlchemy-Utils-0.36.8.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-importlib-metadata", when="@0.38.3: ^python@:3.7")
        depends_on("py-sqlalchemy@1.3.0:", when="@0.38.3:")
    # END DEPENDENCIES

