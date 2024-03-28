# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyApeyeCore(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("1.1.4", sha256="084bc696448d3ac428fece41c1f2eb08fa9d9ce1d1b2f4d43187e3def4528a60", url="https://pypi.org/packages/f4/af/7cfe2c5e01d70848ac1731c8ab37e0e49ab39cf18e595446c192349639c0/apeye_core-1.1.4-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-domdf-python-tools@2.6:")
        depends_on("py-idna@2.5:")
    # END DEPENDENCIES

