# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyOsqp(PythonPackage):
    # BEGIN VERSIONS
    version("0.6.2.post8", sha256="23d6bae4a3612f60d5f652d0e5fa4b2ead507cabfff5d930d822057ae6ed6677", url="https://pypi.org/packages/5a/61/7b94eb7de2b7c9d12d8757ef9d0f5dfe3c5dc0ba0e88f08d4ae929996a34/osqp-0.6.2.post8.tar.gz")
    version("0.6.1", sha256="47b17996526d6ecdf35cfaead6e3e05d34bc2ad48bcb743153cefe555ecc0e8c", url="https://pypi.org/packages/ba/17/49790ce2ce7a6b95cd250642ebc68bd723ddefdd052ee8dcc1e0dcf4ffca/osqp-0.6.1.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-future", when="@0.2:0.2.0,0.4:0.6.1")
        depends_on("py-numpy@1.7:", when="@0.2:0.2.0,0.4:0.6.1,0.6.4:0")
        depends_on("py-scipy@0.13.2:", when="@0.2:0.2.0,0.4:0.6.1,0.6.4")
    # END DEPENDENCIES

