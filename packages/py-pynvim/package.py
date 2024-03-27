##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPynvim(PythonPackage):
    version("0.5.0", sha256="2ac197ef0cdfff53719184a45c33cfb7cef88d1c9bf7f0525c21b3239cb5365f", url="https://pypi.org/packages/8e/40/ee2ec24f1b5ca528f4a87b09c55346c4b67014ad11c1f60ee6b3878b3222/pynvim-0.5.0-py2.py3-none-any.whl")
    version("0.4.3", sha256="3a795378bde5e8092fbeb3a1a99be9c613d2685542f1db0e5c6fd467eed56dff", url="https://pypi.org/packages/7a/01/2d0898ba6cefbe2736283ee3155cba1c602de641ca5667ac55a0e4857276/pynvim-0.4.3.tar.gz")
    version("0.4.2", sha256="6bc6204d465de5888a0c5e3e783fe01988b032e22ae87875912280bef0e40f8f", url="https://pypi.org/packages/9c/76/d16f58648f4d3398ecd5b48ae7fb064f1701c51fe094e0b7b4e08586df0c/pynvim-0.4.2.tar.gz")
    version("0.4.1", sha256="55e918d664654cfa1c9889d3dbe7c63e9f338df5d49471663f78d54c85e84c58", url="https://pypi.org/packages/06/5c/a7a3eb3787c81a11f0c02a11b1ee7d5736d67f5a919c9999ac57479636bd/pynvim-0.4.1.tar.gz")
    version("0.4.0", sha256="71fd8bb3285deeda8c259383066214e0d522a96bfb3ca4871333adfcb454e9d6", url="https://pypi.org/packages/94/73/9fcf169c4bf1bc6d931a1f4002b139a34950ba5804b9066ffd35fc791550/pynvim-0.4.0.tar.gz")
    version("0.3.2", sha256="cf6490c4e586c9da01a32f3e0ae21c61342d7ea171e06025bda210bdc95cbe05", url="https://pypi.org/packages/a7/53/96efef2d4ca3a031d750ff6089ec8335371a840231b76225ae5a3d9ec936/pynvim-0.3.2.tar.gz")
    version("0.3.1", sha256="dd881595055869c2de770517d403faf40d31aa991db2472a1843ff17db47b0fb", url="https://pypi.org/packages/03/26/507e0e1114341cae48af6c6cbb6efa2ea7bcce5866164bca3a22502fee00/pynvim-0.3.1.tar.gz")

    with default_args(type="run"):
        depends_on("py-greenlet@3.0.0:", when="@0.5:")
        depends_on("py-msgpack", when="@0.5:")

