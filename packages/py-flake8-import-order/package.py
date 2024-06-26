# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyFlake8ImportOrder(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.18.1", sha256="90a80e46886259b9c396b578d75c749801a41ee969a235e163cfe1be7afd2543", url="https://pypi.org/packages/ab/52/cf2d6e2c505644ca06de2f6f3546f1e4f2b7be34246c9e0757c6048868f9/flake8_import_order-0.18.1-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-pycodestyle")
        depends_on("py-setuptools")
    # END DEPENDENCIES

