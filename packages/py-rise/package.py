# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyRise(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("5.6.1", sha256="e9637ee5499ad7801474da53a2c830350a44b2192c2f113594e4426190e55ad4", url="https://pypi.org/packages/5c/f4/c226756f3e238a6109aba848ae7e1c96e5b3ed13bbd2916c5f0c6c207fe4/rise-5.6.1-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-notebook@5.5.0:", when="@5.3:5.6")
    # END DEPENDENCIES

