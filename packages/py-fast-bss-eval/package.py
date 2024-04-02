# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyFastBssEval(PythonPackage):
    # BEGIN VERSIONS
    version("0.1.4", sha256="b9b1307577f77128dda9efb8310ff4d4ca39afc0fccce0c62640a1e34f9add13", url="https://pypi.org/packages/2c/df/9095cedbb89aa308c34b692f65fb9f4405c7fea735feeea8ce3148a66f43/fast_bss_eval-0.1.4.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@:3")
    # END DEPENDENCIES

