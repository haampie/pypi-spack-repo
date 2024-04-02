# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyTorchScatter(PythonPackage):
    # BEGIN VERSIONS
    version("2.0.5", sha256="148fbe634fb9e9465dbde2ab337138f63650ed8abbac42bb3f565e3fe92e9b2f", url="https://pypi.org/packages/01/45/cd93ed3227248773ba8bc4b3beaa04e8bddb127a793a41bad875369951b3/torch_scatter-2.0.5.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    variant("cuda", default=False, description="cuda")
    # END VARIANTS

    # BEGIN DEPENDENCIES
    # END DEPENDENCIES

