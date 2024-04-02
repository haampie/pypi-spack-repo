# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyCiSdr(PythonPackage):
    # BEGIN VERSIONS
    version("0.0.0", sha256="a1387f39ccd55cce034e2c01000a0a337b3729d8a5010b42c5381d8c820fa4bb", url="https://pypi.org/packages/5e/77/fb5832a1457d2b15a21a9499135d5385ca76888c0232e4141340f1f71e1e/ci_sdr-0.0.0.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@:3")
    # END DEPENDENCIES

