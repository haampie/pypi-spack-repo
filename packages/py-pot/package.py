# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPot(PythonPackage):
    # BEGIN VERSIONS
    version("0.7.0", sha256="d4ac2bc8791f049a3166820d51e218d6c299885449b735eafef8d18c76d4ad06", url="https://pypi.org/packages/a8/5d/e7525ff865040845bfacbca4416610761a07db67ba77f6be4e26dd2583bf/POT-0.7.0.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-cython@0.23:", when="@0.7:0.7.0.0")
        depends_on("py-numpy@1.16.0:", when="@0.7:0.7.0.0")
        depends_on("py-scipy@1.0.0:", when="@0.7:0.7.0.0")
    # END DEPENDENCIES

