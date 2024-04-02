# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPipx(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("1.2.0", sha256="a94c4bca865cd6e85b37cd6717a22481744890fe36b70db081a78d1feb923ce0", url="https://pypi.org/packages/ee/a2/c219f3e5120c58bfd077340e32c5ac61545e0fb0020701e34a528035aa87/pipx-1.2.0-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.7:", when="@1.1:1.2")
        depends_on("py-argcomplete@1.9.4:", when="@1:")
        depends_on("py-colorama@0.4.4:", when="@0.16.3: platform=windows")
        depends_on("py-importlib-metadata@3.3:", when="@:1.2 ^python@:3.7")
        depends_on("py-packaging@20:")
        depends_on("py-userpath@1.6:", when="@0.16.4:1.2")
    # END DEPENDENCIES

