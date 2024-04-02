# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkLaunchservices(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("10.2", sha256="15b7c96e3059550c218ed5cb5de11dddc7aae21c67c0808b130a5d49b8f4cc0f", url="https://pypi.org/packages/a3/e8/9323d5032ada2465e2dbdd06ea40db8ac5a52bdb1c8735caaec0810c6b3d/pyobjc_framework_LaunchServices-10.2-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.8:", when="@10:")
        depends_on("py-pyobjc-core@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-coreservices@10.2:", when="@10.2:")
    # END DEPENDENCIES

