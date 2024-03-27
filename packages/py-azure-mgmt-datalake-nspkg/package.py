##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyAzureMgmtDatalakeNspkg(PythonPackage):
    version("3.0.1", sha256="deb192ba422f8b3ec272ce4e88736796f216f28ea5b03f28331d784b7a3f4880", url="https://pypi.org/packages/8e/0c/7b705f7c4a41bfeb0b6f3557f227c71aa3fa71555ed76ae934aa7db4b13e/azure-mgmt-datalake-nspkg-3.0.1.zip")
    version("2.0.0", sha256="67abb25403fadaa697a790327b5730b2b88c3779b9b4972427253ee3a04d3e1e", url="https://pypi.org/packages/45/44/ac10e1d1757a46299515568ec7ba62af84f012335cbba957aab32ee08f3d/azure_mgmt_datalake_nspkg-2.0.0-py2.py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-azure-mgmt-nspkg@3:", when="@3:")
        depends_on("py-azure-mgmt-nspkg@2:", when="@2")

