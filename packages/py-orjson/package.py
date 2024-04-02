# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyOrjson(PythonPackage):
    # BEGIN VERSIONS
    version("3.8.7", sha256="8460c8810652dba59c38c80d27c325b5092d189308d8d4f3e688dbd8d4f3b2dc", url="https://pypi.org/packages/0a/6d/329b2cd461269a3cc97c6cf51bf42d3818c9f1aa22b64f00d64ce9907da6/orjson-3.8.7.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.7:", when="@:3.9.7")
    # END DEPENDENCIES

