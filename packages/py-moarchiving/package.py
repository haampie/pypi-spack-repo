# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyMoarchiving(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.6.0", sha256="16a2e2e12edfa324da1cd5c7fdf147a45fd7c4884c00ef2d2868a8ebf793b309", url="https://pypi.org/packages/04/42/f294fcaba5ad224a04948a16935d9fee93a449ba174afb4f867ba18fab81/moarchiving-0.6.0-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    variant("arbitrary_precision", default=False, description="arbitrary_precision")
    # END VARIANTS

    # BEGIN DEPENDENCIES
    # END DEPENDENCIES

