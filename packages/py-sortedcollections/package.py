# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PySortedcollections(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("1.2.1", sha256="f899e46a1e2e1efe022b8e824dc4036ac2a7585e8a37c404e03f6b1ce902666a", url="https://pypi.org/packages/ea/f1/831fa9763afc85d3065557762824490d6e4d1afe1a56e0f053a568ae0cb5/sortedcollections-1.2.1-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-sortedcontainers", when="@0.4:")
    # END DEPENDENCIES

