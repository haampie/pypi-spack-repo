##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyTemplateflow(PythonPackage):
    version("0.7.1", sha256="883dd62ad5ef339ae588d5b74bfec471fd3ec77ff922d5b055ce65c8d6d17cd1", url="https://pypi.org/packages/b7/f9/e5a1abfaa985ffd16ed732573f043b6b3586122ccdffb2f95875862f3251/templateflow-0.7.1-py3-none-any.whl")
    version("0.4.2", sha256="5585f3e7ccaa756f811aafb526ed6b2c79aabfd012477129af9c6038d7686f84", url="https://pypi.org/packages/f5/07/db1bba38404027227c76878674e6a775a2a0bba0ac822c319dda7e3cf76c/templateflow-0.4.2.tar.gz")

    with default_args(type="run"):
        depends_on("py-pybids@0.12.1:", when="@0.7:0")
        depends_on("py-requests", when="@0.6.1:")
        depends_on("py-tqdm", when="@0.6.1:")

