# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyTrimesh(PythonPackage):
    # BEGIN VERSIONS
    version("3.17.1", sha256="a09460ee4e11c32bf9f0643b86241b3e3e2aa86296c4912a0738b76da3034c00", url="https://pypi.org/packages/0e/99/435e48279823f0a833cdbb508b25e1e659af51ed3a1ec2b05551e1dd139a/trimesh-3.17.1-py3-none-any.whl")
    version("2.38.10", sha256="866e73ea35641ff2af73867c891d7f9b90c75ccb8a3c1e8e06e16ff9af1f8c64", url="https://pypi.org/packages/1e/5d/add451660f0f444aeb2b38daa73f336d10b40bc97af164e98f58581c60d6/trimesh-2.38.10.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    variant("easy", default=False, description="easy")
    # END VARIANTS

    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-chardet", when="@3.6.2:+easy")
        depends_on("py-colorlog", when="@3.6.2:+easy")
        depends_on("py-jsonschema", when="@3.6.2:+easy")
        depends_on("py-lxml", when="@3.6.2:+easy")
        depends_on("py-mapbox-earcut", when="@3.15:+easy")
        depends_on("py-msgpack", when="@3.6.2:3.20+easy")
        depends_on("py-networkx", when="@3.6.2:+easy")
        depends_on("py-numpy", when="@3.6.2:")
        depends_on("py-pillow", when="@3.6.2:+easy")
        depends_on("py-pycollada", when="@3.6.2:+easy")
        depends_on("py-pyglet@:1", when="@3.16.2:3.18.1+easy")
        depends_on("py-requests", when="@3.6.2:4.0.4+easy")
        depends_on("py-rtree", when="@3.6.2:+easy")
        depends_on("py-scipy", when="@3.6.2:+easy")
        depends_on("py-setuptools", when="@3.6.2:+easy")
        depends_on("py-shapely", when="@3.6.2:+easy")
        depends_on("py-svg-path", when="@3.6.2:+easy")
        depends_on("py-sympy", when="@3.6.2:3.23.3+easy")
        depends_on("py-xxhash", when="@3.6.2:+easy")
    # END DEPENDENCIES

