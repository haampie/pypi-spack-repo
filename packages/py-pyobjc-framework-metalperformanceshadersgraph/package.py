# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkMetalperformanceshadersgraph(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("10.2", sha256="7fedd831f9fc58708f6b01888abd42a2f08151c86db47280fe47be0f709811bf", url="https://pypi.org/packages/88/75/3cfed273b3aaf92d5cfde429ab4a188964855b333d93deb466ef3c347b72/pyobjc_framework_MetalPerformanceShadersGraph-10.2-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.8:", when="@10:")
        depends_on("py-pyobjc-core@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-metalperformanceshaders@10.2:", when="@10.2:")
    # END DEPENDENCIES

