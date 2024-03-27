##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyGalaxyContainers(PythonPackage):
    version("22.1.1", sha256="d92e51268f187c3c8e8ab4f0d017ee48c47fb89297c69028f04af8c21e9ee919", url="https://pypi.org/packages/e2/d1/d301c53d0bc3b3af38ef65109f892e4b1cde5e77eaa768ba30e8deff62e9/galaxy_containers-22.1.1-py2.py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-galaxy-util")
        depends_on("py-requests")

