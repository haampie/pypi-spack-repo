# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyDaskXgboost(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.2.0", sha256="47b7d96e981d8d7aa81bd15578f470d80ee92ae5aac122adc3bc7e1c9f941682", url="https://pypi.org/packages/0d/33/90fec71df94921d9e604c1f3812b7bb9573ce93aec0637df8a319a7ea42b/dask_xgboost-0.2.0-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-dask", when="@:0.1.3,0.1.7:")
        depends_on("py-distributed@1.15.2:", when="@:0.1.3,0.1.7:")
        depends_on("py-xgboost@:0", when="@0.1.11:")
    # END DEPENDENCIES

