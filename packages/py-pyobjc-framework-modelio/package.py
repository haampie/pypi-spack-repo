# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkModelio(PythonPackage):
    # BEGIN VERSIONS
    version("10.2", sha256="8ae1444375260a346d1c77838f84e2c04dfabaf2769b2970a3588becb670431e", url="https://pypi.org/packages/2e/bf/b3def866d117da921fc64eb15d94dc949da497f60c6f9b22cc3628ec9b6b/pyobjc-framework-ModelIO-10.2.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.8:", when="@10:")
        depends_on("py-pyobjc-core@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-cocoa@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-quartz@10.2:", when="@10.2:")
    # END DEPENDENCIES

