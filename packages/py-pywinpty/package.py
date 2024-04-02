# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPywinpty(PythonPackage):
    # BEGIN VERSIONS
    version("2.0.13", sha256="c34e32351a3313ddd0d7da23d27f835c860d32fe4ac814d372a3ea9594f41dde", url="https://pypi.org/packages/33/d9/93956af389ab7d4ef2f558b1cc6c5cb48885d254ac882f212964c30a1e4f/pywinpty-2.0.13.tar.gz")
    version("1.1.6", sha256="8808f07350c709119cc4464144d6e749637f98e15acc1e5d3c37db1953d2eebc", url="https://pypi.org/packages/3d/1d/b884c586cb4ff53da97f9c9e177dd73e74a5d848e2954492341f118413fc/pywinpty-1.1.6.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.8:", when="@2.0.11:")
    # END DEPENDENCIES

