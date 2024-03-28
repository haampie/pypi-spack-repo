# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyct(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.4.8", sha256="222e104d561b28cfdb56667d2ba10e5290b4466db66d0af38ab935577af85390", url="https://pypi.org/packages/71/76/52ce7aec26b0171939d3b3843acd011f8eb297b2a569e992691bb2964185/pyct-0.4.8-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-param@1.7:", when="@0.4.4:")
        depends_on("py-pyyaml", when="@0.2.3,0.4:0.4.3")
        depends_on("py-requests", when="@0.4:0.4.3")
    # END DEPENDENCIES

