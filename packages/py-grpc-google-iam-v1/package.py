# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyGrpcGoogleIamV1(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.13.0", sha256="53902e2af7de8df8c1bd91373d9be55b0743ec267a7428ea638db3775becae89", url="https://pypi.org/packages/66/a0/d27ec874fb0a86b3609b73161a15cf633924888afa05c1673b3ab5a6c3f4/grpc_google_iam_v1-0.13.0-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-googleapis-common-protos@1.56:+grpc", when="@0.12.4-beta1:")
        depends_on("py-grpcio@1.44.0:", when="@0.12.6:")
        depends_on("py-protobuf@3.19.5:3.20.0-rc2,3.20.1-rc1,3.20.2:4.21.0,4.21.6:4", when="@0.12.6:")
    # END DEPENDENCIES

