# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyUcMicroPy(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("1.0.2", sha256="8c9110c309db9d9e87302e2f4ad2c3152770930d88ab385cd544e7a7e75f3de0", url="https://pypi.org/packages/d1/1c/5aeb94aa980da111e4fd0c0fbe5ad95ed5bf9bd957f8e2a6178b85ff4da8/uc_micro_py-1.0.2-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.7:", when="@1.0.2:")
    # END DEPENDENCIES

