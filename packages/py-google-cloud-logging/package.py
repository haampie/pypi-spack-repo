##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyGoogleCloudLogging(PythonPackage):
    version("3.10.0", sha256="132192beb45731130a2ffbcd4b2b5cbd87370e7dcfa7397ae4002154f542bd20", url="https://pypi.org/packages/02/51/74aea3a6134345572064884d01f811afa3f933b31ddca98ac03b2c6bdb14/google_cloud_logging-3.10.0-py2.py3-none-any.whl")
    version("3.9.0", sha256="094a2db068ff7f38c9e0c1017673fa49c0768fbae02769e03e06baa30f138b87", url="https://pypi.org/packages/a9/94/24603046ca57f88a0602dd682fce99282c62be1b4e90e1316974f7cb1691/google_cloud_logging-3.9.0-py2.py3-none-any.whl")
    version("3.9.0-rc1", sha256="8321c728c0ed0e96d25684084be97402c5409d71f8db6dcfbfd97c64cf477b1d", url="https://pypi.org/packages/76/b0/ffaac82a9ccc5ae9de6a7b5a2d7c8febc850f87add68b5b05bd1473b7971/google_cloud_logging-3.9.0rc1-py2.py3-none-any.whl")
    version("3.8.0", sha256="c868b276b021cf5f32b6e8356b6cb3666357d149ad0fd798076043a5ec7ed988", url="https://pypi.org/packages/b0/90/08669c4471bf9d9cfd51b5533c3b197a2c19f36c65747ee82f522275f9cc/google_cloud_logging-3.8.0-py2.py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-google-api-core@1.34.1:1,2.11:+grpc", when="@3.10:")
        depends_on("py-google-api-core@1.33.2:1,2.8:+grpc", when="@3.4:3.9")
        depends_on("py-google-auth@2.14.1:2.23,2.25.1:", when="@3.10:")
        depends_on("py-google-cloud-appengine-logging", when="@2.7:")
        depends_on("py-google-cloud-audit-log", when="@2.5:")
        depends_on("py-google-cloud-core@2.0.0:", when="@3.2:")
        depends_on("py-grpc-google-iam-v1@0.12.4:", when="@3.1.2:")
        depends_on("py-proto-plus@1.22.2:", when="@3.5: ^python@3.11:")
        depends_on("py-proto-plus@1.22:", when="@3.2.2:")
        depends_on("py-protobuf@3.19.5:3.20.0-rc2,3.20.1-rc1,3.20.2:4.21.0-rc2,4.21.6:4", when="@3.4:")

