# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPep8(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("1.7.1", sha256="b22cfae5db09833bb9bd7c8463b53e1a9c9b39f12e304a8d0bba729c501827ee", url="https://pypi.org/packages/42/3f/669429ce58de2c22d8d2c542752e137ec4b9885fff398d3eceb1a7f5acb4/pep8-1.7.1-py2.py3-none-any.whl")
    version("1.7.0", sha256="4fc2e478addcf17016657dff30b2d8d611e8341fac19ccf2768802f6635d7b8a", url="https://pypi.org/packages/8a/cb/7d0fdca7e03f997945fb1bd60a8ddfea5c51229b865c470b4f7a64619d20/pep8-1.7.0-py2.py3-none-any.whl")
    version("1.5.7", sha256="62e87fd54535fb932b4a4d94868db523257a1031c8bc6bd358c2015433e646db", url="https://pypi.org/packages/e2/3a/fb53887b208e7e444c13b59244fcac4ef923678e6ae33e7fc71391f37b62/pep8-1.5.7-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    # END DEPENDENCIES

