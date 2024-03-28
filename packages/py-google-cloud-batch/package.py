# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyGoogleCloudBatch(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.17.11", sha256="c5efcefae0736b5aa80c3f29b9e1b18ab401407c08dd0d21a60ffdd6b2eb7b63", url="https://pypi.org/packages/d9/66/af0a14a43f244f837962b31571ece429bfd62e85a4e3e9e5db24814ec3ac/google_cloud_batch-0.17.11-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-google-api-core@1.34:1,2.11:+grpc", when="@0.5:0.17.11")
        depends_on("py-google-auth@2.14.1:", when="@0.17.11:0.17.13")
        depends_on("py-proto-plus@1.22.3:", when="@0.17.6-rc0:")
        depends_on("py-protobuf@3.19.5:3.20.0-rc2,3.20.1-rc1,3.20.2:4.21.0-rc2,4.21.6:4", when="@0.3.2:")
    # END DEPENDENCIES

