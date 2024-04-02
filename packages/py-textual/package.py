# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyTextual(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.47.1", sha256="da79df2e138f6de51bda84a1ee1460936bb2ecf5527ca2d47b9b59c584323327", url="https://pypi.org/packages/b7/3f/61a8eae44a5ecffde54a69146e2885bd1b1a877ed46148b2c4e97eb8384b/textual-0.47.1-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.8:3", when="@0.44:")
        depends_on("py-markdown-it-py@2.1:+linkify+plugins")
        depends_on("py-rich@13.3.3:")
        depends_on("py-typing-extensions@4.4:")
    # END DEPENDENCIES

