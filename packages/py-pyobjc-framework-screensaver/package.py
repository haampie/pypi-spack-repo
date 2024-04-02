# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkScreensaver(PythonPackage):
    # BEGIN VERSIONS
    version("10.2", sha256="00c6a312467abb516fd2f19e3166c4609eed939edc0f2c888ccd8c9f0fdd30f1", url="https://pypi.org/packages/21/95/ceab6db3dd4ffd801f927e071be8cc62215de566ed45f59707b80e096aab/pyobjc-framework-ScreenSaver-10.2.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.8:", when="@10:")
        depends_on("py-pyobjc-core@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-cocoa@10.2:", when="@10.2:")
    # END DEPENDENCIES

