# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PySnakemakeInterfaceStoragePlugins(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("3.1.0", sha256="bbe1e9f0cd9c8befa4223bad0388b54f61892bf105e38722604c8ce4f161ecc3", url="https://pypi.org/packages/5d/17/d7001eef38781a74384e97593b05493b5250de38924847436a18a52226e1/snakemake_interface_storage_plugins-3.1.0-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.11:", when="@1.2:")
        depends_on("python@3.9:", when="@:1.1")
        depends_on("py-reretry@0.11.8:")
        depends_on("py-snakemake-interface-common@1.12:", when="@1.2:")
        depends_on("py-throttler@1.2.2:", when="@1.1:")
        depends_on("py-wrapt@1.15.0:")
    # END DEPENDENCIES

