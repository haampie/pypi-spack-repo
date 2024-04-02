# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPydeck(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.8.0", sha256="a8fa7757c6f24bba033af39db3147cb020eef44012ba7e60d954de187f9ed4d5", url="https://pypi.org/packages/ac/1e/676ed6c028bfd39d6c7c75abd57bc482f7eaa813f3faa715d80431732a43/pydeck-0.8.0-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.7:", when="@0.7:")
        depends_on("py-jinja2@2.10.1:")
        depends_on("py-numpy@1.16.4:")
    # END DEPENDENCIES

