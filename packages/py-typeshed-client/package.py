# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyTypeshedClient(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("2.1.0", sha256="95aabf54a80ee19b56ac349ca3fb9bdd4cf03e10ee46778ec2ba05e737290ff5", url="https://pypi.org/packages/0f/41/800089b9b6ff9222b2477e59905296baef77464b206cb69f17656a5d9478/typeshed_client-2.1.0-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-importlib-resources@1.4:", when="@1:")
    # END DEPENDENCIES

