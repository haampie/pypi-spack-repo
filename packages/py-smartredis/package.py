##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PySmartredis(PythonPackage):
    version("0.4.1", sha256="fff16ed1eb09648ac3c3f845373beb37f3ffe7414d8745ae36af9daf585f8c5b", url="https://pypi.org/packages/b4/d8/e76272891b2ad97a925be78625d2532ec04b174bdd278a490a61f834ded4/smartredis-0.4.1.tar.gz")
    version("0.4.0", sha256="d12779aa8bb038e837c25eac41b178aab9e16b729d50ee360b5af8f813d9f1dd", url="https://pypi.org/packages/0b/79/760f917f4bf23a6f68ab89fdf65e3e95040aab860d42db70b3aa92589aae/smartredis-0.4.0.tar.gz")

    with default_args(type="run"):
        depends_on("python@:3.11", when="@0.5.1:")
        depends_on("python@:3.10", when="@0.4:0.5.0")

