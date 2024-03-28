# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyTatsu(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("4.4.0", sha256="c9211eeee9a2d4c90f69879ec0b518b1aa0d9450249cb0dd181f5f5b18be0a92", url="https://pypi.org/packages/1b/36/00664e684e4bba5730db661847447bbcfe789008a154755013e5f457b648/TatSu-4.4.0-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    variant("future_regex", default=False)
    # END VARIANTS

    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.11:", when="@5.9:")
        depends_on("python@3.10:", when="@5.7.1:5.7.3,5.8:5.8.2")
    # END DEPENDENCIES

