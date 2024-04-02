# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkScreencapturekit(PythonPackage):
    # BEGIN VERSIONS
    version("10.2", sha256="86f64377be94db1b95e77ca53301ed94c0a7a82c0251c9e960bcae24b6a5841b", url="https://pypi.org/packages/ea/5b/7a4dab5183278819464b6f698b352428235ab1c6618e06f1a64100db290f/pyobjc-framework-ScreenCaptureKit-10.2.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.8:", when="@10:")
        depends_on("py-pyobjc-core@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-cocoa@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-coremedia@10.2:", when="@10.2:")
    # END DEPENDENCIES

