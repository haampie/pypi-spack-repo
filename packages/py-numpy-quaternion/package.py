# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyNumpyQuaternion(PythonPackage):
    # BEGIN VERSIONS
    version("2021.11.4.15.26.3", sha256="b0dc670b2adc8ff2fb8d6105a48769873f68d6ccbe20af6a19e899b1e8d48aaf", url="https://pypi.org/packages/45/d8/6fb78d8f9e9c5de52908bcbc7ca08ab7b770aa0a1078b71615f3b46aed1b/numpy-quaternion-2021.11.4.15.26.3.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    variant("numba", default=False)
    variant("scipy", default=False)
    # END VARIANTS

    # BEGIN DEPENDENCIES
    # END DEPENDENCIES

