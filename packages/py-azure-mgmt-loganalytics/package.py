# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyAzureMgmtLoganalytics(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.7.0", sha256="e14255483350b67226ed0aecceb89a18c5df6162518da43a1f07a40abdce2098", url="https://pypi.org/packages/73/0f/23b85bcfaf8ad267a7c552293491c03bac382f9a4e99320d2223ddc62b47/azure_mgmt_loganalytics-0.7.0-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-azure-common@1.1:")
        depends_on("py-msrest@0.5:", when="@0.3:8")
        depends_on("py-msrestazure@0.4.32:", when="@0.3:2")
    # END DEPENDENCIES

