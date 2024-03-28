# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPathos(PythonPackage):
    # BEGIN VERSIONS
    version("0.2.8", sha256="789ae53487e5f9393fcc2b9703188a1b97f20206c429654134a7152f591bafe7", url="https://pypi.org/packages/23/6b/7ffe02bdb5f5cf4b2290cc906b415dde7c886dbb11928dda40d39e6654dd/pathos-0.2.8-py2.py3-none-any.whl")
    version("0.2.3", sha256="954c5b0a8b257c375e35d311c65fa62a210a3d65269195557de38418ac9f61f9", url="https://pypi.org/packages/b1/3e/391c9a3c639fc5ce7502ac16fde81dcc5508f2a9cc0d1acc650725400b52/pathos-0.2.3.tar.gz")
    version("0.2.0", sha256="e35418af733bf434da83746d46acca94375d6e306b3df330b2a1808db026a188", url="https://pypi.org/packages/1d/a0/e5107f85bcb397c82ee875d005d88a537d4fdc1d1498f34bb15dfba7ca49/pathos-0.2.0.tgz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-dill@0.3.4:", when="@0.2.8")
        depends_on("py-multiprocess@0.70.12:", when="@0.2.8")
        depends_on("py-pox@0.3:", when="@0.2.8")
        depends_on("py-ppft@1.6.6.4:", when="@0.2.8")
    # END DEPENDENCIES

