# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkSafariservices(PythonPackage):
    # BEGIN VERSIONS
    version("10.2", sha256="723de09afb718b05d03cbbed42f90d36356294b038ca6422c88d50240047b067", url="https://pypi.org/packages/19/dd/df3b26cd620ec9dcb7ce58c6ceb67831fb1f430e36e9c4f5b582ffe9b62a/pyobjc-framework-SafariServices-10.2.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.8:", when="@10:")
        depends_on("py-pyobjc-core@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-cocoa@10.2:", when="@10.2:")
    # END DEPENDENCIES

