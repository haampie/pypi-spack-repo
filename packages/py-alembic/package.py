# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyAlembic(PythonPackage):
    # BEGIN VERSIONS
    version("1.5.5", sha256="65b64087cc47bcf2d7ee127698919976223a1e6fa36c7094f15be4fe55c8d788", url="https://pypi.org/packages/15/9f/b281de89dde4e26111bbc7d852322a79040eef42692d8772cb46f58303a6/alembic-1.5.5-py2.py3-none-any.whl")
    version("1.0.7", sha256="16505782b229007ae905ef9e0ae6e880fddafa406f086ac7d442c1aaf712f8c2", url="https://pypi.org/packages/a4/06/f1ae8393463c26f3dafa21eebac611088da02a26e1f1e23bd75fee2dbffe/alembic-1.0.7.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-mako", when="@1:1.0.0,1.4.3:1.4,1.5.1:1.6.1,1.6.3:")
        depends_on("py-python-dateutil", when="@1:1.0.0,1.4.3:1.4,1.5.1:1.6.1,1.6.3:1.6")
        depends_on("py-python-editor@0.3:", when="@1:1.0.0,1.4.3:1.4,1.5.1:1.6.1,1.6.3:1.6")
        depends_on("py-sqlalchemy@1.3.0:", when="@1.5.1:1.6.1,1.6.3:")
    # END DEPENDENCIES

