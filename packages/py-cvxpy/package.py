##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyCvxpy(PythonPackage):
    version("1.1.13", sha256="a9c781e74ad76097b47b86456cb3a943898f7ec9ac8f47bcefc922051cdc4a04", url="https://pypi.org/packages/f0/95/e7eb169a7802fe0c5c50dd7f29c2e9d357b5f29c70adc3f5ca2ab684a04b/cvxpy-1.1.13.tar.gz")
    version("1.0.25", sha256="8535529ddb807067b0d59661dce1d9a6ddb2a218398a38ea7772328ad8a6ea13", url="https://pypi.org/packages/d9/ed/90e0a13ad7ac4e7cdc2aeaefed26cebb4922f205bb778199268863fa2fbe/cvxpy-1.0.25.tar.gz")

    with default_args(type="run"):
        depends_on("py-ecos@2:", when="@0.4.11:0,1.0.24:1.0,1.1.0-alpha2,1.1.2:1.1.3,1.4:")
        depends_on("py-multiprocess", when="@0.4.11:0,1.0.24:1.0")
        depends_on("py-numpy@1.15.0:", when="@1.0.24:1.0,1.1.0-alpha2,1.1.2:1.1.3,1.4:")
        depends_on("py-osqp@0.4.1:", when="@1.0.24:1.0,1.1.0-alpha2,1.1.2:1.1.3")
        depends_on("py-scipy@1.1.0:", when="@1.0.24:1.0,1.1.0-alpha2,1.1.2:1.1.3,1.4:")
        depends_on("py-scs@1.1.3:", when="@0.4.11:0,1.0.24:1.0,1.1.0-alpha2,1.1.2:1.1.3")
        depends_on("py-six", when="@0.4.11:0,1.0.24:1.0.25")

