# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyAzureMgmtMedia(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("2.2.0", sha256="4cf414376abaf7444359dd8d1a06f4e1156b7d151e7cea42420a0843b7afbe50", url="https://pypi.org/packages/66/a1/4468df95486910343391539887881702ba90d98d005c0362edcb6f7aed89/azure_mgmt_media-2.2.0-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-azure-common@1.1:", when="@1:")
        depends_on("py-msrest@0.5:", when="@1.0.0:7.0.0-beta1")
        depends_on("py-msrestazure@0.4.32:", when="@1.0.0-rc2:4")
    # END DEPENDENCIES

