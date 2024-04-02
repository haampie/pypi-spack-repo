# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkMetalperformanceshaders(PythonPackage):
    # BEGIN VERSIONS
    version("10.2", sha256="66e6f671279b1f7edbaed1bea8ab1eb57f617e000c1e871c190b60ad60c1d727", url="https://pypi.org/packages/13/7a/319128121fddaf6dc68f2eed3e146e1ed7dde558186f368bc67631fbc2d6/pyobjc-framework-MetalPerformanceShaders-10.2.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.8:", when="@10:")
        depends_on("py-pyobjc-core@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-metal@10.2:", when="@10.2:")
    # END DEPENDENCIES

