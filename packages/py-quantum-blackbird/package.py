# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyQuantumBlackbird(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.5.0", sha256="2f7898e08b87689b92bd972b97b9b172f65118c6d80180167a35fb2e3bf02fc6", url="https://pypi.org/packages/85/08/283084c863a9fed00df1215ef5219192956e8070491fea40efd6ca6bc0ea/quantum_blackbird-0.5.0-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-antlr4-python3-runtime@4.9.2", when="@0.5:")
        depends_on("py-networkx", when="@0.2:")
        depends_on("py-numpy@1.16.0:", when="@:0.2.1,0.2.3:")
        depends_on("py-sympy")
    # END DEPENDENCIES

