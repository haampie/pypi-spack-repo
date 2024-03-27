##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyXhistogram(PythonPackage):
    version("0.3.2", sha256="ad55330d55296d273b3370678223fde0f50085e04cb744c7b3b0bb7702a2c6bf", url="https://pypi.org/packages/18/08/1432dd10193a5d45294bd42042a5631259ee5a12cd2e9075350546d07a03/xhistogram-0.3.2-py3-none-any.whl")
    version("0.3.1", sha256="eb5763370ab09afe34196bd06fc86af6eca8cfd67830974f090022824de3c495", url="https://pypi.org/packages/21/7d/1e4fb74edf05e184d842cc8348fd3246232516495af9254c276f34ca3b52/xhistogram-0.3.1-py3-none-any.whl")
    version("0.3.0", sha256="d90c311d38bb0332eb363f6cf8b7398635ac4b4063cf7e86259cff8f951f63f4", url="https://pypi.org/packages/e7/58/f17dea189f1113139d30310291e70cf511d436cfd094ee8cace83b45071d/xhistogram-0.3.0-py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-dask@2.3:+array", when="@0.3.2:")
        depends_on("py-dask+array", when="@0.3.1")
        depends_on("py-dask", when="@:0.3.0")
        depends_on("py-numpy@1.17.0:", when="@0.3:")
        depends_on("py-xarray@0.12:")

