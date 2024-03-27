##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPystan(PythonPackage):
    version("3.5.0", sha256="b4a879f95ff62fab465726163833dcf3f445258acb115103efb143920e66cd21", url="https://pypi.org/packages/e9/21/b20cd3ba84781acdfeb02cee472892740786fe26af7df0b20caaa3d89f43/pystan-3.5.0-py3-none-any.whl")
    version("3.4.0", sha256="9d9f34a20c16f624a9002baaec174b4759230257f46691b9180cb13a67398691", url="https://pypi.org/packages/ac/a4/654b553891b29a58edd3d2ea728b19a986ff4e7198cde257e96e15eee7e4/pystan-3.4.0-py3-none-any.whl")
    version("2.19.1.1", sha256="fa8bad8dbc0da22bbe6f36af56c9abbfcf10f92df8ce627d59a36bd8d25eb038", url="https://pypi.org/packages/10/9f/dcecf31ac08842a675ec337a14439b37d75f6da42f034b1fd5eb90b10b84/pystan-2.19.1.1.tar.gz")
    version("2.19.0.0", sha256="b85301b960d5991918b40bd64a4e9321813657a9fc028e0f39edce7220a309eb", url="https://pypi.org/packages/48/64/dc7152b7ca88903669c296beddf3a8de839c3900684136514293dc99d432/pystan-2.19.0.0.tar.gz")

    with default_args(type="run"):
        depends_on("python@3.9:", when="@3.9:")
        depends_on("py-aiohttp@3.6.0:3", when="@3:")
        depends_on("py-clikit@0.6:", when="@3.0.0:")
        depends_on("py-cython@0.22:0.25.0,0.25.2:", when="@2.16,2.18:2")
        depends_on("py-httpstan@4.8", when="@3.5")
        depends_on("py-httpstan@4.7", when="@3.4")
        depends_on("py-numpy@1.19.0:1", when="@3.4:")
        depends_on("py-numpy@1.7:", when="@2.4.0.2,2.8.0.1:2.8,2.10:2.11,2.16,2.18:2")
        depends_on("py-pysimdjson@3.2:3", when="@3.0.0:3.5")
        depends_on("py-setuptools", when="@3.4:")

