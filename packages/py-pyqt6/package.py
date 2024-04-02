# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyqt6(PythonPackage):
    # BEGIN VERSIONS
    version("6.6.1", sha256="9f158aa29d205142c56f0f35d07784b8df0be28378d20a97bcda8bd64ffd0379", url="https://pypi.org/packages/8c/2b/6fe0409501798abc780a70cab48c39599742ab5a8168e682107eaab78fca/PyQt6-6.6.1.tar.gz")
    version("6.6.0", sha256="d41512d66044c2df9c5f515a56a922170d68a37b3406ffddc8b4adc57181b576", url="https://pypi.org/packages/17/dc/969e2da415597b328e6a73dc233f9bb4f2b312889180e9bbe48470c957e7/PyQt6-6.6.0.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-pyqt6-sip@13.6:", when="@6.5.3:")
    # END DEPENDENCIES

