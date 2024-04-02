# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkWebkit(PythonPackage):
    # BEGIN VERSIONS
    version("10.2", sha256="3717104dbc901a1bd46d97886c5adb6eb32798ff4451c4544e04740e41706083", url="https://pypi.org/packages/6f/76/1c7376b7f4a90095904b8f91a6db1aadde99066ffca999e6ffc1dd83830d/pyobjc-framework-WebKit-10.2.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.8:", when="@10:")
        depends_on("py-pyobjc-core@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-cocoa@10.2:", when="@10.2:")
    # END DEPENDENCIES

