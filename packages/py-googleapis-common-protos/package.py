# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyGoogleapisCommonProtos(PythonPackage):
    # BEGIN VERSIONS
    version("1.58.0", sha256="ca3befcd4580dab6ad49356b46bf165bb68ff4b32389f028f1abd7c10ab9519a", url="https://pypi.org/packages/32/4e/ed585842aaa704d87495a0e99317aaa44c5007a597c05b995fa8cfc4dfbe/googleapis_common_protos-1.58.0-py2.py3-none-any.whl")
    version("1.55.0", sha256="183bb0356bd614c4330ad5158bc1c1bcf9bcf7f5e7f911317559fe209496eeee", url="https://pypi.org/packages/50/a9/6c76954ad5ee88c749407b282e5dfa724e3bd3065a069bcbe6a3da08a3e3/googleapis_common_protos-1.55.0-py2.py3-none-any.whl")
    version("1.6.0", sha256="e61b8ed5e36b976b487c6e7b15f31bb10c7a0ca7bd5c0e837f4afab64b53a0c6", url="https://pypi.org/packages/eb/ee/e59e74ecac678a14d6abefb9054f0bbcb318a6452a30df3776f133886d7d/googleapis-common-protos-1.6.0.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    variant("grpc", default=False)
    # END VARIANTS

    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-grpcio@1.44.0:", when="@1.57:1.61,1.62.0-rc2:+grpc")
        depends_on("py-grpcio@1.0.0:", when="@1.52:1.56.1+grpc")
        depends_on("py-protobuf@3.19.5:3.20.0-rc2,3.20.1-rc1,3.20.2:4.21.0,4.21.6:4", when="@1.57:")
        depends_on("py-protobuf@3.12.0:", when="@1.53:1.56.0")
    # END DEPENDENCIES

