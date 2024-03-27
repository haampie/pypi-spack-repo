##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyOptuna(PythonPackage):
    version("3.2.0", sha256="6140ca7cc1cc6751b5184c9f88cd7bbaaf6172b4bed1792552db9d8931979d77", url="https://pypi.org/packages/a0/8c/f72c6bc61b3c71149af95cd91e16149ea5b5aeae99e6d197f80e79a1035a/optuna-3.2.0-py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-alembic@1.5:", when="@3.0.2:")
        depends_on("py-cmaes@0.9.1:", when="@3.1.0:3.2")
        depends_on("py-colorlog", when="@2.4:")
        depends_on("py-numpy", when="@2.4:2.5,2.7:")
        depends_on("py-packaging@20:", when="@2.4:")
        depends_on("py-pyyaml", when="@2.9:")
        depends_on("py-sqlalchemy@1.3.0:", when="@3.0.2:")
        depends_on("py-tqdm", when="@2.4:")
        depends_on("py-typing-extensions@3.10:", when="@3.0.0:3.0.1")

