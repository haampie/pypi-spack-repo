# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyerfa(PythonPackage):
    # BEGIN VERSIONS
    version("2.0.0.1", sha256="2fd4637ffe2c1e6ede7482c13f583ba7c73119d78bef90175448ce506a0ede30", url="https://pypi.org/packages/78/fd/0148f0e54f0c6f48a141409df65d74a5f1dae2e139f23d50a43c58c16098/pyerfa-2.0.0.1.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.9:", when="@2.0.1:")
    # END DEPENDENCIES

