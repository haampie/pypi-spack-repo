# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyDocutilsStubs(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.0.21", sha256="d8beb6ffac94d2db39179681f6bc17a3b81d3386201dc8b1aec3d61201b1edc9", url="https://pypi.org/packages/8a/1f/441df2631e58ef71eab304b02efe5f7d0e93a887690b887d8f213106abd0/docutils_stubs-0.0.21-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-docutils@0.14", when="@:0.0.21")
    # END DEPENDENCIES

