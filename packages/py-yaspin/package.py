##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyYaspin(PythonPackage):
    version("2.1.0", sha256="d574cbfaf0a349df466c91f7f81b22460ae5ebb15ecb8bf9411d6049923aee8d", url="https://pypi.org/packages/ce/ed/1ae83648729025952b483046d5164fc91625703899707655406db76ce671/yaspin-2.1.0-py3-none-any.whl")

    with default_args(type="run"):
        depends_on("python@3.9:", when="@3:")
        depends_on("python@3.8.1:", when="@2.5:2")
        depends_on("py-termcolor@1.1:1", when="@2:2.1")

