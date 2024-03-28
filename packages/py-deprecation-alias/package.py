# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyDeprecationAlias(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.3.2", sha256="ed2e9dde582530e2a364cae4fa26077fda4adc9b28a44ce94a8ef0ee9271e312", url="https://pypi.org/packages/58/65/b1c462900b300b82d94cff397a6bd6293232644c5741fbc1fcbc385e2de5/deprecation_alias-0.3.2-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-deprecation@2.1:")
        depends_on("py-packaging@20.4:")
    # END DEPENDENCIES

