# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyCylcRose(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("1.3.0", sha256="34319cefea4f039de9babc72e79788ca7b38a13f7df52bf26ab862f07005c205", url="https://pypi.org/packages/bd/16/9d591c837df9e0321d678fd65206a01dd74f15afc43e078b2b7d7ad90c3a/cylc_rose-1.3.0-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-cylc-flow@8.2:", when="@1.3:")
        depends_on("py-jinja2", when="@1:")
        depends_on("py-metomi-isodatetime", when="@1:")
        depends_on("py-metomi-rose@2.1", when="@1.3:1.3.1")
    # END DEPENDENCIES

