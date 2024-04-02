# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyNeptuneClient(PythonPackage):
    # BEGIN VERSIONS
    version("0.16.7", sha256="9b8bf2f59cb6b7ed6d96ea221b68ea20d9d481a1a4672d8173648ef998134454", url="https://pypi.org/packages/cd/0a/d6482f5c866dbe09484c8197d9c6e57f7e16cdbbea6f629b963dea73bb3e/neptune-client-0.16.7.tar.gz")
    version("0.16.1", sha256="821238f510486feacd87c745f4646916259a416545ab678b47195729c071f249", url="https://pypi.org/packages/62/a2/11eb2fe163a0b5d46d1ec0e90c71a3d76d7203ddd2923563934ef58f0599/neptune-client-0.16.1.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.7:", when="@0.16:0.16.11")
    # END DEPENDENCIES

