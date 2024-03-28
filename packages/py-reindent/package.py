# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyReindent(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("3.5.1", sha256="1248ddf8bb209499ddaff6e841d60c822edff7dcff5e0e5beedbafa06dbc33aa", url="https://pypi.org/packages/e2/21/bbfe0baec43c1d1cb1683653334b55161ccc950991c1803e17f276b5759a/reindent-3.5.1-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-setuptools", when="@3:")
    # END DEPENDENCIES

