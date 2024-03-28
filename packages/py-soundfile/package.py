# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PySoundfile(PythonPackage):
    # BEGIN VERSIONS
    version("0.10.3.post1", sha256="490cff42650733d1832728b937fe99fa1802896f5ef4d61bcf78cf7ebecb107b", url="https://pypi.org/packages/bc/7c/440d411e1bf2ef40ec450bb65a2b85ed8b23aaf12b7a99a1888ab551029c/SoundFile-0.10.3.post1.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    variant("numpy", default=False)
    # END VARIANTS

    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-cffi@1:", when="@0.10")
        depends_on("py-numpy", when="@0.10+numpy")
    # END DEPENDENCIES

