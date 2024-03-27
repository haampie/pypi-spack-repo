##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyMetricLearn(PythonPackage):
    version("0.7.0", sha256="193c218ca967289ab988d307fa18ead34fb0ef439774b06867ca526a05d766a8", url="https://pypi.org/packages/52/51/e5d46bef64e6a39055eecca67b5342a5fefe3744b73a744a58487651a209/metric_learn-0.7.0-py2.py3-none-any.whl")
    version("0.3.0", sha256="80711fc830c817b2dc1da4f85bff45995e432db87da920f42cc5cbf586f81423", url="https://pypi.org/packages/4b/9b/2e6f6bc16665b9d6a8f23fe31f012fb5840cdc67e2378af5871782cba766/metric-learn-0.3.0.tar.gz")
    version("0.2.0", sha256="af2d98c737f2d95c4a2ee07282c59f918553ff61f302a0867f034e4a5e09c638", url="https://pypi.org/packages/42/f7/62f3b3b2dec397af71d2207467d07247e74466b2565454bfcee6416f2741/metric-learn-0.2.0.tar.gz")
    version("0.1.1", sha256="09056f87ed9dc051f31ea6c6bff62d1eb6a3eadf7abc81107fd28cc30026413c", url="https://pypi.org/packages/44/e0/9fd04994d98d1f332860409cddfffd0be4596f585410be722729e8d6ebc0/metric-learn-0.1.1.tar.gz")
    version("0.1.0", sha256="03559e7cd8936ba32ca2a3637f11910a5fa65a1f43260617d4d32c459e7c7272", url="https://pypi.org/packages/b6/03/688cdc00826567cd9a91d543073eb2989b1f8d2458a5aad8b3c7fa2151ef/metric-learn-0.1.0.tar.gz")

    with default_args(type="run"):
        depends_on("py-numpy@1.11.0:", when="@0.7:")
        depends_on("py-scikit-learn@0.21.3:", when="@0.7:")
        depends_on("py-scipy@0.17:", when="@0.7:")

