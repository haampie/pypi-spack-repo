# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkContacts(PythonPackage):
    # BEGIN VERSIONS
    version("10.2", sha256="5a9de975f41c7dac3c219b4c60cd08b8ba385685db7997c8622f19e0a43e6857", url="https://pypi.org/packages/1c/20/7428cf84dbae9cf8ae6d44cb88cb7711ba94ed0a98123d8e1f2a30d3d857/pyobjc-framework-Contacts-10.2.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.8:", when="@10:")
        depends_on("py-pyobjc-core@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-cocoa@10.2:", when="@10.2:")
    # END DEPENDENCIES

