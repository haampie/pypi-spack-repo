# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyUserpath(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("1.8.0", sha256="f133b534a8c0b73511fc6fa40be68f070d9474de1b5aada9cded58cdf23fb557", url="https://pypi.org/packages/45/72/e8cf3e440a4719253cf114c091ae84e7a07394dbb44983f3a561f40f80b6/userpath-1.8.0-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.7:", when="@1.8:")
        depends_on("py-click")
    # END DEPENDENCIES

