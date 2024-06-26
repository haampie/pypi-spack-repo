# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyRetry(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.9.2", sha256="ccddf89761fa2c726ab29391837d4327f819ea14d244c232a1d24c67a2f98606", url="https://pypi.org/packages/4b/0d/53aea75710af4528a25ed6837d71d117602b01946b307a3912cb3cfcbcba/retry-0.9.2-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-decorator@3.4.2:", when="@0.9.2:")
        depends_on("py-py@1.4.26:", when="@0.9.1:")
    # END DEPENDENCIES

