# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkAvfoundation(PythonPackage):
    # BEGIN VERSIONS
    version("10.2", sha256="4d394014f2477c0c6a596dbb01ef5d92944058d0e0d954ce6121a676ae9395ce", url="https://pypi.org/packages/e1/10/f0867dcd21afac4edc6d6435e0ab65743503143a911de1ab80648346d3b4/pyobjc-framework-AVFoundation-10.2.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.8:", when="@10:")
        depends_on("py-pyobjc-core@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-cocoa@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-coreaudio@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-coremedia@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-quartz@10.2:", when="@10.2:")
    # END DEPENDENCIES

