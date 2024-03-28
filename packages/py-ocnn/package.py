# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyOcnn(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("2.2.0", sha256="790d689ff5d1b9d26dc6fabe4b1fc72ade8fd71b55f0497dcf7d23595a42aa49", url="https://pypi.org/packages/b6/4c/e22fd40215216d5c3d8388e9827392a2daf0462f719800972c3eed2bd5ae/ocnn-2.2.0-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-numpy")
        depends_on("py-torch")
    # END DEPENDENCIES

