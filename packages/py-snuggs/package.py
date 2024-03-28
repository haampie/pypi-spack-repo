# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PySnuggs(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("1.4.7", sha256="988dde5d4db88e9d71c99457404773dabcc7a1c45971bfbe81900999942d9f07", url="https://pypi.org/packages/cc/0e/d27d6e806d6c0d1a2cfdc5d1f088e42339a0a54a09c3343f7f81ec8947ea/snuggs-1.4.7-py3-none-any.whl")
    version("1.4.6", sha256="5ac04dadd8ba20e70ab2a0d565fe2e1a7347635aa2aaf3650d1551b1ef941994", url="https://pypi.org/packages/58/14/8e90b7586ab6929861161e73e9fd55637a060e4d14dd1be14a4b8a08751f/snuggs-1.4.6-py3-none-any.whl")
    version("1.4.5", sha256="2fc919d4271fbc5e9b7e28ebffdd793c83b63f553c1e3451dd5764194cbabfa8", url="https://pypi.org/packages/71/45/ba56f5be5357c5ad60aa89c1cc483c6c969d33f4effa2b5d50e8df395b4d/snuggs-1.4.5-py3-none-any.whl")
    version("1.4.4", sha256="27655ea49423262b96915ec0f26f0daf9548a3ad99af5aa87830e26dceea633b", url="https://pypi.org/packages/1d/77/d718ecb2de2f34e6e21c247cc43cf5eb943e2bc4a7f959df467c5060c64b/snuggs-1.4.4-py3-none-any.whl")
    version("1.4.3", sha256="1c06f68cfa5f700339ba000875049f87b394679aa1dd06fc64af71e446caf4a6", url="https://pypi.org/packages/a5/8a/abb0803f05feb4401ab9e4c776ce11f0048b6cb0f2d84ace97cd93d7da04/snuggs-1.4.3-py3-none-any.whl")
    version("1.4.2", sha256="0ae01783adeaa6948352fc474605da78d277da545b2315f6d2febe0f065bab02", url="https://pypi.org/packages/53/af/e6c28e9062894e1115f629ed43c8a7a8ea285ede2901d56424faf42ae1d0/snuggs-1.4.2-py3-none-any.whl")
    version("1.4.1", sha256="ef38fd4400b96f3999c928396102e65d3b0aa2f22bbc2c5fa49e151608368487", url="https://pypi.org/packages/23/dd/f8a42549be3f02af7f1edd583b4b0a7e946e330aa2cef48a9bd2f43b87fa/snuggs-1.4.1-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-click", when="@1.1:1.4.2")
        depends_on("py-numpy", when="@1.1:")
        depends_on("py-pyparsing@2.1.6:", when="@1.4.5:")
        depends_on("py-pyparsing", when="@1.1:1.4.4")
    # END DEPENDENCIES

