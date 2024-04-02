# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkPhotosui(PythonPackage):
    # BEGIN VERSIONS
    version("10.2", sha256="d0bbcae82b4cc652bb60d3221c557cc19be62ff430575ec8e6d233beb936f73b", url="https://pypi.org/packages/f5/ad/d727d4eca6a4222f50bb1fb706ec3bb6977b315d929dd889365277cd8c27/pyobjc-framework-PhotosUI-10.2.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.8:", when="@10:")
        depends_on("py-pyobjc-core@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-cocoa@10.2:", when="@10.2:")
    # END DEPENDENCIES

