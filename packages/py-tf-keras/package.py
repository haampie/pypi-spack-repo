# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyTfKeras(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("2.16.0", sha256="b2ad0541fa7d9e92c4b7a1b96593377afb58aaff374299a6ca6be1a42f51d899", url="https://pypi.org/packages/75/aa/cf09f8956d4f276f655b13674e15d8d6015fd832f9689aa9ff2a515781ab/tf_keras-2.16.0-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.9:", when="@2.16:")
        depends_on("py-tensorflow@2.16.0:", when="@2.16.0:")
    # END DEPENDENCIES

