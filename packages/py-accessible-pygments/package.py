# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyAccessiblePygments(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.0.4", sha256="416c6d8c1ea1c5ad8701903a20fcedf953c6e720d64f33dc47bfb2d3f2fa4e8d", url="https://pypi.org/packages/20/d7/45cfa326d945e411c7e02764206845b05f8f5766aa7ebc812ef3bc4138cd/accessible_pygments-0.0.4-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-pygments@1.5:")
    # END DEPENDENCIES

