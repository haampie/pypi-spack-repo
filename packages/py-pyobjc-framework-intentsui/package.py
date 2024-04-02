# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkIntentsui(PythonPackage):
    # BEGIN VERSIONS
    version("10.2", sha256="4b9ca6f868b6cb7945ef4c285e73d220433efc35dfcad6b4a356bfce55e96c09", url="https://pypi.org/packages/af/ae/5f671f2906d4fcfaf9955bad758e7b29278fb3c5f91a65fd78548c5ece74/pyobjc-framework-IntentsUI-10.2.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.8:", when="@10:")
        depends_on("py-pyobjc-core@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-intents@10.2:", when="@10.2:")
    # END DEPENDENCIES

