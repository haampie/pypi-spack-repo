# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyTfKerasNightly(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.0.0", sha256="bf24dcff1170cca1e39a95787549e8564f166fa64f59dd139a641d9d14e3751e", url="https://pypi.org/packages/1d/4a/7a18e0809f4ddc2ece9c02e55ed924fd06d01e7d2353c4bdda09e1ea8e9f/tf_keras_nightly-0.0.0-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.8:", when="@:2.15")
    # END DEPENDENCIES

