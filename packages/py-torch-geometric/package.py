# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyTorchGeometric(PythonPackage):
    # BEGIN VERSIONS
    version("2.1.0.post1", sha256="32347402076ccf60fa50312825178f1e3e5ce5e7b3b3a8b2729ac699da24525d", url="https://pypi.org/packages/bd/e3/3913bc65cb23db1dcc5a69a87f53206ebcdfebc28973535a4a64a0cb97cd/torch_geometric-2.1.0.post1.tar.gz")
    version("1.6.3", sha256="347f693bebcc8a621eda4867dafab91c04db5f596d7ed7ecb89b242f8ab5c6a1", url="https://pypi.org/packages/59/5c/3e95b76321fb14f24cc2ace392075717f645c4632e796ee0db1bc7d17231/torch_geometric-1.6.3.tar.gz")
    version("1.6.0", sha256="fbf43fe15421c9affc4fb361ba4db55cb9d3c64d0c29576bb58d332bf6d27fef", url="https://pypi.org/packages/8e/18/93b190226d09958be96919fd50c55d28f83f1a1b9260a2b33499f9d86728/torch_geometric-1.6.0.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    variant("cuda", default=False, description="cuda")
    # END VARIANTS

    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.7:", when="@2.0.4:2.3")
    # END DEPENDENCIES

