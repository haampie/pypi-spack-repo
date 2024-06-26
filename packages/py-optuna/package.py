# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyOptuna(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("3.2.0", sha256="6140ca7cc1cc6751b5184c9f88cd7bbaaf6172b4bed1792552db9d8931979d77", url="https://pypi.org/packages/a0/8c/f72c6bc61b3c71149af95cd91e16149ea5b5aeae99e6d197f80e79a1035a/optuna-3.2.0-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.7:", when="@3.1:")
        depends_on("py-alembic@1.5:", when="@3.0.2:")
        depends_on("py-cmaes@0.9.1:", when="@3.1.0:3.2")
        depends_on("py-colorlog")
        depends_on("py-numpy")
        depends_on("py-packaging@20:")
        depends_on("py-pyyaml")
        depends_on("py-sqlalchemy@1.3.0:", when="@3.0.2:")
        depends_on("py-tqdm")
    # END DEPENDENCIES

