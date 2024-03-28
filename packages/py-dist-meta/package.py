# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyDistMeta(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.8.0", sha256="a01eba9a9a0737e8293d3a7f6750fb7395fc47e96bec59a918912535347360ad", url="https://pypi.org/packages/5c/59/50227daa0c8543094b363bf1c0ea58c8a4877b5d901eb81b4d3f0271dfeb/dist_meta-0.8.0-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-domdf-python-tools@3.1:")
        depends_on("py-handy-archives")
        depends_on("py-packaging@20.9:")
    # END DEPENDENCIES

