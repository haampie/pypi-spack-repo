# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyupgrade(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("3.3.1", sha256="3b93641963df022d605c78aeae4b5956a5296ea24701eafaef9c487527b77e60", url="https://pypi.org/packages/31/ee/dda0d7b86c4c0cd02494566243ad14f152e10994f1c345d57e9b9edd0c8a/pyupgrade-3.3.1-py2.py3-none-any.whl")
    version("2.31.1", sha256="4060a7c20c79d373a3dcf34566b275c6de6cd2b034ad22465d3263fb0de82648", url="https://pypi.org/packages/87/c5/5db2c423c83b9369f5985d2a9ca9318524756c028b46ab1827e15807e306/pyupgrade-2.31.1-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.8.1:", when="@3.9:")
        depends_on("py-tokenize-rt@3.2:", when="@1.20.2:2.38.2,3:3.9")
    # END DEPENDENCIES

