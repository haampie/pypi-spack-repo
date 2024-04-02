# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyTorchCluster(PythonPackage):
    # BEGIN VERSIONS
    version("1.6.3", sha256="78d5a930a5bbd0d8788df8c6d66addd68d6dd292fe3edb401e3dacba26308152", url="https://pypi.org/packages/54/31/e7f7a28253cd907404eb652607613b35779140b326d15d0636511b7b9438/torch_cluster-1.6.3.tar.gz")
    version("1.5.8", sha256="a0a32f63faac40a026ab1e9da31f6babdb4d937e53be40bd1c91d9b5a286eee6", url="https://pypi.org/packages/ff/39/6524367aed276171ba66675b25b368c1522e1d35e17b96ee4ff4025e1d98/torch_cluster-1.5.8.tar.gz")
    version("1.5.7", sha256="62a3ec1bebadda1a4a2c867203f4c957b9c0b9d11ffb03b40b8ea9f95a0a4d3b", url="https://pypi.org/packages/ff/78/66d8a75aea9d671dc25a7368fd6e86d1e43c4c47c3dd3d68df16dde57837/torch_cluster-1.5.7.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    variant("cuda", default=False, description="cuda")
    # END VARIANTS

    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.8:", when="@1.6.2:")
    # END DEPENDENCIES

