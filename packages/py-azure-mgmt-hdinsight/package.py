# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyAzureMgmtHdinsight(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("1.5.1", sha256="53134d367ff7e9529ddc9f9cf00cdbece8be55103a24d37607ed8f53391cec9f", url="https://pypi.org/packages/ae/c2/fb2076606f1f72ea299b023d5e0dd18672ca99a51767439cc9272b3d9c2f/azure_mgmt_hdinsight-1.5.1-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-azure-common@1.1:")
        depends_on("py-msrest@0.5:", when="@:7")
        depends_on("py-msrestazure@0.4.32:", when="@:3")
    # END DEPENDENCIES

