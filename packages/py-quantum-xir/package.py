# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyQuantumXir(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.2.2", sha256="5acd7955d8d854e216bdeb773afbf534d6fbe2e35ded5295ff0cacc7fd84f9fc", url="https://pypi.org/packages/98/8f/29e6eb321df7777f7b97c818f191d8db05ecbd71d0452de5fbba4605af92/quantum_xir-0.2.2-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-lark-parser@0.11.0:")
    # END DEPENDENCIES

