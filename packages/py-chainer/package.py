# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyChainer(PythonPackage):
    # BEGIN VERSIONS
    version("7.2.0", sha256="d8b2eea53cd6698e9d1a7c25c4989477f4fd344601f12898996780524440ab0b", url="https://pypi.org/packages/c5/b0/edb9e4f9c361c784331e7a61e6f0d1dbae4cfb0da74ddb79e21b0ef9b513/chainer-7.2.0.tar.gz")
    version("6.7.0", sha256="762557c38ea30ee4519e3381ce13f40fda1b564fb5cb5c221a2c7c166f3cf292", url="https://pypi.org/packages/57/c7/8703e3d03825d51a80919e250f6aa5c88f181b8b5cf3cac0d7761dfe0f6d/chainer-6.7.0.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    variant("mn", default=False)
    # END VARIANTS

    # BEGIN DEPENDENCIES
    # END DEPENDENCIES

