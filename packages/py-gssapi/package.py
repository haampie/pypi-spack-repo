# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyGssapi(PythonPackage):
    # BEGIN VERSIONS
    version("1.8.2", sha256="b78e0a021cc91158660e4c5cc9263e07c719346c35a9c0f66725e914b235c89a", url="https://pypi.org/packages/27/71/5110b5af9354e5eb66a30dbaa6bac2a5e3013057120544830a849dbd087b/gssapi-1.8.2.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.7:", when="@1.8.1:")
    # END DEPENDENCIES

