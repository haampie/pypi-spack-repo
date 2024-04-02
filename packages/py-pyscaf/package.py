# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyscaf(PythonPackage):
    # BEGIN VERSIONS
    version("0.12-alpha4", sha256="3ce3f6fe80bd058831b6a38a56d464ef10f3ebbdd6bc3dcb0d7f127c0b2c1b36", url="https://pypi.org/packages/ee/52/a947347d00c323a87588d6b6d5ad54b3656a5df2f3bcaad477833a43d1f6/pyScaf-0.12a4.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-fastaindex")
    # END DEPENDENCIES

