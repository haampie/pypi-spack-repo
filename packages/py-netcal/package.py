# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyNetcal(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("1.3.5", sha256="3c3ae5ea35786878c3a979ad5a0f7192d89e7c53d0b3ab76ed27e227dd18d6cd", url="https://pypi.org/packages/12/a6/fd7aa37d5d613216637976f4f121270bc1781d1ad4ac3bf981f34a45b1c0/netcal-1.3.5-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-gpytorch@1.5.1:", when="@1.3:")
        depends_on("py-matplotlib@3.3.0:", when="@1.3:")
        depends_on("py-numpy@1.18.0:", when="@1.3:")
        depends_on("py-pyro-ppl@1.8:", when="@1.3:")
        depends_on("py-scikit-learn@0.24.0:", when="@1.3:")
        depends_on("py-scipy@1.4.0:", when="@1.3:")
        depends_on("py-tensorboard@2.2:", when="@1.2:")
        depends_on("py-tikzplotlib@0.9.8", when="@1.3:")
        depends_on("py-torch@1.9:", when="@1.3:")
        depends_on("py-torchvision@0.10:", when="@1.3:")
        depends_on("py-tqdm@4.40:", when="@1.2:")
    # END DEPENDENCIES

