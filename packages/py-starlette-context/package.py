# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyStarletteContext(PythonPackage):
    # BEGIN VERSIONS
    version("0.3.5", sha256="e6b9f905823860e9e36c013dbfcf770562f3b88bec21cb861fef2e0bd0615697", url="https://pypi.org/packages/e9/8e/608c0333e9c1c18a25ad81292bbc83d351317fe2059c52f3b135f7777700/starlette_context-0.3.5.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.7:", when="@:0.3.5")
    # END DEPENDENCIES

