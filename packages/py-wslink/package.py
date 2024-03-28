# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyWslink(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("1.12.4", sha256="20d53c81c720c3d9054957312e6c1c190040c8908741e1803d2752a0d8f7a638", url="https://pypi.org/packages/26/34/d2bb14c69951234e1d121d3f48307907d552c2a8cbde60a6f6d46ee53f5f/wslink-1.12.4-py3-none-any.whl")
    version("1.12.3", sha256="5fd6ddf86ff2c1bf5776a59b48410c23e35d9aba08461d81b5c2e18019209518", url="https://pypi.org/packages/07/24/95a870a3ecf48de85c5dbbdd286e2c38c51e8ddeaab7a65c43eca4ba8cbe/wslink-1.12.3-py3-none-any.whl")
    version("1.12.2", sha256="b10c94a9c2d950e3a09a8961f45b9d567350091c89389d936b02b0abf2efb0c0", url="https://pypi.org/packages/77/fc/7cf750ae91df543a3caaba46e06bfae9a582208674aa73e3ea213c1b7dd1/wslink-1.12.2-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-aiohttp@:3", when="@1.6.6:")
    # END DEPENDENCIES

