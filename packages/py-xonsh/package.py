# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyXonsh(PythonPackage):
    # BEGIN VERSIONS
    version("0.11.0", sha256="0d9c3d9a4e8b8199ae697fbc9d1e0ae55085cdbdd4306d04813350996f9c15dc", url="https://pypi.org/packages/12/5c/b6143c3d6a3007450f2126a5188a86d7524122c761bf1652428c3393dfd2/xonsh-0.11.0.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.9:", when="@0.14.1:")
    # END DEPENDENCIES

