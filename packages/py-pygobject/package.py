# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPygobject(PythonPackage):
    # BEGIN VERSIONS
    version("3.46.0", sha256="481437b05af0a66b7c366ea052710eb3aacbb979d22d30b797f7ec29347ab1e6", url="https://pypi.org/packages/ac/4a/f24ddf1d20cc4b56affc7921e29928559a06c922eb60077448392792b914/PyGObject-3.46.0.tar.gz")
    version("3.38.0", sha256="051b950f509f2e9f125add96c1493bde987c527f7a0c15a1f7b69d6d1c3cd8e6", url="https://pypi.org/packages/3a/a7/de282a4aaedba59d60a895a7821e6497b39cbdfa94a352776ff45ffc6e6f/PyGObject-3.38.0.tar.gz")
    version("3.28.3", sha256="250fb669b6ac64eba034cc4404fcbcc993717b1f77c29dff29f8c9202da20d55", url="https://pypi.org/packages/e0/e8/1e4f21800015a9ca153969e85fc29f7962f8f82fc5dbc1ecbdeb9dc54c75/PyGObject-3.28.3.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.8:3", when="@3.46:")
        depends_on("python@:3", when="@3.32.2:3.42")
    # END DEPENDENCIES

