# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyFastcore(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("1.3.27", sha256="03c6c93f2c769fdd611e32a7cc1433db5a82f67146d9e2f88e03107db203f6de", url="https://pypi.org/packages/50/2b/832378cc02c608798fe13baec2709e70e3796459e6936c4bd3ee7edc4345/fastcore-1.3.27-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-packaging")
        depends_on("py-pip")
    # END DEPENDENCIES

