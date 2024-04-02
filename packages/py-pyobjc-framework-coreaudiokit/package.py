# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkCoreaudiokit(PythonPackage):
    # BEGIN VERSIONS
    version("10.2", sha256="38dfafba8eddb655aac352a967c0e713a90e10a4dd40d4ea1abbb4db01c5d33f", url="https://pypi.org/packages/ef/6d/c6fe61ee094ad062eaa04ae12cd5ced4fbdb34b233f12b71eccaaaea7c10/pyobjc-framework-CoreAudioKit-10.2.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.8:", when="@10:")
        depends_on("py-pyobjc-core@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-cocoa@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-coreaudio@10.2:", when="@10.2:")
    # END DEPENDENCIES

