# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyRougeScore(PythonPackage):
    # BEGIN VERSIONS
    version("0.1.2", sha256="c7d4da2683e68c9abf0135ef915d63a46643666f848e558a1b9f7ead17ff0f04", url="https://pypi.org/packages/e2/c5/9136736c37022a6ad27fea38f3111eb8f02fe75d067f9a985cc358653102/rouge_score-0.1.2.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.7:", when="@0.1.2:")
    # END DEPENDENCIES

