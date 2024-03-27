##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyCsvkit(PythonPackage):
    version("1.1.1", sha256="4ab7b4ced265fabecc6af5658166745b29d894d76cdb4bde51507b8a8fdbcfae", url="https://pypi.org/packages/88/49/ba166a86956deda92fc80d3a7032c219f0c80baff822d319d5864d039b35/csvkit-1.1.1-py2.py3-none-any.whl")
    version("1.0.4", sha256="1353a383531bee191820edfb88418c13dfe1cdfa9dd3dc46f431c05cd2a260a0", url="https://pypi.org/packages/66/d8/206e4da52bcf9cc29dfa3a93837b14b37ba42f58ccbd22a42a3b3ae0381a/csvkit-1.0.4.tar.gz")
    version("0.9.1", sha256="92f8b8647becb5cb1dccb3af92a13a4e85702d42ba465ce8447881fb38c9f93a", url="https://pypi.org/packages/f6/5a/4843db5d3ea69c4984fbfd64859e5ae32847e9384ccc82849c27fd33720b/csvkit-0.9.1.tar.gz")

    with default_args(type="run"):
        depends_on("py-agate@1.6.1:", when="@1.0.6:1.3")
        depends_on("py-agate-dbf@0.2.2:", when="@1.0.7:")
        depends_on("py-agate-excel@0.2.2:", when="@1.0.6:")
        depends_on("py-agate-sql@0.5.3:", when="@1.0.6:")

