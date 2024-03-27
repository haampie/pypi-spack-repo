##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyTikzplotlib(PythonPackage):
    version("0.10.1", sha256="bf0451b86fe4db40aa742f7e5a180dfaaadf57c746ddb2ab7e58a5163d8be75f", url="https://pypi.org/packages/67/3e/24d1c41cbe520d17cfb887e1d527937ad3b6a1c3dc42c12cd48fa60d2dc7/tikzplotlib-0.10.1-py3-none-any.whl")
    version("0.10.0", sha256="d654696c45595c152e8e0f952931f9520b624c786a223a0e812b7287c8c9714d", url="https://pypi.org/packages/2b/5c/2754abab147bb3dd5767a176b170202965a7c20cf1edf6ebc21f4445be65/tikzplotlib-0.10.0-py3-none-any.whl")
    version("0.9.17", sha256="84d06f84faa41c6dce4540e74d2e2f573dbfb44a5093fa1f2268c286dca9ee28", url="https://pypi.org/packages/a9/34/2fc9454a7ac8b3a6069130539118255db7d1938c63a6c78e6250a0c5a0c2/tikzplotlib-0.9.17-py3-none-any.whl")
    version("0.9.16", sha256="deacbd69d89ecf9edd7d29606c6927b83a952e68ddc6c8ab0fda2c401a574c41", url="https://pypi.org/packages/ba/57/00d72c0003d9f048f17a0d85c496f090903cf97c9843587263c7de84d5b6/tikzplotlib-0.9.16-py3-none-any.whl")
    version("0.9.15", sha256="891dd3d674b59d4197d8d5873d38d39fedf43f11fbd4ab2c9bdd652e662c89da", url="https://pypi.org/packages/95/24/79127905ecc51bc62c8910e19a67c037307775ce3f31d0d36019e4c0acd0/tikzplotlib-0.9.15-py3-none-any.whl")
    version("0.9.14", sha256="5f123c8812ec413776402b16e63837f679e32e25e1bcf74a4c5cf4a2b054d248", url="https://pypi.org/packages/6a/49/3b59d397cde82aa9be1019c28e74c2d0ea45f100b438d017a1e665173b95/tikzplotlib-0.9.14-py3-none-any.whl")
    version("0.9.13", sha256="da9d767cc7db2abf240fcc077d323655d484ab0b8fcd6e4a7a7717cc8729a3d9", url="https://pypi.org/packages/d4/4c/9b0b0defe070690cc02e417cf2d54c1648e33ae2f645abea086056569918/tikzplotlib-0.9.13-py3-none-any.whl")
    version("0.9.12", sha256="4230f8cf75e22168af95f3b048ae2ac095929137654d0bcbb7e446ff161bfec3", url="https://pypi.org/packages/f3/73/02c8703ca824a64714731afb8ade70aeb662fc899d9787be8c2d8ce03ebf/tikzplotlib-0.9.12-py3-none-any.whl")
    version("0.9.11", sha256="00eda8ccb19132c1a487c1d7f70c206d06f7a899f4a6a2dd2d00f9ff9bebae56", url="https://pypi.org/packages/01/9b/e1a14465be785d3764dd1aaecba83d2dd323dc35a74b6bd150860228793d/tikzplotlib-0.9.11-py3-none-any.whl")
    version("0.9.10", sha256="f7e1bc42df4da3f44848009dc55e015ab3bf1e213f0d84ae313c38b400339243", url="https://pypi.org/packages/66/9b/35b00f38e5896d8dfa842bd1940238c09de5f692b92c37bf2ef18bcf3fd8/tikzplotlib-0.9.10-py3-none-any.whl")
    version("0.9.8", sha256="e9c33fa35d7ec3024674207469f86bd9a29128783b55fc6b3bee968e8e28a8db", url="https://pypi.org/packages/e7/92/8c988a21d71cc773a63d5d25814cbdce16bf064899242d14e03d6a4f5df3/tikzplotlib-0.9.8-py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-matplotlib@1.4:")
        depends_on("py-numpy")
        depends_on("py-pillow")
        depends_on("py-webcolors", when="@0.10:")

