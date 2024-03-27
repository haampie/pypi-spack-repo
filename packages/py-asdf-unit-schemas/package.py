##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyAsdfUnitSchemas(PythonPackage):
    version("0.2.0", sha256="6a2af1aeda688bc4994e7c933badbee0ff7e61f1ba3121159635c51510979b8d", url="https://pypi.org/packages/e8/74/56957ec9c6e04a8ec7f578bbd558d206a1779c394e171ed2cf0da60fc9c3/asdf_unit_schemas-0.2.0-py3-none-any.whl")
    version("0.1.0", sha256="0e104b53c23a9e15541cfa5d101613d2724a9124fc56301324512659afb470d5", url="https://pypi.org/packages/3e/55/78e900affcb8306cb669e52ee2eac670badef4c8d5938e8dae824ef21932/asdf_unit_schemas-0.1.0-py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-asdf-standard@1.0.1:", when="@:0.1")
        depends_on("py-importlib-resources@3:", when="@:0.1 ^python@:3.8")

