# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyTensorstore(PythonPackage):
    # BEGIN VERSIONS
    version("0.1.54", sha256="e1a9dcb0be7c828f752375409537d4b39c658dd6c6a0873fe21a24a556ec0e2a", url="https://pypi.org/packages/9b/83/39928c1569007a734006b5ac2eaba26d8751cd292cff9d06887c0de97003/tensorstore-0.1.54.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.9:", when="@0.1.46:")
    # END DEPENDENCIES

