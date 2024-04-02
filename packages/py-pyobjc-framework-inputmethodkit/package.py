# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkInputmethodkit(PythonPackage):
    # BEGIN VERSIONS
    version("10.2", sha256="294cf2c50cdbb4cdc8f06946924a01faf45a7356ef86652d73c1f310fc1ce99f", url="https://pypi.org/packages/9d/3c/377c35aab6ae237d95b345f533191c43fdb4c7a4d9daca364bbeb23d4072/pyobjc-framework-InputMethodKit-10.2.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.8:", when="@10:")
        depends_on("py-pyobjc-core@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-cocoa@10.2:", when="@10.2:")
    # END DEPENDENCIES

