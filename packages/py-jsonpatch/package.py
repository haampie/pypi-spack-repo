# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyJsonpatch(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("1.23", sha256="8bf92fa26bc42c346c03bd4517722a8e4f429225dbe775ac774b2c70d95dbd33", url="https://pypi.org/packages/a0/e6/d50d526ae2218b765ddbdb2dda14d65e19f501ce07410b375bc43ad20b7a/jsonpatch-1.23-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-jsonpointer@1.9:", when="@1.20:1.24,1.26:")
    # END DEPENDENCIES

