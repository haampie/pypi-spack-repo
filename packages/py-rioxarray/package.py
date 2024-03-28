# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyRioxarray(PythonPackage):
    # BEGIN VERSIONS
    version("0.4.1.post0", sha256="f043f846724a58518f87dd3fa84acbe39e15a1fac7e64244be3d5dacac7fe62b", url="https://pypi.org/packages/ab/a1/37432860acd0859b7df470150f10bba2fd1d08e879ab8e7a63b85bab9048/rioxarray-0.4.1.post0.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.10:", when="@0.15.1:")
        depends_on("python@3.9:", when="@0.14:0.15.0")
    # END DEPENDENCIES

