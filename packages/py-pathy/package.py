# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPathy(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.10.1", sha256="a7613ee2d99a0a3300e1d836322e2d947c85449fde59f52906f995dbff67dad4", url="https://pypi.org/packages/82/c6/683e3955de9a13b14dfa3ea358cd58f3914057e8064a2dcbfd450958e72e/pathy-0.10.1-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-google-cloud-storage@1.26:1", when="@:0.2")
        depends_on("py-smart-open@5.2.1:6", when="@0.10.1:")
        depends_on("py-typer@0.3:", when="@0.1.3:")
    # END DEPENDENCIES

