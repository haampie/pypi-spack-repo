# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyMysqlConnectorPython(PythonPackage):
    # BEGIN VERSIONS
    version("8.0.13", sha256="95d5be4528158c8464a6aa64d27c4f872998b3d2a666efada833db4c90646622", url="https://pypi.org/packages/8f/6d/fb8ebcbbaee68b172ce3dfd08c7b8660d09f91d8d5411298bcacbd309f96/mysql-connector-python-8.0.13.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-protobuf@3.0.0:", when="@8.0.11:8.0.18,8.0.20:8.0.21")
    # END DEPENDENCIES

