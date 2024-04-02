# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkPushkit(PythonPackage):
    # BEGIN VERSIONS
    version("10.2", sha256="e30fc4926a9fcd3427701e48a8908f72e546720e52b1e0f457ba2fa017974917", url="https://pypi.org/packages/77/80/1e592435111b7f3c01d17f62f5d8694c639035bceca09dbbf8fb71075f7f/pyobjc-framework-PushKit-10.2.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.8:", when="@10:")
        depends_on("py-pyobjc-core@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-cocoa@10.2:", when="@10.2:")
    # END DEPENDENCIES

