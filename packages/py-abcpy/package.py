# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyAbcpy(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.6.3", sha256="b1c6e35d50daae1415085e4380fb643b8af3004ee493b90dd0c27786d9b08095", url="https://pypi.org/packages/af/7e/633fb84eac95a77c6a2e9302e5801da7d87e82014526427345aed5052ec6/abcpy-0.6.3-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-cloudpickle", when="@0.5.6:")
        depends_on("py-coverage")
        depends_on("py-glmnet@2.2.1:", when="@0.6:")
        depends_on("py-matplotlib", when="@0.5.7:")
        depends_on("py-mpi4py", when="@0.5.6:")
        depends_on("py-pot", when="@0.6:")
        depends_on("py-scikit-learn@0.23.1:", when="@0.6:")
        depends_on("py-scipy")
        depends_on("py-sklearn")
        depends_on("py-sphinx", when="@0.5.3:")
        depends_on("py-sphinx-rtd-theme")
        depends_on("py-tqdm", when="@0.5.7:")
    # END DEPENDENCIES

