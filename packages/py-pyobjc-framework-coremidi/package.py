# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkCoremidi(PythonPackage):
    # BEGIN VERSIONS
    version("10.2", sha256="8168cb1e57e5dbc31648cd68d9afe3306cd2751de03275ef5f7f9b6483f17c07", url="https://pypi.org/packages/1d/cd/ff309706091fcfdc10fe6732ce4830b0fdeccfd3c2a1450ac4cf8b4df175/pyobjc-framework-CoreMIDI-10.2.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.8:", when="@10:")
        depends_on("py-pyobjc-core@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-cocoa@10.2:", when="@10.2:")
    # END DEPENDENCIES

