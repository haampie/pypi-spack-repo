# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkSpeech(PythonPackage):
    # BEGIN VERSIONS
    version("10.2", sha256="4cb3445ff31a3f8d50492d420941723e07967b4fc4fc46c336403d8ca245c086", url="https://pypi.org/packages/a4/b4/95857748e26fe65c52c4e1544335cc9b3af831f0b8bd7c76e501b12c711a/pyobjc-framework-Speech-10.2.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.8:", when="@10:")
        depends_on("py-pyobjc-core@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-cocoa@10.2:", when="@10.2:")
    # END DEPENDENCIES

