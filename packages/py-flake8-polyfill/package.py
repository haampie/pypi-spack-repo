# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyFlake8Polyfill(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("1.0.2", sha256="12be6a34ee3ab795b19ca73505e7b55826d5f6ad7230d31b18e106400169b9e9", url="https://pypi.org/packages/86/b5/a43fed6fd0193585d17d6faa7b85317d4461f694aaed546098c69f856579/flake8_polyfill-1.0.2-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-flake8")
    # END DEPENDENCIES

