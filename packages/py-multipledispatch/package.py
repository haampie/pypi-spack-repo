# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyMultipledispatch(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.6.0", sha256="a55c512128fb3f7c2efd2533f2550accb93c35f1045242ef74645fc92a2c3cba", url="https://pypi.org/packages/89/79/429ecef45fd5e4504f7474d4c3c3c4668c267be3370e4c2fd33e61506833/multipledispatch-0.6.0-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-six", when="@0.6:0")
    # END DEPENDENCIES

