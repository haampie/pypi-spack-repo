# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyAdal(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("1.2.4", sha256="b332316f54d947f39acd9628e7d61d90f6e54d413d6f97025a51482c96bac6bc", url="https://pypi.org/packages/46/58/a19e0eb0c388fb7aced40f940c09069343862613d83095b592a8d3961ba1/adal-1.2.4-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-cryptography@1.1:", when="@0.4.3:0.4.5,0.4.7:")
        depends_on("py-pyjwt@1:", when="@0.4.3:0.4.5,0.4.7:1.2.5")
        depends_on("py-python-dateutil@2:", when="@0.4.3:0.4.5,0.4.7:1.2.5")
        depends_on("py-requests@2:", when="@0.4.4:0.4.5,0.4.7:1.2.5")
    # END DEPENDENCIES

