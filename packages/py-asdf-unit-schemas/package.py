# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyAsdfUnitSchemas(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.1.0", sha256="0e104b53c23a9e15541cfa5d101613d2724a9124fc56301324512659afb470d5", url="https://pypi.org/packages/3e/55/78e900affcb8306cb669e52ee2eac670badef4c8d5938e8dae824ef21932/asdf_unit_schemas-0.1.0-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-asdf-standard@1.0.1:", when="@:0.1")
        depends_on("py-importlib-resources@3:", when="@:0.1 ^python@:3.8")
    # END DEPENDENCIES

