# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyGoogleCloudLogging(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("3.9.0", sha256="094a2db068ff7f38c9e0c1017673fa49c0768fbae02769e03e06baa30f138b87", url="https://pypi.org/packages/a9/94/24603046ca57f88a0602dd682fce99282c62be1b4e90e1316974f7cb1691/google_cloud_logging-3.9.0-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-google-api-core@1.33.2:1,2.8:+grpc", when="@3.4:3.9")
        depends_on("py-google-cloud-appengine-logging", when="@2.7:")
        depends_on("py-google-cloud-audit-log", when="@2.5:")
        depends_on("py-google-cloud-core@2.0.0:", when="@3.2:")
        depends_on("py-grpc-google-iam-v1@0.12.4:", when="@3.1.2:")
        depends_on("py-proto-plus@1.22.2:", when="@3.5: ^python@3.11:")
        depends_on("py-proto-plus@1.22:", when="@3.2.2:")
        depends_on("py-protobuf@3.19.5:3.20.0-rc2,3.20.1-rc1,3.20.2:4.21.0-rc2,4.21.6:4", when="@3.4:")
    # END DEPENDENCIES

