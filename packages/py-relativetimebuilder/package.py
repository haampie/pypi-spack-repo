# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyRelativetimebuilder(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("3.0.0", sha256="d521b559891589c1f6cbd9573ba5432d608121c6b9d9e3449879c2eac732e61f", url="https://pypi.org/packages/8c/2f/fcdc2a87730e72f748db1e3e03aaab3fad8748358b5d81e0a8d1837ca961/relativetimebuilder-3.0.0-py2.py3-none-any.whl")
    version("2.0.1", sha256="2358ff6645c4a78d5965bc4baa08513e60ec493e5fe84a968a67f990fe8f00b5", url="https://pypi.org/packages/23/b4/940d91a2dcfa29a3bc04c13ccfdddb16827ebe59046fb398089ae7fdd1ab/relativetimebuilder-2.0.1-py2.py3-none-any.whl")
    version("2.0.0", sha256="944331c6ea76e7f9d1ce610b01b235045fe8249d87b2e57ae296c2210f28f191", url="https://pypi.org/packages/5f/20/1600f25c436823d5c6cb6398793590c51247ab5d78f645fe3d2db6ee13df/relativetimebuilder-2.0.0-py2.py3-none-any.whl")
    version("1.0.0", sha256="7b5600a6572075400c2134b1524ab5ffa1e5c7d74db3be37da5eb9520627b024", url="https://pypi.org/packages/38/9d/706d6f206060b8be979672d22d02a2f7355f45de86779fb13dbb098afd45/relativetimebuilder-1.0.0-py2.py3-none-any.whl")
    version("0.2.0", sha256="8b11e6fa6d6d4a09c61cfa9dadae4ea640bf10818e0991874d33452c0aeff2d7", url="https://pypi.org/packages/b9/46/fb188619006d458598d7a8910bbb5cd2c6debfb36821b460532bebddd046/relativetimebuilder-0.2.0-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-aniso8601@9:", when="@3:")
        depends_on("py-aniso8601@7:8", when="@2.0.1:2")
        depends_on("py-aniso8601@7", when="@2:2.0.0")
        depends_on("py-aniso8601@5:6", when="@1")
        depends_on("py-aniso8601@5", when="@0.2:0")
        depends_on("py-python-dateutil@2.7.3:", when="@1:")
    # END DEPENDENCIES

