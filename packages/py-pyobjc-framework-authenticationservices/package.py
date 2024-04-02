# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkAuthenticationservices(PythonPackage):
    # BEGIN VERSIONS
    version("10.2", sha256="1be0f05458c4ebfc3e018cb59b4a8bd9022c42b18fea449b0fbf5def0b5f7ef7", url="https://pypi.org/packages/41/98/6c874be70ae4fc24936ac8d90cf1fbfcdaeff484444080b35cd04fc2adf8/pyobjc-framework-AuthenticationServices-10.2.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.8:", when="@10:")
        depends_on("py-pyobjc-core@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-cocoa@10.2:", when="@10.2:")
    # END DEPENDENCIES

