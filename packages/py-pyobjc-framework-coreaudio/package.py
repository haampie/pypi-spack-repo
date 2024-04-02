# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkCoreaudio(PythonPackage):
    # BEGIN VERSIONS
    version("10.2", sha256="5e97ae7a65be85aee83aef004b31146c5fbf28325d870362959f7312b303fb67", url="https://pypi.org/packages/df/a8/9a2645bfe7ab310f39a35605911ef1a04a9b8a5224e58244c8edda3e2731/pyobjc-framework-CoreAudio-10.2.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.8:", when="@10:")
        depends_on("py-pyobjc-core@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-cocoa@10.2:", when="@10.2:")
    # END DEPENDENCIES

