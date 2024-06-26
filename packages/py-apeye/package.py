# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyApeye(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("1.4.1", sha256="44e58a9104ec189bf42e76b3a7fe91e2b2879d96d48e9a77e5e32ff699c9204e", url="https://pypi.org/packages/89/7b/2d63664777b3e831ac1b1d8df5bbf0b7c8bee48e57115896080890527b1b/apeye-1.4.1-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-apeye-core@1.0.0-beta2:", when="@1.3:")
        depends_on("py-domdf-python-tools@2.6:", when="@1.2:")
        depends_on("py-platformdirs@2.3:", when="@1.2:")
        depends_on("py-requests@2.24:")
    # END DEPENDENCIES

