# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyTrame(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("3.5.3", sha256="612c22c94cc221590297cf5e0b231c5b48cc8d453682d814529a5fe99016ae9a", url="https://pypi.org/packages/e5/aa/37e9ba76b5b0d564bf7738936dae572d39fe32ec3a6c6cb96fbc3a567b3a/trame-3.5.3-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-trame-client@2.14:", when="@3.4:")
        depends_on("py-trame-server@2.13.1:", when="@3.4:")
    # END DEPENDENCIES

