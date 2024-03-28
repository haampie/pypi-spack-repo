# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyAzureMgmtImagebuilder(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.4.0", sha256="e9240c332f2dabb8fdabce8a8b21ed37392ac97389d151bcf79e4e9ea1ca2d09", url="https://pypi.org/packages/d1/42/7c50901d834bdeee7fa8ea03993ce3294c4f41640e066468cc0d6e255483/azure_mgmt_imagebuilder-0.4.0-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-azure-common@1.1:")
        depends_on("py-msrest@0.5:", when="@:0")
        depends_on("py-msrestazure@0.4.32:", when="@:0")
    # END DEPENDENCIES

