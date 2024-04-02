# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyLightningApiAccess(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.0.5", sha256="08657fee636377534332df92e0bee893d46cb877f9642cba09ce560aed95fd40", url="https://pypi.org/packages/0e/22/85cd1c2ed7a90fc6213ed107533cf7168fc58a4bef3bf276271169f4b021/lightning_api_access-0.0.5-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.7:")
    # END DEPENDENCIES

