# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyGidgethub(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("5.3.0", sha256="4dd92f2252d12756b13f9dd15cde322bfb0d625b6fb5d680da1567ec74b462c0", url="https://pypi.org/packages/0f/e6/659924caa8b03cf06395775eb046ed4701913791d2b6afef8a4cf2861c92/gidgethub-5.3.0-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    variant("aiohttp", default=False, description="aiohttp")
    variant("tornado", default=False, description="tornado")
    # END VARIANTS

    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.7:", when="@5.2.1:")
        depends_on("py-aiohttp", when="+aiohttp")
        depends_on("py-pyjwt@2.4:+crypto", when="@5.2:")
        depends_on("py-tornado", when="+tornado")
        depends_on("py-uritemplate@3.0.1:", when="@4:")
    # END DEPENDENCIES

