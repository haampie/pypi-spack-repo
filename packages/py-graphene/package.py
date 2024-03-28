# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyGraphene(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("2.1.9", sha256="3d446eb1237c551052bc31155cf1a3a607053e4f58c9172b83a1b597beaa0868", url="https://pypi.org/packages/ef/a2/b3e68706bf45abc2f9d70f099a4b4ca6305779577f4a03458d78fb39cd42/graphene-2.1.9-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-aniso8601@3:7", when="@2.1.8:2")
        depends_on("py-graphql-core@2.1:2", when="@2.1.3:2")
        depends_on("py-graphql-relay@2", when="@2.1.7:2")
        depends_on("py-six@1.10:", when="@2.0.1:2")
    # END DEPENDENCIES

