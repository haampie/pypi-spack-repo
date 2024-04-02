# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkSystemconfiguration(PythonPackage):
    # BEGIN VERSIONS
    version("10.2", sha256="e9ec946ca56514a68e28040c55c79ba105c9a70b56698635767250e629c37e49", url="https://pypi.org/packages/12/4a/409177e9530ba9334c2014c5e7ef7a016950da88a12c9ccd5d36fc65b4d6/pyobjc-framework-SystemConfiguration-10.2.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.8:", when="@10:")
        depends_on("py-pyobjc-core@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-cocoa@10.2:", when="@10.2:")
    # END DEPENDENCIES

