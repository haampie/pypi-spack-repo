# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkClasskit(PythonPackage):
    # BEGIN VERSIONS
    version("10.2", sha256="252e47e3284491e48000d4d87948b31e396aaa78eaf2447ba03a71f4b97cb989", url="https://pypi.org/packages/03/ee/302ed4f416ded628920458b873a2eb2ac9af3900da5bee5cb80b44e37b06/pyobjc-framework-ClassKit-10.2.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.8:", when="@10:")
        depends_on("py-pyobjc-core@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-cocoa@10.2:", when="@10.2:")
    # END DEPENDENCIES

