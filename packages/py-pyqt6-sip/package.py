# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyqt6Sip(PythonPackage):
    # BEGIN VERSIONS
    version("13.6.0", sha256="2486e1588071943d4f6657ba09096dc9fffd2322ad2c30041e78ea3f037b5778", url="https://pypi.org/packages/98/23/e54e02a44afc357ccab1b88575b90729664164358ceffde43e4f2e549daa/PyQt6_sip-13.6.0.tar.gz")
    version("13.5.1", sha256="d1e9141752966669576d04b37ba0b122abbc41cc9c35493751028d7d91c4dd49", url="https://pypi.org/packages/2b/b4/87241bb21832cda1061805492ca2a5fd9d18969ea72277bb9fde94228962/PyQt6_sip-13.5.1.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.7:", when="@13.3.1:")
    # END DEPENDENCIES

