# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyNdindex(PythonPackage):
    # BEGIN VERSIONS
    version("1.8", sha256="b5132cd331f3e4106913ed1a974a3e355967a5991543c2f512b40cb8bb9f50b8", url="https://pypi.org/packages/4c/1f/cbec4cb91b5aa7e44a539a92ec76293ababe9a6dd123c52a0e416d50dc81/ndindex-1.8-py3-none-any.whl")
    version("1.7", sha256="4c0555d352ac9947b0f022562aea9f5d57fa06743ea069669138f75a88b42884", url="https://pypi.org/packages/7e/6e/bc00eed30c09815d815fce51f4f921c603b188ad6c3c9887662eabea4c64/ndindex-1.7-py3-none-any.whl")
    version("1.6", sha256="5c1158b6dcaf4e2b79c329d27985361bfeadaa4b3dc9e929a370abefddf9d4f0", url="https://pypi.org/packages/a3/98/7ca8e9d837aba1b2c68ead618b6568c1dadc3616d3a841a45db41b755c6f/ndindex-1.6-py3-none-any.whl")
    version("1.5.2", sha256="e35fe1babe2d11c0b7af55b93b64f9c2725ea19a5d81c973fb8a2db5fbf3902e", url="https://pypi.org/packages/90/f3/d0d965f1fb4ab2df0715764ed6eeda82c68115b93a73e156e46bb659c23f/ndindex-1.5.2.tar.gz")
    version("1.5.1", sha256="3035a560da304be6a2862f66c554e0ec0a447fc411c72d6006bf71ccf2dc80a6", url="https://pypi.org/packages/04/0d/390f09e4837cefaa9a0eba74eb30766ace467ef811a3f09f3960061132e4/ndindex-1.5.1-py3-none-any.whl")
    version("1.5", sha256="0c7094b4f398f0aace1a22b1ad0030db14379689da359bc53650165035a45a1b", url="https://pypi.org/packages/3c/e9/ea3d74043ab00f3b4998960ebb9b89b28aa9b07e11a6af71d788e59b211d/ndindex-1.5.tar.gz")
    version("1.4", sha256="02e39f55529140cf89bbeb1b644cc65364ae4bce168f480b1b87ccf5cca790ca", url="https://pypi.org/packages/5f/e9/e56aa1a03b96d736ece367d54ced1d90881f9856954c0bcd9443f8bb0aec/ndindex-1.4.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-numpy", when="@1.5.1")
        depends_on("py-sympy", when="@1.5.1")
    # END DEPENDENCIES

