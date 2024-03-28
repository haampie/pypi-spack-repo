# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyCftime(PythonPackage):
    # BEGIN VERSIONS
    version("1.0.3.4", sha256="dd74d0d470baf1c50e31335215793a5e78436903e34b4f151fa9ccbf3a6cc20c", url="https://pypi.org/packages/7a/83/a61141ec141ceb0617468e04cc163dbdb9007b958191043618d1dc950b8f/cftime-1.0.3.4.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-numpy", when="@:1.0.1,1.0.3.3:1.2")
    # END DEPENDENCIES

