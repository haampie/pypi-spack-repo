##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyDaskExpr(PythonPackage):
    version("1.0.4", sha256="442463458dbd583768d67d4d6a904904e2b3115bb65e6b8215832e760ab86cf1", url="https://pypi.org/packages/b3/33/59616c0f2694364e21959f73172ec3c865d318c5d3a13010de8428cf3bb9/dask_expr-1.0.4-py3-none-any.whl")
    version("1.0.3", sha256="6820f424f594f063826167e8cebedb6aca03252f4fdb091edb90b6da445c3536", url="https://pypi.org/packages/11/d3/ab426ef795914690dd8b961a88a2bda59c003cacbf804dc26e421c856d03/dask_expr-1.0.3-py3-none-any.whl")
    version("1.0.2", sha256="f99c92178eafc736669dea893cf9c5dd750dff58ccd26af5ad20569b6a160111", url="https://pypi.org/packages/9e/9f/5893615a20e5f097d15acd6b29e98302b4149967365d27701a12724c8d3c/dask_expr-1.0.2-py3-none-any.whl")
    version("1.0.1", sha256="2f299ca583ce5de18b41b91788905ea15506a6da3cad9623f48a0c1877953725", url="https://pypi.org/packages/06/8b/e509ed035185d1f56803979050c1c00d56182c12d8b8ef5196c5a2cc571d/dask_expr-1.0.1-py3-none-any.whl")
    version("1.0", sha256="aebc2f1720a84380fd872af1625e85287e21d57dfba077b2135e6c03c26a80a5", url="https://pypi.org/packages/8f/94/53f9a046ef09080a09f15b3d07a2a159befceffc6dbee7227dcfa61cf79f/dask_expr-1.0-py3-none-any.whl")

    with default_args(type="run"):
        depends_on("python@3.9:")
        depends_on("py-dask@2024.3.1:", when="@1.0.3:")
        depends_on("py-dask@2024.3:2024.3.0", when="@1:1.0.2")
        depends_on("py-pandas@2.0.0:")
        depends_on("py-pyarrow@7:", when="@1:")

