# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyIgor2(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.5.3", sha256="bb7b54a5926ec640e0e9176f46e0dd88ad956fec2d17ba3b0a7687eba82cefee", url="https://pypi.org/packages/5c/b8/5c73c5c54804323c8b5b1a52b68ff5d34a22d52bbd9bc0dd6d63745e4f1e/igor2-0.5.3-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-numpy@1.25.1:", when="@0.5.3:")
    # END DEPENDENCIES

