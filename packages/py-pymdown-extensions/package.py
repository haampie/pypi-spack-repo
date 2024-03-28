# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPymdownExtensions(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("9.5", sha256="ec141c0f4983755349f0c8710416348d1a13753976c028186ed14f190c8061c4", url="https://pypi.org/packages/f1/e0/1ed09f66cd1648f8e009120debf9b7d67596fb688e53e71522da1daa02a0/pymdown_extensions-9.5-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-markdown@3.2:", when="@7.0-rc1,7.1:10.4")
    # END DEPENDENCIES

