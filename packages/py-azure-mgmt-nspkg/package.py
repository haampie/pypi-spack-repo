# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyAzureMgmtNspkg(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("3.0.2", sha256="d638ea5fda3ed323db943feb29acaa200f5d8ff092078bf8d29d4a2f8ed16999", url="https://pypi.org/packages/b3/c2/af4b47845f27dc7d206ed4908b9e580f8bc94a4b2f3956a0d87c40719d90/azure_mgmt_nspkg-3.0.2-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-azure-nspkg@3:", when="@3:")
    # END DEPENDENCIES

