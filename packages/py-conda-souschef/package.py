# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyCondaSouschef(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("2.2.3", sha256="56c0764022f0b53722e7f25fef396bb2812fc85ff4acc5da64acc48ddb1da4cc", url="https://pypi.org/packages/36/6b/03647c71ea8db50d90d5e404ac9a647733d8d01d1887fc79507ace973743/conda_souschef-2.2.3-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.8:")
        depends_on("py-ruamel-yaml@0.15.3:")
        depends_on("py-ruamel-yaml-jinja2")
    # END DEPENDENCIES

