##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyBiopandas(PythonPackage):
    version("0.2.5", sha256="0c3f770dabf27a4b405ed7606ce90f62e47f3d85d7385b13b8a7ae9964ac8bec", url="https://pypi.org/packages/fd/9a/0aee6d7405e120dd9b911f386a36e9ab5cf1916c38042a4142e3ad90b73a/biopandas-0.2.5.tar.gz")

    with default_args(type="run"):
        depends_on("py-numpy@1.16.2:", when="@0.2.5:")
        depends_on("py-pandas@0.24.2:", when="@0.2.5:")
        depends_on("py-setuptools", when="@0.2.5:")

