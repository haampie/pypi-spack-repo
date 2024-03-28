# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyMetricLearn(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.7.0", sha256="193c218ca967289ab988d307fa18ead34fb0ef439774b06867ca526a05d766a8", url="https://pypi.org/packages/52/51/e5d46bef64e6a39055eecca67b5342a5fefe3744b73a744a58487651a209/metric_learn-0.7.0-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-numpy@1.11.0:", when="@0.7:")
        depends_on("py-scikit-learn@0.21.3:", when="@0.7:")
        depends_on("py-scipy@0.17:", when="@0.7:")
    # END DEPENDENCIES

