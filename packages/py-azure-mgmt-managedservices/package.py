# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyAzureMgmtManagedservices(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("1.0.0", sha256="cc05519a528ad6c1fe87c18da34c6fac62f0a097ee6e73630826fdc598bce869", url="https://pypi.org/packages/2e/6d/9e22f03eef41ac4c9f8a6cbe002d65e12f693cc7b93eff1b907918ed8f60/azure_mgmt_managedservices-1.0.0-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-azure-common@1.1:")
        depends_on("py-msrest@0.5:", when="@:6.0.0-beta1")
        depends_on("py-msrestazure@0.4.32:", when="@:1")
    # END DEPENDENCIES

