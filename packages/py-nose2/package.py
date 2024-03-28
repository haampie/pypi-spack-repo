# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyNose2(PythonPackage):
    # BEGIN VERSIONS
    version("0.9.1", sha256="31d8beb00aed3ccc6efb1742bb90227d883e471715188249f594310676e0ef0e", url="https://pypi.org/packages/2a/c6/f1941e6af8e97cb5cf7405283d5240ba3fb0ce9ace68403904436d6fff65/nose2-0.9.1-py2.py3-none-any.whl")
    version("0.6.0", sha256="daa633e92a52e0db60ade7e105a2ba5cad7ac819f3608740dcfc6140b9fd0a94", url="https://pypi.org/packages/d5/63/806d5f07ea3fc1f8c4df739cf110d87412850ada0d52d905f1bb9c610793/nose2-0.6.0.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-coverage@4.4.1:", when="@0.9:0.11")
        depends_on("py-six@1.7:", when="@0.9:0.11")
    # END DEPENDENCIES

