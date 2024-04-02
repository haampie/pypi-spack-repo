# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkDiskarbitration(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("10.2", sha256="dd14eb448865ca4c49e15a543f748f1ef6501ea0044eaa2cf04860547205c84f", url="https://pypi.org/packages/cc/f8/87aa1bcc317badb20e4e17a2acc42a3f5b14963fe4b34ebaae29672c9b64/pyobjc_framework_DiskArbitration-10.2-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.8:", when="@10:")
        depends_on("py-pyobjc-core@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-cocoa@10.2:", when="@10.2:")
    # END DEPENDENCIES

