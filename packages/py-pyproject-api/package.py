# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyprojectApi(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("1.6.1", sha256="4c0116d60476b0786c88692cf4e325a9814965e2469c5998b830bba16b183675", url="https://pypi.org/packages/cf/b4/39eea50542e50e93876ebc09c4349a9c9eee9f6b9c9d30f88c7dc5433db8/pyproject_api-1.6.1-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-packaging@23.1:", when="@1.5.2:")
        depends_on("py-tomli@2.0.1:", when="@1: ^python@:3.10")
    # END DEPENDENCIES

