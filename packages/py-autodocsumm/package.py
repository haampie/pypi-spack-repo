# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyAutodocsumm(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.2.11", sha256="f1d0a623bf1ad64d979a9e23fd360d1fb1b8f869beaf3197f711552cddc174e2", url="https://pypi.org/packages/c6/37/0a08e3e1d8b78185837c0c483267b87660ae74cdee0c91dc56ae83093965/autodocsumm-0.2.11-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-sphinx@2.2:", when="@0.2.11:")
    # END DEPENDENCIES

