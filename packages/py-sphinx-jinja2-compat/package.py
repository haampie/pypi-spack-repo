# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PySphinxJinja2Compat(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.2.0", sha256="a5f3112d6873991c2cf28e37287163a0485d9c0812863b8aa4df7182722501fb", url="https://pypi.org/packages/75/c7/18ffe4d7cb65ea20094645d640ff18ac4cd6a64b1f26b71f8308d26c9d32/sphinx_jinja2_compat-0.2.0-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-jinja2@2.10:")
        depends_on("py-markupsafe@1:")
    # END DEPENDENCIES

