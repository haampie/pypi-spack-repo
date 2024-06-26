# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyAzureMgmtServicefabric(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.4.0", sha256="e86ca293aaa012349aa1ef5340e3bcc6ec398a413ba43642524ddde155b2c1fe", url="https://pypi.org/packages/57/b6/7e53e52f13a63621801630f9b2fbec73b2f3705f6d98e2181b288ba9810d/azure_mgmt_servicefabric-0.4.0-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-azure-common@1.1:")
        depends_on("py-msrest@0.5:", when="@0.2:1.0.0-beta1")
        depends_on("py-msrestazure@0.4.32:", when="@0.2:0")
    # END DEPENDENCIES

