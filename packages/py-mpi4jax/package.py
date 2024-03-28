# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyMpi4jax(PythonPackage):
    # BEGIN VERSIONS
    version("0.3.11.post3", sha256="ad4c5840c81ead40b68f4885d705c06eeca22cd4e998790de589c6566db75a75", url="https://pypi.org/packages/e6/f5/9a273e2dea6982c15f4786ff234e063bce9ed0707eebb8bf645a2dd1b283/mpi4jax-0.3.11.post3.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    variant("cuda", default=False)
    variant("cuda_arch", default=False)
    # END VARIANTS

    # BEGIN DEPENDENCIES
    # END DEPENDENCIES

