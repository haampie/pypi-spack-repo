# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyDeap(PythonPackage):
    # BEGIN VERSIONS
    version("1.3.3", sha256="8772f1b0fff042d5e516b0aebac2c706243045aa7d0de8e0b8658f380181cf31", url="https://pypi.org/packages/9a/a1/8c5ad42e78abdd7d2174baace0bd864ef6fd9a86c1cf72d410945669d784/deap-1.3.3.tar.gz")
    version("1.3.1", sha256="11f54493ceb54aae10dde676577ef59fc52d52f82729d5a12c90b0813c857a2f", url="https://pypi.org/packages/85/1e/5f707798f8f05616c03079f02b63568b2b91f8136891a2eeffd9f78f6d8b/deap-1.3.1.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-numpy", when="@1.3.1")
    # END DEPENDENCIES

