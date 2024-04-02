# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyZfitInterface(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.0.3", sha256="c41cf79f1da4150b9a60bb1e8cab15df895b6ff4b753e2306494a7abda4150d0", url="https://pypi.org/packages/61/ce/07d8fa63a501dc3af9639595e486be0a18de00726b54a7dc88a5ada235d8/zfit_interface-0.0.3-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.7:", when="@0.0.3:")
        depends_on("py-numpy", when="@0.0.3:")
        depends_on("py-typing-extensions", when="@0.0.3:")
        depends_on("py-uhi", when="@0.0.3:")
    # END DEPENDENCIES

