##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyRetrying(PythonPackage):
    version("1.3.4", sha256="8cc4d43cb8e1125e0ff3344e9de678fefd85db3b750b81b2240dc0183af37b35", url="https://pypi.org/packages/8f/04/9e36f28be4c0532c0e9207ff9dc01fb13a2b0eb036476a213b0000837d0e/retrying-1.3.4-py3-none-any.whl")
    version("1.3.3", sha256="08c039560a6da2fe4f2c426d0766e284d3b736e355f8dd24b37367b0bb41973b", url="https://pypi.org/packages/44/ef/beae4b4ef80902f22e3af073397f079c96969c69b2c7d52a57ea9ae61c9d/retrying-1.3.3.tar.gz")

    with default_args(type="run"):
        depends_on("py-six@1.7:", when="@1.3.4:")

