# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyYtopt(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.0.1", sha256="9f373a4802b18f3ce12537a106763489d7a9112500fcfde92191b696023a7662", url="https://pypi.org/packages/b3/71/29066bc101b0f62215bbaf55a4a7ef1c8138b5d74107a2434e2a8c139df4/ytopt-0.0.1-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    variant("online", default=False, description="online")
    # END VARIANTS

    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-gym")
        depends_on("py-joblib")
        depends_on("py-keras")
        depends_on("py-mpi4py@3:")
        depends_on("py-numpy")
        depends_on("py-scikit-learn")
        depends_on("py-scikit-optimize")
        depends_on("py-tensorflow@1.11.0:")
        depends_on("py-tqdm")
    # END DEPENDENCIES

