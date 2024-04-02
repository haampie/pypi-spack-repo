# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyLpips(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.1.4", sha256="fd537af5828b69d2e6ffc0a397bd506dbc28ca183543617690844c08e102ec5e", url="https://pypi.org/packages/9b/13/1df50c7925d9d2746702719f40e864f51ed66f307b20ad32392f1ad2bb87/lpips-0.1.4-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-numpy@1.14.3:", when="@0.1.4:")
        depends_on("py-scipy@1.0.1:", when="@0.1.4:")
        depends_on("py-torch@0.4:", when="@0.1.4:")
        depends_on("py-torchvision@0.2.1:", when="@0.1.4:")
        depends_on("py-tqdm@4.28.1:", when="@0.1.4:")
    # END DEPENDENCIES

