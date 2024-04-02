# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyColossalai(PythonPackage):
    # BEGIN VERSIONS
    version("0.1.3", sha256="f25ffd313e62b2cb8f97c57f25fafb0e9f59ec7bd1d1bf6e8d8483f9b0082d33", url="https://pypi.org/packages/ab/af/295b4ef91a36d5692104416a5463a6a18d029cb0fe2cf9026e4ffad1b08d/colossalai-0.1.3.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.7:", when="@0.1.1:0.1.3")
    # END DEPENDENCIES

