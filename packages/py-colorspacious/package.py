# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyColorspacious(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("1.1.2", sha256="c78befa603cea5dccb332464e7dd29e96469eebf6cd5133029153d1e69e3fd6f", url="https://pypi.org/packages/ab/a1/318b9aeca7b9856410ededa4f52d6f82174d1a41e64bdd70d951e532675a/colorspacious-1.1.2-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-numpy", when="@1:")
    # END DEPENDENCIES

