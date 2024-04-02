# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyKeyboard(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.13.5", sha256="8e9c2422f1217e0bd84489b9ecd361027cc78415828f4fe4f88dd4acd587947b", url="https://pypi.org/packages/55/88/287159903c5b3fc6d47b651c7ab65a54dcf9c9916de546188a7f62870d6d/keyboard-0.13.5-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-pyobjc", when="@0.13.2: platform=darwin")
    # END DEPENDENCIES

