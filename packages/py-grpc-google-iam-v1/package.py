# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyGrpcGoogleIamV1(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.13.0", sha256="53902e2af7de8df8c1bd91373d9be55b0743ec267a7428ea638db3775becae89", url="https://pypi.org/packages/66/a0/d27ec874fb0a86b3609b73161a15cf633924888afa05c1673b3ab5a6c3f4/grpc_google_iam_v1-0.13.0-py2.py3-none-any.whl")
    version("0.13.0-rc1", sha256="1a8e37e9661e792f9d2968ba70b04d3ee364fda6f002f76d04788f76c7cb4d1e", url="https://pypi.org/packages/ec/74/6474d80e78bb4ba9efd084b09cad64592eb40277aaf2a98910b8c0fba824/grpc_google_iam_v1-0.13.0rc1-py2.py3-none-any.whl")
    version("0.12.7", sha256="834da89f4c4a2abbe842a793ed20fc6d9a77011ef2626755b1b89116fb9596d7", url="https://pypi.org/packages/5f/4b/404f59d065a410e835576433bc296599ae093460c7724fa5d5ca2354a885/grpc_google_iam_v1-0.12.7-py2.py3-none-any.whl")
    version("0.12.6", sha256="5c10f3d8dc2d88678ab1a9b0cb5482735c5efee71e6c0cd59f872eef22913f5c", url="https://pypi.org/packages/34/72/c84e54991d452942c5a85474693c8433169104a596e9dd23b05c5f091894/grpc_google_iam_v1-0.12.6-py2.py3-none-any.whl")
    version("0.12.4", sha256="312801ae848aeb8408c099ea372b96d253077e7851aae1a9e745df984f81f20c", url="https://pypi.org/packages/49/cb/5c7a8cf8211475908b9d101d160f02b9fb3f3062302625227e8724db36b3/grpc_google_iam_v1-0.12.4-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-googleapis-common-protos@1.56:+grpc", when="@0.12.4-beta1:")
        depends_on("py-grpcio@1.44.0:", when="@0.12.6:")
        depends_on("py-grpcio@1.0.0:", when="@0.12.4-beta1:0.12.4")
        depends_on("py-protobuf@3.19.5:3.20.0-rc2,3.20.1-rc1,3.20.2:4.21.0,4.21.6:4", when="@0.12.6:")
    # END DEPENDENCIES

