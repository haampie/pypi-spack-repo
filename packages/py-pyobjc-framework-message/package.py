# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkMessage(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("8.5.1", sha256="bf4fd13bbe28ddfcbba544251e07edab9ec2e9ed34000a205a7baec403ee20a8", url="https://pypi.org/packages/3f/db/b4154660a5350509e451a1e6f9cc76f8fcbf97bfe25a7febd116988c3ffc/pyobjc_framework_Message-8.5.1-py2.py3-none-any.whl")
    version("8.5", sha256="ae36377f6ce9b0190601e5eebd758bf34c4b5d7c40f24ec82cecbde246671724", url="https://pypi.org/packages/57/14/54fcab4e3d1ae98d364d8baa57132634ee24f0068f0040a7d062d95f758f/pyobjc_framework_Message-8.5-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-pyobjc-core@8.5.1:", when="@8.5.1:")
        depends_on("py-pyobjc-core@8.5:", when="@8.5:8.5.0")
        depends_on("py-pyobjc-framework-cocoa@8.5.1:", when="@8.5.1:")
        depends_on("py-pyobjc-framework-cocoa@8.5:", when="@8.5:8.5.0")
    # END DEPENDENCIES

