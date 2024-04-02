# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyWslink(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("1.12.4", sha256="20d53c81c720c3d9054957312e6c1c190040c8908741e1803d2752a0d8f7a638", url="https://pypi.org/packages/26/34/d2bb14c69951234e1d121d3f48307907d552c2a8cbde60a6f6d46ee53f5f/wslink-1.12.4-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-aiohttp@:3")
    # END DEPENDENCIES

