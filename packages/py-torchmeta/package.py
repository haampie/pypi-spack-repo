# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyTorchmeta(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("1.7.0", sha256="a53276ca10a59ec88c23bb3c1871cdeb5eadc1da5ac2e0bb102533e157f55910", url="https://pypi.org/packages/3e/76/b380f7b39ebbbf7fc50e016e6755523dd1194bcb39deee88acf3bb9e7b0f/torchmeta-1.7.0-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-h5py", when="@1.4.4:")
        depends_on("py-numpy@1.14.0:")
        depends_on("py-ordered-set", when="@1.4.5:")
        depends_on("py-pillow@7:")
        depends_on("py-requests")
        depends_on("py-torch@1.4:1.8", when="@1.7")
        depends_on("py-torchvision@0.5:0.9", when="@1.7")
        depends_on("py-tqdm@4:")
    # END DEPENDENCIES

