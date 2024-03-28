# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PySnakemakeInterfaceStoragePlugins(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("3.1.1", sha256="fce880593273073b0707438792252bac8ad454ebef3a22f9ea7b52368670b1be", url="https://pypi.org/packages/99/41/0b112829ffb0af3d9c2808c314722cb87b64329b3e40deb744e08ba99228/snakemake_interface_storage_plugins-3.1.1-py3-none-any.whl")
    version("3.1.0", sha256="bbe1e9f0cd9c8befa4223bad0388b54f61892bf105e38722604c8ce4f161ecc3", url="https://pypi.org/packages/5d/17/d7001eef38781a74384e97593b05493b5250de38924847436a18a52226e1/snakemake_interface_storage_plugins-3.1.0-py3-none-any.whl")
    version("3.0.0", sha256="a2bff701cc23930143d2699520080234f8cc8ce59774be938d46fb86b82e848c", url="https://pypi.org/packages/50/e0/79ab611fc2a75c7ad732cf3ed20c1503a5736ff4d0df39aeef6aa193e6d3/snakemake_interface_storage_plugins-3.0.0-py3-none-any.whl")
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

