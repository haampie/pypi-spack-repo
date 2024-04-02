# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyOgb(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("1.3.5", sha256="25a4265cc610de49f481ccd70d80acf57e4d338b3133659c7c5396336c4e5654", url="https://pypi.org/packages/75/b1/33a442a945188c5d1cf3d87487f30a7fce9775b73c119149c0f708aa3caa/ogb-1.3.5-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-numpy@1.16.0:")
        depends_on("py-outdated@0.2:")
        depends_on("py-pandas@0.24.0:")
        depends_on("py-scikit-learn@0.20.0:")
        depends_on("py-six@1.12:")
        depends_on("py-torch@1.6:", when="@1.3.1:")
        depends_on("py-tqdm@4.29:")
        depends_on("py-urllib3@1.24:")
    # END DEPENDENCIES

