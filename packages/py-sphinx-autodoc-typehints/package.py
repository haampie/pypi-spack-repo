# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PySphinxAutodocTypehints(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("1.12.0", sha256="5e81776ec422dd168d688ab60f034fccfafbcd94329e9537712c93003bddc04a", url="https://pypi.org/packages/25/04/f59887284d9ea7e5e1473b74177fc8fca43c949a683750c733a154ba8148/sphinx_autodoc_typehints-1.12.0-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-sphinx@3.0.0:", when="@1.11:1.12")
    # END DEPENDENCIES

