# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyEmailValidator(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("1.3.1", sha256="49a72f5fa6ed26be1c964f0567d931d10bf3fdeeacdf97bc26ef1cd2a44e0bda", url="https://pypi.org/packages/ba/ec/adc595d04e795b04bb0028fc6b067713fdb4a7e8cec44b428f7144fc432e/email_validator-1.3.1-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-dnspython@1.15:", when="@:1")
        depends_on("py-idna@2:")
    # END DEPENDENCIES

