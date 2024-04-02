# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkImagecapturecore(PythonPackage):
    # BEGIN VERSIONS
    version("10.2", sha256="68f1f96982282e786c9c387c177c3b14202d560d68000136562eba1ed3f45a6e", url="https://pypi.org/packages/38/ac/b779c127c35f8f8888cf3636eb853777158d22166e937746040f5d35c252/pyobjc-framework-ImageCaptureCore-10.2.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.8:", when="@10:")
        depends_on("py-pyobjc-core@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-cocoa@10.2:", when="@10.2:")
    # END DEPENDENCIES

