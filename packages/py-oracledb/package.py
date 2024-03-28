# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyOracledb(PythonPackage):
    # BEGIN VERSIONS
    version("1.2.2", sha256="dd9f63084e44642b484a46b2fcfb4fc921f39facf494a1bab00628fa6409f4fc", url="https://pypi.org/packages/6b/85/a1eaa9e96ad25aee72d70eee2e9f4070b88fcaa343a3270b865d1d1fc865/oracledb-1.2.2.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    variant("impl", default=False)
    # END VARIANTS

    # BEGIN DEPENDENCIES
    # END DEPENDENCIES

