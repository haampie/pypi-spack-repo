##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyDescartes(PythonPackage):
    version("1.1.0", sha256="135a502146af5ed6ff359975e2ebc5fa4b71b5432c355c2cafdc6dea1337035b", url="https://pypi.org/packages/1d/6f/81735a30432b74f41db6754dd13869021ccfed3088d1cf7a6cfc0af9ac49/descartes-1.1.0.tar.gz")
    version("1.0.2", sha256="078ef4b50baeafd0cbde538750911ca60161829a8696ae2c7e5a6a1071af1257", url="https://pypi.org/packages/52/65/6078084b6b84b8c87730f9ebf825fbcd7f1ba7bf383fbb6f0a8a6d2419af/descartes-1.0.2.tar.gz")
    version("1.0.1", sha256="d2cec01cb2517f693c40567d3a3ec0e580768f6df5fd002bac5ee2ed7e28af16", url="https://pypi.org/packages/eb/2d/c0b511e8ced8478e6cef9834bdbfe811b7d7280d69f0aaec8b16a2d9d5e9/descartes-1.0.1.tar.gz")
    version("1.0", sha256="b6e5688534805ac36421cd93000f1dc453aa5cec8cbd05b3de5e1226197a6bea", url="https://pypi.org/packages/d6/ed/0cb064e19d4f8e597d426a847bf6073c31c1db0dc471d5e3b966c267c70b/descartes-1.0.tar.gz")
    version("0.1.2", sha256="695f525c00381c60d3c1d8665936df51ed5a1b20b0fe2cf6a194a7eb0da0d3b6", url="https://pypi.org/packages/63/cb/27f47e1de6b75ca551832879b756f730427e3c670596fe49ee0df2dddafe/descartes-0.1.2.tar.gz")
    version("0.1.1", sha256="472e59132d04d6e4bfc1d41fe07fca659ba63a1376c872ef78630a856abe7823", url="https://pypi.org/packages/08/5c/6f9267dc5b1211818a89274048c2e50868a8aade1aab959161b74cd41678/descartes-0.1.1.tar.gz")
    version("0.1", sha256="85453d07ced4a35bb2f6ee416af5dbbcdf8f596208decaca10ac393108d29681", url="https://pypi.org/packages/f5/77/214fb0b9eb260b8c4d1b6b5cf26e6c2a86b3916f24e49c92023ef2c99247/descartes-0.1.tar.gz")

    with default_args(type="run"):
        depends_on("py-matplotlib", when="@1.1:")

