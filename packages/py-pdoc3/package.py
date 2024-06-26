# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPdoc3(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.10.0", sha256="ba45d1ada1bd987427d2bf5cdec30b2631a3ff5fb01f6d0e77648a572ce6028b", url="https://pypi.org/packages/67/36/add16f4705689ed1f31aba24c973d035fc953c6fe54af9143837cc3b1315/pdoc3-0.10.0-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-mako", when="@0.10:")
        depends_on("py-markdown@3:", when="@0.10:")
    # END DEPENDENCIES

