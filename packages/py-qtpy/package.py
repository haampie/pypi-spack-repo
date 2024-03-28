# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyQtpy(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("1.11.2", sha256="83c502973e9fdd7b648d8267a421229ea3d9a0651c22e4c65a4d9228479c39b6", url="https://pypi.org/packages/73/47/cc42c2b4fe4ddb7e289ef8f098c7249903ad09cd3f6ee8ec17c63de2b728/QtPy-1.11.2-py2.py3-none-any.whl")
    version("1.7.1", sha256="166766ec89365e43b9a7c733f2362b66325ea039dc4806cfa7aec4199f43662c", url="https://pypi.org/packages/14/a8/6145994bd4eb03f2bfe54a87665588891dacf2dd5e96ca6546cf16d76f45/QtPy-1.7.1-py2.py3-none-any.whl")
    version("1.2.1", sha256="fdeceddd7933906b96785c752e5be6705f890929df5d42e0985b6ef4206a41ad", url="https://pypi.org/packages/ed/38/17a3d96166824662d162d886f263905dbf3a0a66fec74989a3ac9a88afb6/QtPy-1.2.1-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    variant("api", default=False)
    # END VARIANTS

    # BEGIN DEPENDENCIES
    # END DEPENDENCIES

