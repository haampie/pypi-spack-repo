# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyAioftp(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.22.3", sha256="93d17d5d3b8033570f2dfee013172d49e52323437925120ec87190539113ebd0", url="https://pypi.org/packages/0f/5f/81bb77d4e2e5569106f2b9420d126d3c5531f4dc33a772ddd9eea57e03aa/aioftp-0.22.3-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.8:", when="@0.22.3:")
    # END DEPENDENCIES

