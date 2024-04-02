# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyFuzzywuzzy(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.18.0", sha256="928244b28db720d1e0ee7587acf660ea49d7e4c632569cad4f1cd7e68a5f0993", url="https://pypi.org/packages/43/ff/74f23998ad2f93b945c0309f825be92e04e0348e062026998b5eefef4c33/fuzzywuzzy-0.18.0-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    variant("speedup", default=False, description="speedup")
    # END VARIANTS

    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-python-levenshtein@0.12:", when="@0.18:+speedup")
    # END DEPENDENCIES

