# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyMlDtypes(PythonPackage):
    # BEGIN VERSIONS
    version("0.3.1", sha256="60778f99194b4c4f36ba42da200b35ef851ce4d4af698aaf70f5b91fe70fc611", url="https://pypi.org/packages/16/6e/9a7a51ee1ca24b8e92109128260c5aec8340c8fe5572e9ceecddae559abe/ml_dtypes-0.3.1.tar.gz")
    version("0.2.0", sha256="6488eb642acaaf08d8020f6de0a38acee7ac324c1e6e92ee0c0fea42422cb797", url="https://pypi.org/packages/fa/47/09ca9556bf99cfe7ddf129a3423642bd482a27a717bf115090493fa42429/ml_dtypes-0.2.0.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.9:", when="@0.3:")
    # END DEPENDENCIES

