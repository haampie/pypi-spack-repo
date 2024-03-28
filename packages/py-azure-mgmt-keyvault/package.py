# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyAzureMgmtKeyvault(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("2.2.0", sha256="8b490af44d389b918b4feca41a27eab0e77d724f64db69e3e6e00c8b984e07f2", url="https://pypi.org/packages/f1/af/1ba15e7176bcf6b1531b453e410ae41a983c09f834d8700dfce739451b53/azure_mgmt_keyvault-2.2.0-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-azure-common@1.1:", when="@1.0.0:")
        depends_on("py-msrest@0.5:", when="@1.1:8")
        depends_on("py-msrestazure@0.4.32:", when="@1.1:2")
    # END DEPENDENCIES

