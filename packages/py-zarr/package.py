# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyZarr(PythonPackage):
    # BEGIN VERSIONS
    version("2.17.0", sha256="d287cb61019c4a0a0f386f76eeaa7f0b1160b1cb90cf96173a4b6cbc135df6e1", url="https://pypi.org/packages/f1/69/ecaaa497d704c58621d0828bd1336d8040e09c94e822ca8d28410fbdeff2/zarr-2.17.0-py3-none-any.whl")
    version("2.10.2", sha256="10e67dc6163b08497ce0a0d6dfe1ed07f71d5abfcb040f5b7eeb5d33ebf5da3e", url="https://pypi.org/packages/42/17/9aef39c229de767ffc320e43a73e98983e9f941b0fbd10dba1fd09fe0168/zarr-2.10.2-py3-none-any.whl")
    version("2.6.1", sha256="e4eb501ff472cf97b7e497a504a2fb818d6d3bff398997bcfe9438c2cc1a3665", url="https://pypi.org/packages/60/67/d69a3fcd34254df8dce23e1a4d570509f8a373fc58e40cb8681cf26795f6/zarr-2.6.1-py3-none-any.whl")
    version("2.5.0", sha256="f86c95fef1442d974adae3269c0b5a5e5200f0d46b6572bad6a9ee2c1a262478", url="https://pypi.org/packages/22/17/37cc7afabdec7b5759d68fab0bc5afd950799a4ce2189826caf5ee087414/zarr-2.5.0-py3-none-any.whl")
    version("2.4.0", sha256="53aa21b989a47ddc5e916eaff6115b824c0864444b1c6f3aaf4f6cf9a51ed608", url="https://pypi.org/packages/a3/87/383d77399148ef0772da3472b513ecf143252e7c365c51b0f06714800366/zarr-2.4.0.tar.gz")
    version("2.3.2", sha256="c62d0158fb287151c978904935a177b3d2d318dea3057cfbeac8541915dfa105", url="https://pypi.org/packages/d0/d0/02a3457f4e86a8f74104e7686c43b6bf0c76534b626f174eb20786a6f781/zarr-2.3.2.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.9:", when="@2.17:")
        depends_on("python@3.7:3", when="@2.9:2.12")
        depends_on("python@:3", when="@2.6:2.8")
        depends_on("py-asciitree", when="@2.5:")
        depends_on("py-fasteners", when="@2.5:")
        depends_on("py-numcodecs@0.10.0:", when="@2.13.0:")
        depends_on("py-numcodecs@0.6.4:", when="@2.5:2.13.0-alpha2")
        depends_on("py-numpy@1.21.1:", when="@2.17:")
        depends_on("py-numpy@1.7:", when="@2.5:2.13.3")
    # END DEPENDENCIES

