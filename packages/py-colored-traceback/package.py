# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyColoredTraceback(PythonPackage):
    # BEGIN VERSIONS
    version("0.3.0", sha256="6da7ce2b1da869f6bb54c927b415b95727c4bb6d9a84c4615ea77d9872911b05", url="https://pypi.org/packages/9a/8b/0a4e2a8cdc14279b265532f11c9cb75396880e6295c99a0bed7281b6076a/colored-traceback-0.3.0.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-pygments", when="@0.2.2:")
    # END DEPENDENCIES

