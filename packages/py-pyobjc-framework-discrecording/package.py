# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkDiscrecording(PythonPackage):
    # BEGIN VERSIONS
    version("10.2", sha256="9670018a0970553882feb10e066585ad791c502539712f4117bad4a6647c79b3", url="https://pypi.org/packages/c4/a1/0cdd58c3180fd705f1a206991b0eb3d0f3dde17dc246d2d5e786d310ab77/pyobjc-framework-DiscRecording-10.2.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.8:", when="@10:")
        depends_on("py-pyobjc-core@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-cocoa@10.2:", when="@10.2:")
    # END DEPENDENCIES

