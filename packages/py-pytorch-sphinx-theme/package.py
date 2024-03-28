# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPytorchSphinxTheme(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.0.19", sha256="3f66199e6b652ee1aa9bf6bc2c8f1c76551094d7fda5ccc9f1f34cc83ca00966", url="https://pypi.org/packages/c9/5d/b2f87b07c65cd9621064c39ee3d88f5c236e819eb9e65fd8bdd7466275e9/pytorch_sphinx_theme-0.0.19-py2.py3-none-any.whl")
    version("0.0.18", sha256="4d8bfa860b8ff68f702c0860c09a839923ee07c004a6bc24811ba4c2d3099afa", url="https://pypi.org/packages/0f/60/36b7459832b72354aeb601c11406866d0daad10126ce59bbf019ac2035e0/pytorch_sphinx_theme-0.0.18-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-sphinx")
    # END DEPENDENCIES

