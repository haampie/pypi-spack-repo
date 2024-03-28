# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyCmaes(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.10.0", sha256="72cea747ad37b1780b0eb6f3c098cee33907fafbf6690c0c02db1e010cab72f6", url="https://pypi.org/packages/f7/46/7d9544d453346f6c0c405916c95fdb653491ea2e9976cabb810ba2fe8cd4/cmaes-0.10.0-py3-none-any.whl")
    version("0.9.1", sha256="6e2930b6a99dd94621bf62966c13d29e6a7f90a909b4e4266010d5f3a7fb74b8", url="https://pypi.org/packages/11/a9/83c304855d801dda85c05e6fad0483161ebfba1500efde3de9652b50ac14/cmaes-0.9.1-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-numpy", when="@:0.7.0,0.8.1:")
    # END DEPENDENCIES

