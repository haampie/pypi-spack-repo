# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyEcos(PythonPackage):
    # BEGIN VERSIONS
    version("2.0.12", sha256="f48816d73b87ae325556ea537b7c8743187311403c80e3832035224156337c4e", url="https://pypi.org/packages/04/da/aefd27c06a9179a7e5614d0d97c0384072d2d22800790690c661eb6f2f4a/ecos-2.0.12.tar.gz")
    version("2.0.7.post1", sha256="83e90f42b3f32e2a93f255c3cfad2da78dbd859119e93844c45d2fca20bdc758", url="https://pypi.org/packages/b9/3a/59aa93b573a22fda44402383aeddcc2a081c31e61080af3da9d11855c77a/ecos-2.0.7.post1.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-numpy@1.6:", when="@1.1:2.0.4,2.0.7.post:2.0.7")
        depends_on("py-scipy@0.9:", when="@1.1:2.0.4,2.0.7.post:2.0.7")
    # END DEPENDENCIES

