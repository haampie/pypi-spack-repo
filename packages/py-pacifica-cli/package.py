##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPacificaCli(PythonPackage):
    version("0.5.2", sha256="b8175e109ea2253c883a556fdc7f04972b90154f99984e28aef65b207f717ff7", url="https://pypi.org/packages/45/a6/f275a9e2e3494542f3477887a5beb8fe411f0519e0f8c3da15ea77e771d5/pacifica_cli-0.5.2-py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-jsonschema", when="@0.5:")
        depends_on("py-pacifica-downloader@0.4.1:", when="@0.5.1:")
        depends_on("py-pacifica-namespace", when="@0.5:")
        depends_on("py-pacifica-uploader@0.3.1:", when="@0.5.1:")
        depends_on("py-pager")

