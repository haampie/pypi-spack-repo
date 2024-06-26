# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPlumDispatch(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("2.2.2", sha256="d7ee415bd166ffa90eaa4b24d7c9dc7ca6f8875750586001e7c9baff706223bd", url="https://pypi.org/packages/45/07/95c6be6710207f4a2c83023f59889a86c58282c8367aa49a907e9e6deb57/plum_dispatch-2.2.2-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.8:", when="@2.2:")
        depends_on("py-beartype@0.16.2:", when="@2.2.2:")
        depends_on("py-typing-extensions", when="@2.2: ^python@:3.9")
    # END DEPENDENCIES

