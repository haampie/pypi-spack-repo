# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPomegranate(PythonPackage):
    # BEGIN VERSIONS
    version("0.12.0", sha256="8b00c88f7cf9cad8d38ea00ea5274821376fefb217a1128afe6b1fcac54c975a", url="https://pypi.org/packages/51/b9/832545c599c967e94019d587effd3fc03de9febe45cc297906a2f56790bc/pomegranate-0.12.0.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-joblib@0.9.0-beta4:", when="@0.11.2:0.12.0,0.13.1-rc0:0.13.1")
        depends_on("py-networkx@2:", when="@0.11.2:0.12.0,0.13.1-rc0:0.13.1")
        depends_on("py-numpy@1.8:", when="@0.11.2:0.12.0,0.13.1-rc0:0.13.1")
        depends_on("py-pyyaml", when="@0.11.2:0.12.0,0.13.1-rc0:0.13.1")
        depends_on("py-scipy@0.17:", when="@0.11.2:0.12.0,0.13.1-rc0:0.13.1")
    # END DEPENDENCIES

