# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyAzureMgmtDatalakeNspkg(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("3.0.1", sha256="3b9e2843f5d0fd6015bba13040dfc2f5fe9bc7b02c9d91dd578e8fe852d1b2dd", url="https://pypi.org/packages/76/e2/4271ab409ff3bac77ae2843c30590868db42715a75658f8a9da229b7ac98/azure_mgmt_datalake_nspkg-3.0.1-py2-none-any.whl")
    version("2.0.0", sha256="67abb25403fadaa697a790327b5730b2b88c3779b9b4972427253ee3a04d3e1e", url="https://pypi.org/packages/45/44/ac10e1d1757a46299515568ec7ba62af84f012335cbba957aab32ee08f3d/azure_mgmt_datalake_nspkg-2.0.0-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-azure-mgmt-nspkg@3:", when="@3:")
        depends_on("py-azure-mgmt-nspkg@2:", when="@2")
    # END DEPENDENCIES

