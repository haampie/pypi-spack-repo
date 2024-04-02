# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyTorchSparse(PythonPackage):
    # BEGIN VERSIONS
    version("0.6.17", sha256="06e268dd77f73eb641da8f9383306d7afac6423383c9197b9df120955e2a96bd", url="https://pypi.org/packages/cb/ff/21d4674bdf232cd7a2bdbbbb04c35ba1cbdf444d4f3331f5d7eb6c5d4a8f/torch_sparse-0.6.17.tar.gz")
    version("0.6.8", sha256="312fb5ae6e4e575fca4bbc0bd092af85e7679d5b8e53459f24492fc2a073c7b6", url="https://pypi.org/packages/3c/dd/f34dce6512a3922948c3ac0cf50cceb2eeafeedd34a278d502eb77d07dc0/torch_sparse-0.6.8.tar.gz")
    version("0.6.7", sha256="f69b2ed35baf2a9853234756a2b19e6f7ce88d2c1f029d1c7ca166d91e1adbd0", url="https://pypi.org/packages/ce/c0/f5ccc280629765cf1e97b601426cad6170d00603cf9836ba52f85d44ac27/torch_sparse-0.6.7.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    variant("cuda", default=False, description="cuda")
    # END VARIANTS

    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.7:", when="@0.6.13:0.6.17")
    # END DEPENDENCIES

