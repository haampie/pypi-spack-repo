# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyJax(PythonPackage):
    # BEGIN VERSIONS
    version("0.4.25", sha256="8158c837e5ecc195074b421609e85329a962785b36f9fe5ff53e844e8ad87dbc", url="https://pypi.org/packages/ad/29/37cc2d58775917e6da532ef59cd3a66133d4de73fce1c16852e8475e5411/jax-0.4.25-py3-none-any.whl")
    version("0.4.23", sha256="a7a07ccd1577111e3b82378c79a8ed0f9d6613b1e98fb6bf3c0b459198f73eaa", url="https://pypi.org/packages/28/d0/edf653ea02628f2130ea2557f96d02b264768a2f54d22a9c002c7119cb1d/jax-0.4.23-py3-none-any.whl")
    version("0.4.16", sha256="c37d8eee6dec3763d9428fdf318a9351369f19ceaa174b11696b3d7960a43d5b", url="https://pypi.org/packages/2f/7e/052564673066fcb143a7d096232790d037554b323f0cf0e7c2af3a60ca88/jax-0.4.16-py3-none-any.whl")
    version("0.4.3", sha256="d43f08f940aa30eb339965cfb3d6bee2296537b0dc2f0c65ccae3009279529ae", url="https://pypi.org/packages/96/f2/cfbefdd74bb04e02c8a0599332c22db9adbdf2b13775de3ce9b0445bdf18/jax-0.4.3.tar.gz")
    version("0.3.23", sha256="bff436e15552a82c0ebdef32737043b799e1e10124423c57a6ae6118c3a7b6cd", url="https://pypi.org/packages/43/ce/7ce437f917b8bd0e55db25e08e1c4bec8692a1f9236472e93d16aef86e77/jax-0.3.23.tar.gz")
    version("0.3.5", sha256="bde2adb9c8b3abc10cadeab4199a0a8fe04de4dd39fac160140f4375fe24ce30", url="https://pypi.org/packages/33/fe/1120b6c91e38d47cfd9533e2a525ba15df494687c4a9c09ec71890046c67/jax-0.3.5.tar.gz")
    version("0.2.25", sha256="822e8d1e06257eaa0fdc4c0a0686c4556e9f33647fa2a766755f984786ae7446", url="https://pypi.org/packages/bf/7a/b395056c9ec4a67b95107c4ad8853f9697e3451916d69501d97843156947/jax-0.2.25.tar.gz")
    version("0.2.22", sha256="ec0963e0b08599628f4c9a04b18b2bb9e99939cb2eb0589039daa5925f575e5c", url="https://pypi.org/packages/2d/59/42b41f3950ea1bf31308323fc1de65551cb406e3b7cdc900a2add80414b3/jax-0.2.22.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.9:", when="@0.4.14:")
        depends_on("python@3.8:", when="@0.4:0.4.13")
        depends_on("python@3.7:", when="@0.2.18:0.3")
        depends_on("py-importlib-metadata@4.6:", when="@0.4.16: ^python@:3.9")
        depends_on("py-ml-dtypes@0.2:", when="@0.4.16:")
        depends_on("py-numpy@1.26.0:", when="@0.4.18: ^python@3.12:")
        depends_on("py-numpy@1.23.2:", when="@0.4.18: ^python@3.11:")
        depends_on("py-numpy@1.22.0:", when="@0.4.16:")
        depends_on("py-opt-einsum", when="@0.4.16:")
        depends_on("py-scipy@1.11.1:", when="@0.4.19: ^python@3.12:")
        depends_on("py-scipy@1.9.0:", when="@0.4.19:")
        depends_on("py-scipy@1.7.0:", when="@0.4.16:0.4.18")
    # END DEPENDENCIES

