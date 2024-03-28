# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyModin(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.16.2", sha256="6c00c42887d7aac72dcaa1dad4f34f66f22364b4d9df88fde260bf3551d1bb82", url="https://pypi.org/packages/d4/d1/0f7de03512702c42133a54a4c0a04a8aa0e2eecd318959c45eb798f8a8f1/modin-0.16.2-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    variant("engine", default=False)
    # END VARIANTS

    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.9:", when="@0.24:")
        depends_on("py-fsspec", when="@0.12:0.23.0")
        depends_on("py-numpy@1.18.5:", when="@0.13:0.23.0")
        depends_on("py-packaging", when="@0.7.1:0.7,0.12:0.23.0")
        depends_on("py-pandas@1.5.1", when="@0.16.2:0.17.0")
        depends_on("py-psutil", when="@0.15.2:0.23.0")
    # END DEPENDENCIES

