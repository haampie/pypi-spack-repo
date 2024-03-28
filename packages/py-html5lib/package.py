# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyHtml5lib(PythonPackage):
    # BEGIN VERSIONS
    version("1.1", sha256="0d78f8fde1c230e99fe37986a60526d7049ed4bf8a9fadbad5f00e22e58e041d", url="https://pypi.org/packages/6c/dd/a834df6482147d48e225a49515aabc28974ad5a4ca3215c18a882565b028/html5lib-1.1-py2.py3-none-any.whl")
    version("1.0.1", sha256="20b159aa3badc9d5ee8f5c647e5efd02ed2a66ab8d354930bd9ff139fc1dc0a3", url="https://pypi.org/packages/a5/62/bbd2be0e7943ec8504b517e62bab011b4946e1258842bc159e5dfde15b96/html5lib-1.0.1-py2.py3-none-any.whl")
    version("0.99", sha256="aff6fd3031c563883197e5a04b7df324086ff5f358278a0386808c463a077e59", url="https://pypi.org/packages/2c/e8/4944b8a4e48951cf9db0cd05c4efdfc341583017f66d67b04ac1f4e63ab5/html5lib-0.99.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-six@1.9:", when="@1.0.1:")
        depends_on("py-webencodings", when="@1.0.1:")
    # END DEPENDENCIES

