##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PySingularityHpc(PythonPackage):
    version("0.1.16", sha256="107aa1f404f72cab5e94f37fad5a840ba9334e4c7e740aeabaa376e861f84f27", url="https://pypi.org/packages/06/14/621cca31ae5bb83fd9475474aae5394d00829a0a32e3b81cc97f44a48820/singularity_hpc-0.1.16-py3-none-any.whl")
    version("0.1.12", sha256="c525ee645f9a1cbd7e944f9779d3c03ad4c9998c67cfb85269851a9af7f1b704", url="https://pypi.org/packages/51/3c/76820d3562dba9d675e2f22ccc1b1993f0ad92f0debc78c2edd5e68fb4c2/singularity_hpc-0.1.12-py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-jinja2", when="@0.0.5,0.0.43:0.0.49,0.0.51:")
        depends_on("py-jsonschema", when="@0.0.5,0.0.43:0.0.49,0.0.51:")
        depends_on("py-requests", when="@0.0.5,0.0.49,0.0.51:")
        depends_on("py-ruamel-yaml", when="@0.0.5,0.0.43:0.0.49,0.0.51:0.1.23,0.1.26:")
        depends_on("py-spython@0.2:", when="@0.0.51:")

