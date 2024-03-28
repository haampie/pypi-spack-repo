# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyShap(PythonPackage):
    # BEGIN VERSIONS
    version("0.41.0", sha256="a49ea4d65aadbc845a695fa3d7ea0bdfc8c928b8e213b0feedf5868ade4b3ca5", url="https://pypi.org/packages/ed/bb/b48bb3fe1b47e7673b037ed9627746eb1bf9f3ee5b45289f5ab6a26089ef/shap-0.41.0.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.9:", when="@0.45:")
    # END DEPENDENCIES

