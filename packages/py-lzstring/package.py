# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyLzstring(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("1.0.3", sha256="82a913b08f6eaacf584624e4cbd5e5c361b546d0f9ec5620760d2ca137926811", url="https://pypi.org/packages/bd/4e/0885ee80e75b709dfb0750dacfc9bd1bff37c591c777015d43d5679d60b0/lzstring-1.0.3-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-future", when="@1.0.1:1.0.3")
    # END DEPENDENCIES

