# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PySshtunnel(PythonPackage):
    # BEGIN VERSIONS
    version("0.1.5", sha256="5eee2e414c3fd9e9ef5d058bebece272a6aae928849ef7f2d9561b7fffab7aea", url="https://pypi.org/packages/38/7d/6f19be1ee49cee9593c5ac3aa1fb38fe30eaf1520114e08dee2ab2a45855/sshtunnel-0.1.5-py2.py3-none-any.whl")
    version("0.1.4", sha256="f29ae41a1bd3afa64e9a31029bece2966e4be9a9641e8262372741e691c40d76", url="https://pypi.org/packages/bf/8d/385c7e7c90e17934b3102ad2902e224c27a7173a6a57ef4805dcef8043b1/sshtunnel-0.1.4.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-paramiko@1.15.2:", when="@0.1.3:0.1.3.0,0.1.5:0.3")
    # END DEPENDENCIES

