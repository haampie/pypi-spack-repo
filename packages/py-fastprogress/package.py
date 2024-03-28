# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyFastprogress(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("1.0.0", sha256="474cd6a6e5b1c29a02383d709bf71f502477d0849bddc6ba5aa80b683f4ad16f", url="https://pypi.org/packages/eb/1f/c61b92d806fbd06ad75d08440efe7f2bd1006ba0b15d086debed49d93cdc/fastprogress-1.0.0-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-numpy", when="@1:1.0.1")
    # END DEPENDENCIES

