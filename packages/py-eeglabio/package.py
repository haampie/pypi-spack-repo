# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyEeglabio(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.0.2.post4", sha256="76ce4da4a33fc6ec53830756dab04cdda9f7b4e01ee91b0d7d4055d3382d17ae", url="https://pypi.org/packages/71/1e/4d4df763057a0e003255603dc2634ce9e0ef352fbaa16b101b2492763212/eeglabio-0.0.2.post4-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.7:", when="@0.0.1.post7:")
        depends_on("py-numpy")
        depends_on("py-scipy")
    # END DEPENDENCIES

