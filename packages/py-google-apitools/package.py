# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyGoogleApitools(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.5.32", sha256="b78f74116558e0476e19501b5b4b2ac7c93261a69c5449c861ea95cbc853c688", url="https://pypi.org/packages/5e/cb/cb0311f2ec371c83d6510847476c665edc9cc97564a51923557bc8f0b680/google_apitools-0.5.32-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-fasteners@0.14:", when="@0.5.23:")
        depends_on("py-httplib2@0.8:", when="@0.5.23:")
        depends_on("py-oauth2client@1.4.12:", when="@0.5.23:")
        depends_on("py-six@1.12:", when="@0.5.27:")
    # END DEPENDENCIES

