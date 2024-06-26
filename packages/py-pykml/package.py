# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPykml(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.2.0", sha256="bd4e259527a88c3b3d0d264c133b8b05bfc457efca37467f7f891b6be937d60e", url="https://pypi.org/packages/b8/22/8b3e7aec303a3d11bc62de04d863cf2092d7a722ade35809f7f6232df164/pykml-0.2.0-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-lxml@3.3.6:", when="@0.2:")
    # END DEPENDENCIES

