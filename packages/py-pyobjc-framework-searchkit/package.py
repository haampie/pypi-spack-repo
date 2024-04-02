# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkSearchkit(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("10.2", sha256="ddd9e2f207ae578f04ec2358fdf485f26978d6de4909640b58486a8a9e4e639c", url="https://pypi.org/packages/15/5a/d411aeadd0177beb5b3bd0afa8a4882342db31730332e2eb5b19749101e0/pyobjc_framework_SearchKit-10.2-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.8:", when="@10:")
        depends_on("py-pyobjc-core@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-coreservices@10.2:", when="@10.2:")
    # END DEPENDENCIES

