# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPandasStubs(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("2.0.2.230605", sha256="39106b602f3cb6dc5f728b84e1b32bde6ecf41ee34ee714c66228009609fbada", url="https://pypi.org/packages/09/1d/2b9b5905d869c3e65d1c35e2a6420cbe4313a277aabfae6001670ef04075/pandas_stubs-2.0.2.230605-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.9:", when="@2.1:")
        depends_on("python@:3.11", when="@1.5.2:1")
        depends_on("python@:3.10", when="@1.4:1.5.1")
        depends_on("py-numpy@1.24.3:", when="@2.0.2")
        depends_on("py-types-pytz@2022.1.1:", when="@1.4.3.220718:")
    # END DEPENDENCIES

