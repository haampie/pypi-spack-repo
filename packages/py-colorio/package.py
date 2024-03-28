# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyColorio(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.11.2", sha256="75b972de1c08164adbb7d344b8c4eee0e589b30d7e7b223395c923fa2ab5c02d", url="https://pypi.org/packages/d0/08/d03f65aa6344f46a42cc2d3aad2807a565aec8525ea419ff4834c63f8de3/colorio-0.11.2-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-matplotlib")
        depends_on("py-npx", when="@0.7.4:")
        depends_on("py-numpy@1.20.0:", when="@0.8:")
        depends_on("py-scipy", when="@0.2.3:0.5.5")
    # END DEPENDENCIES

