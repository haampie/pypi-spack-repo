# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyFlashAttn(PythonPackage):
    # BEGIN VERSIONS
    version("2.5.5", sha256="751cee17711d006fe7341cdd78584af86a6239afcfe43b9ed11c84db93126267", url="https://pypi.org/packages/3b/ff/33a4ccc778c56d2ab9845b5ea09ab15d368ac39fa945f0bd2bd2724e18e8/flash_attn-2.5.5.tar.gz")
    version("2.5.4", sha256="d83bb427b517b07e9db655f6e5166eb2607dccf4d6ca3229e3a3528c206b0175", url="https://pypi.org/packages/4e/7b/b42299ad0edf4d185c883dcf83d4f31bf577e8e86f20e70b8ea8ebc0d75d/flash_attn-2.5.4.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.7:")
    # END DEPENDENCIES

