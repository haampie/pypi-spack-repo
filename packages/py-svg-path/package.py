# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PySvgPath(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("6.3", sha256="4bd4747679b527f8db9868e1623bee9f416540b658285d903885768d8a427e5a", url="https://pypi.org/packages/d6/ea/ec6101e1710ac74e88b10312e9b59734885155e47d7dbb1171e4d347a364/svg.path-6.3-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.8:", when="@6.3:")
    # END DEPENDENCIES

