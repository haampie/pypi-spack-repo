# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyCwlUtils(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.21", sha256="fba9348bfef42e7d359f1a93e1188f1da40cce714532a3e49901343bae6b01a0", url="https://pypi.org/packages/03/15/a4156b82adf2a6f7575c3229adf1e523237786c25385151460dd8d2eb560/cwl_utils-0.21-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-cachecontrol", when="@0.15:0.25")
        depends_on("py-cwl-upgrader@1.2.3:", when="@0.15:")
        depends_on("py-packaging", when="@0.14:")
        depends_on("py-rdflib", when="@0.15:")
        depends_on("py-requests")
        depends_on("py-schema-salad@8.3.20220825114525:", when="@0.16:0.31")
    # END DEPENDENCIES

