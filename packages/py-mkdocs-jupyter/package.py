# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyMkdocsJupyter(PythonPackage):
    # BEGIN VERSIONS
    version("0.21.0", sha256="c8c00ce44456e3cf50c5dc3fe0cb18fab6467fb5bafc2c0bfe1efff3e0a52470", url="https://pypi.org/packages/fc/36/6fd82a714f84f165509382bc43957e440ed4abaf640e67985f9e2e11a6a6/mkdocs-jupyter-0.21.0.tar.gz")
    version("0.20.1", sha256="3b6ef675ee2f22ad94047db7f84e212f5278529df659f7584b5a2b8662db39f6", url="https://pypi.org/packages/94/71/c1b3c3a9735669221ea6ffaeda8866fef4f83b49bb0122869135498b5d87/mkdocs-jupyter-0.20.1.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.9:", when="@0.24.4:")
        depends_on("py-jupytext@1.13.8:", when="@0.21:0.22")
        depends_on("py-jupytext@1.11.2:", when="@0.18.1:0.20")
        depends_on("py-mkdocs@1.2.3:", when="@0.19:0.22")
        depends_on("py-mkdocs-material@8.0.0:8", when="@0.19:0.22")
        depends_on("py-nbconvert@6.2.0:6", when="@0.18.1:0.22")
        depends_on("py-pygments@2.12:", when="@0.21:0.22")
    # END DEPENDENCIES

