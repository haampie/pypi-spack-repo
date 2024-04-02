# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPytestAiohttp(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("1.0.5", sha256="63a5360fd2f34dda4ab8e6baee4c5f5be4cd186a403cabd498fced82ac9c561e", url="https://pypi.org/packages/9a/a7/6e50ba2c0a27a34859a952162e63362a13142ce3c646e925b76de440e102/pytest_aiohttp-1.0.5-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.7:", when="@1:")
        depends_on("py-aiohttp@3.8.1:", when="@1:")
        depends_on("py-pytest@6.1:", when="@1:")
        depends_on("py-pytest-asyncio@0.17.2:", when="@1:")
    # END DEPENDENCIES

