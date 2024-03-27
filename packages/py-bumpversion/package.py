##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyBumpversion(PythonPackage):
    version("0.6.0", sha256="4eb3267a38194d09f048a2179980bb4803701969bff2c85fa8f6d1ce050be15e", url="https://pypi.org/packages/4e/ff/93f0db7b3ca337e9f2a289980083e858775dfb3672b38052c6911b36ea66/bumpversion-0.6.0-py2.py3-none-any.whl")
    version("0.5.3", sha256="6744c873dd7aafc24453d8b6a1a0d6d109faf63cd0cd19cb78fd46e74932c77e", url="https://pypi.org/packages/14/41/8c9da3549f8e00c84f0432c3a8cf8ed6898374714676aab91501d48760db/bumpversion-0.5.3.tar.gz")
    version("0.5.0", sha256="030832b9b46848e1c1ac6678dba8242a021e35e908b65565800c9650291117dc", url="https://pypi.org/packages/ae/62/afe05b3616c8479b248ab9812ec257615a184bfd7799ab5898e74248d068/bumpversion-0.5.0.tar.gz")

    with default_args(type="run"):
        depends_on("py-bump2version", when="@0.6:")

