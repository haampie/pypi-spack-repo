# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyDebtcollector(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("2.2.0", sha256="34663e5de257c67bf38827cfbea259c4d4ad27eba6b5a9d9242cb54076bfb4ad", url="https://pypi.org/packages/8e/50/07a7ccf4dbbe90b58e96f97b747ff98aef9d8c841d2616c48cc05b07db33/debtcollector-2.2.0-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-pbr@2:2.0,3:", when="@:2.4")
        depends_on("py-six@1.10:", when="@1.19:2.3")
        depends_on("py-wrapt@1.7:")
    # END DEPENDENCIES

