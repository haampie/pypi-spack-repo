# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyTypesentry(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.2.7", sha256="fcf3b928bfac3009785d9043e55ee303ae00f26d0abf1fc781cd8ea9784eb8c9", url="https://pypi.org/packages/0f/37/3757249f05aac8a08d9742f9a35c17ab6895eb916b83bbf3a23eae6842b2/typesentry-0.2.7-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-colorama@0.3:")
    # END DEPENDENCIES


        # self-dependency
        # depends_on("py-typesentry@0.2.7:", when="@0.2.7:")
