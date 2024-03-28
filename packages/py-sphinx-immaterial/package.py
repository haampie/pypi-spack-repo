# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PySphinxImmaterial(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.11.2", sha256="96fc25386863a20626827104217b58ec1c541c9d77fc14c169226619fdb2fd9e", url="https://pypi.org/packages/13/17/0b7805cd078a47d0fd24faa4fa350b21568ea59f345b06574059ad794375/sphinx_immaterial-0.11.2-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-appdirs", when="@0.9:")
        depends_on("py-markupsafe", when="@0.4.1:")
        depends_on("py-pydantic", when="@0.6:0.11.4")
        depends_on("py-requests", when="@0.9:")
        depends_on("py-sphinx@4.0.0:", when="@:0.11.2")
        depends_on("py-typing-extensions", when="@0.6.1:")
    # END DEPENDENCIES

