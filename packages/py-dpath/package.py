# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyDpath(PythonPackage):
    # BEGIN VERSIONS
    version("2.1.6", sha256="31407395b177ab63ef72e2f6ae268c15e938f2990a8ecf6510f5686c02b6db73", url="https://pypi.org/packages/84/c8/10c2d41a0958b76e777c07a521d64c871ab9022520babb3e08fa7eeb0810/dpath-2.1.6-py3-none-any.whl")
    version("2.0.1", sha256="bea06b5f4ff620a28dfc9848cf4d6b2bfeed34238edeb8ebe815c433b54eb1fa", url="https://pypi.org/packages/60/3f/562b045ad2542ab1279bbc5a05a62511c1ea1d8b5987fb0a50ee78704621/dpath-2.0.1.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.7:", when="@2.0.8:")
    # END DEPENDENCIES

