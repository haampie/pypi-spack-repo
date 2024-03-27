##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPythonLspJsonrpc(PythonPackage):
    version("1.1.2", sha256="7339c2e9630ae98903fdaea1ace8c47fba0484983794d6aafd0bd8989be2b03c", url="https://pypi.org/packages/cb/d9/656659d5b5d5f402b2b174cd0ba9bc827e07ce3c0bf88da65424baf64af8/python_lsp_jsonrpc-1.1.2-py3-none-any.whl")
    version("1.1.1", sha256="2bd7771bd5e23ba2edb17101432c5fd680bbacedb8dddeb472a8250ca8d936d6", url="https://pypi.org/packages/d3/71/4803437cc06fa10dbe8a90a303e37d1836caf8fe538f9a8fc3bef9e1dc7b/python_lsp_jsonrpc-1.1.1-py3-none-any.whl")
    version("1.1.0", sha256="28d831fac282ba25ffdeb7737549a75c03a827d049589c5e3e16f42b664bc7ab", url="https://pypi.org/packages/fa/31/d4a39670369fc67d3c3f153c0799bf26575740f8b38b81403f6d849bef92/python_lsp_jsonrpc-1.1.0-py3-none-any.whl")
    version("1.0.0", sha256="079b143be64b0a378bdb21dff5e28a8c1393fe7e8a654ef068322d754e545fc7", url="https://pypi.org/packages/06/ee/754bfd5f6bfe7162c10d3ecb0aeef6f882f91d3231596c83f761a75efd0b/python_lsp_jsonrpc-1.0.0-py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-ujson@3:")

