# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyOpencensusContext(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.1.1", sha256="1a3fdf6bec537031efcc93d51b04f1edee5201f8c9a0c85681d63308b76f5702", url="https://pypi.org/packages/2b/b7/720d4507e97aa3916ac47054cd75490de6b6148c46d8c2c487638f16ad95/opencensus_context-0.1.1-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-contextvars", when="^python@:3.6")
    # END DEPENDENCIES

