# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyVcstools(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.1.42", sha256="451d9efc1d7e0089a4a4488ec4be13b66d820c06e9d656011aa5c94c5b0385f1", url="https://pypi.org/packages/30/4a/a3ee59bd58ea68d1d33693c310c7f44206d53f1e17e9cab815273589503e/vcstools-0.1.42-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-python-dateutil", when="@0.1.42:")
        depends_on("py-pyyaml", when="@0.1.42:")
    # END DEPENDENCIES

