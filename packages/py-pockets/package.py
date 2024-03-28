# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPockets(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.9.1", sha256="68597934193c08a08eb2bf6a1d85593f627c22f9b065cc727a4f03f669d96d86", url="https://pypi.org/packages/e9/2f/a4583c70fbd8cd04910e2884bcc2bdd670e884061f7b4d70bc13e632a993/pockets-0.9.1-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-six@1.5.2:", when="@0.3.1:")
    # END DEPENDENCIES

