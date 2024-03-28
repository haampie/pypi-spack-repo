# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyMultiprocess(PythonPackage):
    # BEGIN VERSIONS
    version("0.70.12.2", sha256="206bb9b97b73f87fec1ed15a19f8762950256aa84225450abc7150d02855a083", url="https://pypi.org/packages/99/1a/472900644359cdd208d1fbe71706bdeecbc6e8db2e39c35ebe89459e9172/multiprocess-0.70.12.2.zip")
    version("0.70.9", sha256="9fd5bd990132da77e73dec6e9613408602a4612e1d73caf2e2b813d2b61508e5", url="https://pypi.org/packages/58/17/5151b6ac2ac9b6276d46c33369ff814b0901872b2a0871771252f02e9192/multiprocess-0.70.9.tar.gz")
    version("0.70.7", sha256="46479a327388df8e77ad268892f2e73eac06d6271189b868ce9d4f95474e58e3", url="https://pypi.org/packages/31/60/6d74caa02b54ca43092e745640c7d98f367f07160441682a01602ce00bc5/multiprocess-0.70.7.tar.gz")
    version("0.70.5", sha256="c4c196f3c4561dc1d78139c3e73709906a222d2fc166ef3eef895d8623df7267", url="https://pypi.org/packages/65/03/bd8ac79948049b5a0f7ee5f2642f76dbb2d9cb83cc5433dfb2112f89d69a/multiprocess-0.70.5.zip")
    version("0.70.4", sha256="a692c6dc8392c25b29391abb58a9fbdc1ac38bca73c6f27d787774201e68e12c", url="https://pypi.org/packages/fb/44/308000ee233ce789e139978b15c1da4a8cdb0126522f2cb8a4ba560f4fb3/multiprocess-0.70.4.zip")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-dill@0.2.9:", when="@0.70.7")
    # END DEPENDENCIES

