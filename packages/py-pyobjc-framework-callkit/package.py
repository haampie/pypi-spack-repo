# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkCallkit(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("10.2", sha256="f3f26c877743a340718e0647ccee4604f9d87aa8ad5c3268c794d94f6f9246ee", url="https://pypi.org/packages/e0/fd/23c66b686280caa062c399cfc8d371e1f57f4625e77f7cd6d16abad5c13d/pyobjc_framework_CallKit-10.2-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.8:", when="@10:")
        depends_on("py-pyobjc-core@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-cocoa@10.2:", when="@10.2:")
    # END DEPENDENCIES

