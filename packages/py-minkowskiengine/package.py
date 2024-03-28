# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyMinkowskiengine(PythonPackage):
    # BEGIN VERSIONS
    version("0.5.4", sha256="b1879c00d0b0b1d30ba622cce239886a7e3c78ee9da1064cdfe2f64c2ab15f94", url="https://pypi.org/packages/21/5c/c543c4bc5fbe73ac3e38465b3da4f24a61f7a4ac5baec867e582e94aa551/MinkowskiEngine-0.5.4.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    variant("cuda", default=False)
    variant("cuda_arch", default=False)
    # END VARIANTS

    # BEGIN DEPENDENCIES
    # END DEPENDENCIES

