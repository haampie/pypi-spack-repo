# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyRepozeLru(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.7", sha256="f77bf0e1096ea445beadd35f3479c5cff2aa1efe604a133e67150bc8630a62ea", url="https://pypi.org/packages/b0/30/6cc0c95f0b59ad4b3b9163bff7cdcf793cc96fac64cf398ff26271f5cf5e/repoze.lru-0.7-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    variant("docs", default=False, description="docs")
    # END VARIANTS

    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-sphinx", when="@0.7:+docs")
    # END DEPENDENCIES

