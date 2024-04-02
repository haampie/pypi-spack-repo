# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyAsdf(PythonPackage):
    # BEGIN VERSIONS
    version("2.15.0", sha256="11fae326d1f3a39a2c0c4cd42d4fcb789ef46f9ebe00c79564f34b066f05027a", url="https://pypi.org/packages/17/5e/789fd7cc9696cb8962fd3ca8734a51f606f9d5f0847c3d7e9ff32c9a750b/asdf-2.15.0-py3-none-any.whl")
    version("2.4.2", sha256="6ff3557190c6a33781dae3fd635a8edf0fa0c24c6aca27d8679af36408ea8ff2", url="https://pypi.org/packages/04/16/3c5a9b98b0519ae22d69e521334d9d56176255637f7c60e68fabbce82bc5/asdf-2.4.2.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    variant("lz4", default=False, description="lz4")
    # END VARIANTS

    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.8:", when="@2.12.1:2.15.0")
        depends_on("py-asdf-standard@1.0.1:", when="@2.10.1:")
        depends_on("py-asdf-transform-schemas@0.3:", when="@2.14.3:")
        depends_on("py-asdf-unit-schemas@0.1:", when="@2.14:")
        depends_on("py-importlib-metadata@4.11.4:", when="@2.14.3:")
        depends_on("py-importlib-resources@3:", when="@2.10.1:2.15.0 ^python@:3.8")
        depends_on("py-jmespath@0.6.2:", when="@2.10.1:")
        depends_on("py-jsonschema@4.0.1:4.17", when="@2.14.4:2.15.0")
        depends_on("py-numpy@1.20.0:1.24", when="@2.15:2.15.0 ^python@:3.8")
        depends_on("py-numpy@1.20.0:", when="@2.15:2.15.0")
        depends_on("py-packaging@19:", when="@2.15:")
        depends_on("py-pyyaml@5.4.1:", when="@2.15:")
        depends_on("py-semantic-version@2.8:", when="@2.10.1:")
    # END DEPENDENCIES

