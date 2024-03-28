# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyLfpykit(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.5", sha256="3f87f12466ec905890ea854eb1444d9709a72218aefe683cb762f10c9df51ea2", url="https://pypi.org/packages/79/c2/3d26ea734e2195e6320fec4a6e50ffa2c3ac3e14b923376ead8c4f62257f/LFPykit-0.5-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-meautility", when="@0.2-rc2:")
        depends_on("py-numpy@1.15.2:", when="@0.2-rc2:")
        depends_on("py-scipy", when="@0.2-rc2:")
    # END DEPENDENCIES

