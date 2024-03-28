# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyAsdf(PythonPackage):
    # BEGIN VERSIONS
    version("3.1.0", sha256="89974e774dc32f53cea802068685e538871db6c6c025b8c73975819a495eb292", url="https://pypi.org/packages/bf/cc/7a0a1c7a42ca7d4da05ad6b71bb75af6dee90c6ddf35ae9059d47e48e338/asdf-3.1.0-py3-none-any.whl")
    version("3.0.1", sha256="29f17af820317f159dba388faa9828816d5b098e1ad0c9df8d8efd77b3552e13", url="https://pypi.org/packages/f7/20/1ca57978171a2c122830afa42e1768dfb8f25e30c592c0d1ae56d3283d0c/asdf-3.0.1-py3-none-any.whl")
    version("3.0.0", sha256="6afb2e4b9207d5f8aac00afa28ee22d8a2a5e4433810dc173cbbcb073ec17e5b", url="https://pypi.org/packages/3d/f1/42d1dd3bd54d2deb115b4354dd71519f029d62a13c6e3354d2f659f8c2c7/asdf-3.0.0-py3-none-any.whl")
    version("2.15.2", sha256="dc2ef392b1cd674797da3932919b92767a7dfb5727cbf29b5b8a81ab3114db74", url="https://pypi.org/packages/3e/21/2de569a7b82fc767a0d7959bb3411f8fafc1e2d78a690fa50966eed69449/asdf-2.15.2-py3-none-any.whl")
    version("2.15.1", sha256="7631882a99ddf8fc70daa5a4de74a9a0f0512b58a8691aafd554111b7c08049e", url="https://pypi.org/packages/25/2e/7a1e284184a42a53c9075b56c20e4f6b3c715ac7a0dbd8a00380917dcb78/asdf-2.15.1-py3-none-any.whl")
    version("2.15.0", sha256="11fae326d1f3a39a2c0c4cd42d4fcb789ef46f9ebe00c79564f34b066f05027a", url="https://pypi.org/packages/17/5e/789fd7cc9696cb8962fd3ca8734a51f606f9d5f0847c3d7e9ff32c9a750b/asdf-2.15.0-py3-none-any.whl")
    version("2.14.4", sha256="101dd245e2fbeee9cc13a6c78f59fdf4bc66c8290f742644656c5946c97231dd", url="https://pypi.org/packages/99/8b/79f48bc1bbcda1b4c13433989f661db096ee5b2a7f662317035772255a7e/asdf-2.14.4-py3-none-any.whl")
    version("2.14.3", sha256="80203adee64611eb0bbb098af9df7120c23d5060a9eb215f0881a8c6c0dde8bd", url="https://pypi.org/packages/bf/6e/918cec55e4670f438b689c92c59aebe01a6c7d381db4bbe9cd26900cb3ce/asdf-2.14.3-py3-none-any.whl")
    version("2.14.2", sha256="c42ffd1d8fd194e475e6336a4c30d8888a10eb04939294440031d9a634c17767", url="https://pypi.org/packages/db/c9/483d6e8f42179e225c987b3839967e6b1e0bc2c25a5b4377177784b20d00/asdf-2.14.2-py3-none-any.whl")
    version("2.14.1", sha256="b265b17bc476b074e1349c0b828d26001adcd82830c6165de6d877beb53a4c55", url="https://pypi.org/packages/22/78/24472763b2bca50008220e0c215ff3e9c4d01c36869c0ea048c8f01e7a91/asdf-2.14.1-py3-none-any.whl")
    version("2.4.2", sha256="6ff3557190c6a33781dae3fd635a8edf0fa0c24c6aca27d8679af36408ea8ff2", url="https://pypi.org/packages/04/16/3c5a9b98b0519ae22d69e521334d9d56176255637f7c60e68fabbce82bc5/asdf-2.4.2.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    variant("lz4", default=False)
    # END VARIANTS

    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.9:", when="@2.15.1:")
        depends_on("py-asdf-standard@1.0.1:", when="@2.10.1:")
        depends_on("py-asdf-transform-schemas@0.3:", when="@2.14.3:")
        depends_on("py-asdf-transform-schemas@0.2.2:", when="@2.10.1:2.14.2")
        depends_on("py-asdf-unit-schemas@0.1:", when="@2.14:")
        depends_on("py-attrs@20:", when="@2.15.1:")
        depends_on("py-importlib-metadata@4.11.4:", when="@2.14.3:")
        depends_on("py-importlib-metadata@3:", when="@2.14:2.14.2 ^python@:3.9")
        depends_on("py-importlib-resources@3:", when="@2.10.1:2.15.0 ^python@:3.8")
        depends_on("py-jmespath@0.6.2:", when="@2.10.1:")
        depends_on("py-jsonschema@4.8:", when="@2.15.1:2")
        depends_on("py-jsonschema@4.0.1:4.17", when="@2.14.4:2.15.0")
        depends_on("py-jsonschema@4.0.1:", when="@2.11:2.11.1,2.12:2.12.0,2.14:2.14.3")
        depends_on("py-numpy@1.22.0:", when="@2.15.1:")
        depends_on("py-numpy@1.20.0:1.24", when="@2.15:2.15.0 ^python@:3.8")
        depends_on("py-numpy@1.20.0:", when="@2.15:2.15.0")
        depends_on("py-numpy@1.18.0:", when="@2.14")
        depends_on("py-packaging@19:", when="@2.15:")
        depends_on("py-packaging@16:", when="@2.10.1:2.14")
        depends_on("py-pyyaml@5.4.1:", when="@2.15:")
        depends_on("py-pyyaml", when="@2.10.1:2.14")
        depends_on("py-semantic-version@2.8:", when="@2.10.1:")
    # END DEPENDENCIES

