# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPytestRandomOrder(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("1.0.4", sha256="72279a7f823969e18b10e438950f58330d17e0fcffb57cbd7929770cd687ecb2", url="https://pypi.org/packages/e0/b8/617b593b629b8198338b1d860ada33be94d78195543dc0aa8659077ee0a0/pytest_random_order-1.0.4-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-pytest@3:", when="@1.0.3:")
    # END DEPENDENCIES

