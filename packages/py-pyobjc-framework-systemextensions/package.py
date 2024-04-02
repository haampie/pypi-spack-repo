# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkSystemextensions(PythonPackage):
    # BEGIN VERSIONS
    version("10.2", sha256="883c41cb257fb2b5baadafa4213dc0f0fffc97edb35ebaf6ed95a185a786eb85", url="https://pypi.org/packages/5b/a8/0f785b4667671a918967f660e2a42961b00f78ad494629481816b89133fa/pyobjc-framework-SystemExtensions-10.2.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.8:", when="@10:")
        depends_on("py-pyobjc-core@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-cocoa@10.2:", when="@10.2:")
    # END DEPENDENCIES

