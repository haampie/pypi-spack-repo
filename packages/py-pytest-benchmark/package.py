# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPytestBenchmark(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("3.2.3", sha256="01f79d38d506f5a3a0a9ada22ded714537bbdfc8147a881a35c1655db07289d9", url="https://pypi.org/packages/e7/1e/180579ad3bc53fe3181ef3843f0602f4db77f3609e5e5069a0ec194ff213/pytest_benchmark-3.2.3-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-py-cpuinfo", when="@3.1.0-alpha2:")
        depends_on("py-pytest@3.8:", when="@3.2.1:")
    # END DEPENDENCIES

