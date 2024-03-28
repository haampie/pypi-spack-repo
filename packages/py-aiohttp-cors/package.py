# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyAiohttpCors(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.7.0", sha256="0451ba59fdf6909d0e2cd21e4c0a43752bc0703d33fc78ae94d9d9321710193e", url="https://pypi.org/packages/13/e7/e436a0c0eb5127d8b491a9b83ecd2391c6ff7dcd5548dfaec2080a2340fd/aiohttp_cors-0.7.0-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-aiohttp@1.1:", when="@0.5:0.5.0,0.5.2:")
    # END DEPENDENCIES

