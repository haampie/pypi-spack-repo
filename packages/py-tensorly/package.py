# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyTensorly(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.8.1", sha256="08988dbc5e433c3f255d0e00855f99a613fe273d50a1627b7e82b03ff2a6da9a", url="https://pypi.org/packages/71/6c/b07811af60b429d29ff1aab7a8d7b845f24e27462c7455c3df734007dd67/tensorly-0.8.1-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-numpy", when="@:0.4.3,0.6:")
        depends_on("py-scipy", when="@:0.4.3,0.6:")
    # END DEPENDENCIES

