# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PySchemaSalad(PythonPackage):
    # BEGIN VERSIONS
    version("8.3.20221209165047", sha256="d97cc9a4d7c4255eb8000bcebaa8ac0d1d31801c921fd4113ab3051c1e326c7c", url="https://pypi.org/packages/22/10/b4519f55e08badba227829586f110e77798f7ab19bb60b349e67423ad8c5/schema-salad-8.3.20221209165047.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@:3.12", when="@8.4.20230808163024:")
        depends_on("python@:3.11", when="@8.3.20221115203138:8.4.20230606143604")
        depends_on("python@:3.11.0", when="@8.3.20220825114525:8.3.20221028160159")
    # END DEPENDENCIES

