# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyTorchComplex(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.4.3", sha256="283a61a65fdcfcdadb8234540c6d4a621d02832f20ab8f980f08bc4f20eec8c3", url="https://pypi.org/packages/9e/35/1ded2af76633aa9b2e875033265e6bc74e444fc8a78af48108ffe77b14cf/torch_complex-0.4.3-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-numpy")
    # END DEPENDENCIES

