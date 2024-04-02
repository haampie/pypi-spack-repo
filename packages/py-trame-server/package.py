# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyTrameServer(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("2.17.2", sha256="d27214d4395d3f778a527017db094449bdeb88586efccd60a6c9280e8c0ea25c", url="https://pypi.org/packages/fa/d2/46603ca2b9e992b90eb178d79503fb88bcdf9b1da39020a6950ae9dcc93a/trame_server-2.17.2-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-more-itertools", when="@2.13:")
        depends_on("py-wslink@1.12.2:")
    # END DEPENDENCIES

