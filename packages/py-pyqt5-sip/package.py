# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyqt5Sip(PythonPackage):
    # BEGIN VERSIONS
    version("12.13.0", sha256="7f321daf84b9c9dbca61b80e1ef37bdaffc0e93312edae2cd7da25b953971d91", url="https://pypi.org/packages/ee/81/fce2a475aa56c1f49707d9306b930695b6ff078c2242c9f2fd72a3214e1f/PyQt5_sip-12.13.0.tar.gz")
    version("12.12.1", sha256="8fdc6e0148abd12d977a1d3828e7b79aae958e83c6cb5adae614916d888a6b10", url="https://pypi.org/packages/c1/61/4055e7a0f36339964956ff415e36f4abf82561904cc49c021da32949fc55/PyQt5_sip-12.12.1.tar.gz")
    version("12.9.0", sha256="d3e4489d7c2b0ece9d203ae66e573939f7f60d4d29e089c9f11daa17cfeaae32", url="https://pypi.org/packages/b1/40/dd8f081f04a12912b65417979bf2097def0af0f20c89083ada3670562ac5/PyQt5_sip-12.9.0.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.7:", when="@12.10.1:")
    # END DEPENDENCIES

