# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyStarletteContext(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.3.5", sha256="d9eeccaafd4fad13abe662295b802c8a58a7e11a0d33f933f001212472619086", url="https://pypi.org/packages/6e/0d/613f99d2b8e5c40fdbcfd9c04241ad7fdb6b3fc4c706dbdcd9f0cadbdec9/starlette_context-0.3.5-py37-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-starlette", when="@0.2.3:")
    # END DEPENDENCIES

