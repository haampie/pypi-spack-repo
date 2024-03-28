# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyBatchspawner(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("1.1.0", sha256="d7e203128700c9105c660bf139a2dfe132e4c92708292576ea7ffe7985ed1481", url="https://pypi.org/packages/27/de/b9f3cf50d90167cca00e2f98f501038e0d2fb9a918343abfb767df000976/batchspawner-1.1.0-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-async-generator@1.8:", when="@1:1.2")
        depends_on("py-jinja2", when="@1:1.2")
        depends_on("py-jupyterhub@0.5:", when="@:1.1")
    # END DEPENDENCIES

