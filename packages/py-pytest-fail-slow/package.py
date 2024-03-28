# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPytestFailSlow(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.3.0", sha256="bf8b57a90d13f8f694ad8250c6d2e869714422c5d7f3c2d6541bec7d1706f783", url="https://pypi.org/packages/a2/bb/275f32982bd4f7a5c52639a1cb9571f0716d1b50647e607beb88769d9ff3/pytest_fail_slow-0.3.0-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-pytest@6.0.0:", when="@:0.4")
    # END DEPENDENCIES

