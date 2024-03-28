# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyJpype1(PythonPackage):
    # BEGIN VERSIONS
    version("0.6.3", sha256="6841523631874a731e1f94e1b1f130686ad3772030eaa3b6946256eeb1d10dd1", url="https://pypi.org/packages/c4/4b/60a3e63d51714d4d7ef1b1efdf84315d118a0a80a5b085bb52a7e2428cdc/JPype1-0.6.3.tar.gz")
    version("0.6.2", sha256="99206412d80b9d5a81a7cc205267ca63554403eb57f13420302e2f39bfad7f25", url="https://pypi.org/packages/d2/c2/cda0e4ae97037ace419704b4ebb7584ed73ef420137ff2b79c64e1682c43/JPype1-0.6.2.tar.gz")
    version("0.6.1", sha256="0d366228b7b37b0266184161cc7ea1ce58f60199f6ec9451985149ea873774be", url="https://pypi.org/packages/3c/94/b620c0e0143c864141ea572a7ad831d8233d84d5702cef692bc039f1c9c1/JPype1-0.6.1.tar.gz")
    version("0.6.0", sha256="f5d783520cb4c30595c3bc509065e30fc292ec7cfb57045141eae77c518bcdb0", url="https://pypi.org/packages/83/3a/ca1b519c9c27cc556286d67f0288f0c2e060e5ba6b99cea0248b33f851a5/JPype1-0.6.0.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    variant("numpy", default=False)
    # END VARIANTS

    # BEGIN DEPENDENCIES
    # END DEPENDENCIES

