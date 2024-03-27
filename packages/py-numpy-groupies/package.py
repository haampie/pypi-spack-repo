##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyNumpyGroupies(PythonPackage):
    version("0.9.20", sha256="43c29c8f9fff5e2449a356c352bec0a5bb1a229c4e5b3281641ab04f9b864e8e", url="https://pypi.org/packages/e0/f1/0541f72a6052ad45af1c89f1393b2b7416be50ac549cb5f5e198a9ee8a89/numpy_groupies-0.9.20-py3-none-any.whl")

    with default_args(type="run"):
        depends_on("python@3.9:", when="@0.10:")
        depends_on("py-numpy", when="@0.9.19:0.9.20,0.10:")

