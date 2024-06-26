# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyReacton(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("1.8.2", sha256="37ff8b7622511fa62ecb4595475eb3787b983476fcdbd34322ca28384139af06", url="https://pypi.org/packages/7d/87/aaf958a4c85db9290414518dcc9115c2cbd903fd4d3fda5580f79cb53eb8/reacton-1.8.2-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-ipywidgets")
        depends_on("py-typing-extensions@4.1.1:")
    # END DEPENDENCIES

