# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyElasticTransport(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("8.4.0", sha256="19db271ab79c9f70f8c43f8f5b5111408781a6176b54ab2e54d713b6d9ceb815", url="https://pypi.org/packages/bd/3b/a2f4a4f1f7578ceaff490961753a75984efc17c17b1f6f59c3a866debeca/elastic_transport-8.4.0-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-certifi", when="@0.1:0,7:")
        depends_on("py-urllib3@1.26.2:1", when="@8:8.4")
    # END DEPENDENCIES

