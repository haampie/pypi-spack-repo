##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyCertipy(PythonPackage):
    version("0.1.3", sha256="f272c13bfa9af6b2f3f746329d08adb66af7dd0bbb08fc81175597f25a7284b5", url="https://pypi.org/packages/4e/c4/02194a623c03547306c5edfb6b1c0fadaa35ad7fdc2a93b2c1e5e86afc51/certipy-0.1.3-py3-none-any.whl")
    version("0.1.2", sha256="3dd0d3622a24222dd40755d2e0c111258fd67c9ab9fd2da37b298e6d5108f17a", url="https://pypi.org/packages/3f/c2/e21906bf5fe2a3dd2d26fe59ab30a25ebf1d2026a27949655e84f0c4b996/certipy-0.1.2-py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-pyopenssl")

