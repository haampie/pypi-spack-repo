# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkCoremedia(PythonPackage):
    # BEGIN VERSIONS
    version("10.2", sha256="d726d86636217eaa135e5626d05c7eb0f9b4529ce1ed504e08069fe1e0421483", url="https://pypi.org/packages/79/45/343e8f778f6fdd52b85850975b1cb60f0d2f1cc1c3bdfbcb398104756fd7/pyobjc-framework-CoreMedia-10.2.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.8:", when="@10:")
        depends_on("py-pyobjc-core@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-cocoa@10.2:", when="@10.2:")
    # END DEPENDENCIES

