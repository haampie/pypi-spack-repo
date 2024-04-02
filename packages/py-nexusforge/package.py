# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyNexusforge(PythonPackage):
    # BEGIN VERSIONS
    version("0.8.1", sha256="eb2909cbec185e7a73191c1be1e62902a0d8534f0d93454ef3e4e3b18b5129cf", url="https://pypi.org/packages/01/d4/0b7fecbabd0559984a358f1a4c97d3c386f7a2a2b92d8fca9e9220fd4936/nexusforge-0.8.1.tar.gz")
    version("0.8.0", sha256="4358505ead26e41c2a0c4e6113cf3a486c9661e2a3899394497a2b5a94b70424", url="https://pypi.org/packages/33/d9/8301db68f4417b8ea618861a6dd19d3abebb0581b816190886a27ea6c1f7/nexusforge-0.8.0.tar.gz")
    version("0.7.0", sha256="a8d2951d9ad18df9f2f4db31a4c18fcdd27bfcec929b03a3c91f133ea439413c", url="https://pypi.org/packages/57/3f/6760acbd770a35c87389bc56404708d8ab09692df810220d01bdad779089/nexusforge-0.7.0.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    variant("sklearn", default=False, description="sklearn")
    # END VARIANTS

    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.8:", when="@0.8.1:")
        depends_on("python@3.7:", when="@0.7:0.8.0")
    # END DEPENDENCIES

