# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyMultiprocess(PythonPackage):
    # BEGIN VERSIONS
    version("0.70.16", sha256="161af703d4652a0e1410be6abccecde4a7ddffd19341be0a7011b94aeb171ac1", url="https://pypi.org/packages/b5/ae/04f39c5d0d0def03247c2893d6f2b83c136bf3320a2154d7b8858f2ba72d/multiprocess-0.70.16.tar.gz")
    version("0.70.15", sha256="f20eed3036c0ef477b07a4177cf7c1ba520d9a2677870a4f47fe026f0cd6787e", url="https://pypi.org/packages/68/e0/a77ca96e772e13c828fa52f3ad370d413bef194aeaf78b7c6611870ad815/multiprocess-0.70.15.tar.gz")
    version("0.70.14", sha256="3eddafc12f2260d27ae03fe6069b12570ab4764ab59a75e81624fac453fbf46a", url="https://pypi.org/packages/e3/ab/9aafc121c6a3d2470ccdf28f99897e88d324c948893b30e46cb359f595e3/multiprocess-0.70.14.tar.gz")
    version("0.70.13", sha256="2e096dd618a84d15aa369a9cf6695815e5539f853dc8fa4f4b9153b11b1d0b32", url="https://pypi.org/packages/4b/7f/55f7dacc3127a918110763998dfbabbec8dd693bfde9a7df9c4e44f4da29/multiprocess-0.70.13.tar.gz")
    version("0.70.12.2", sha256="206bb9b97b73f87fec1ed15a19f8762950256aa84225450abc7150d02855a083", url="https://pypi.org/packages/99/1a/472900644359cdd208d1fbe71706bdeecbc6e8db2e39c35ebe89459e9172/multiprocess-0.70.12.2.zip")
    version("0.70.12.1", sha256="d73afab98823e06423f68271cce77743fd82ce587090bf5a6ce408396d9a68f3", url="https://pypi.org/packages/26/19/7034777e8ffe6892a27d232466ac81400e7dfb98ba1d3438a15344d2f565/multiprocess-0.70.12.1.zip")
    version("0.70.12", sha256="853d02581a03b3bf7872f5e997d2e2b62e177c22a9d05158dc96a675854f2b60", url="https://pypi.org/packages/c6/ff/d85f76f7fb62745664924414cb58340725b61a61f9226db10bec16de01c9/multiprocess-0.70.12.zip")
    version("0.70.11.1", sha256="9d5e417f3ebce4d027a3c900995840f167f316d9f73c0a7a1fbb4ac0116298d0", url="https://pypi.org/packages/28/22/d41648b1303352bccfa497509a32606085bfb2f99fbb423d8863a635a9fd/multiprocess-0.70.11.1.zip")
    version("0.70.11", sha256="e75f02a8dc3707207d3356e0d272933a718654b54d792fc1f7b2925b5c0e120d", url="https://pypi.org/packages/a4/0a/b0d517755cce23781c69c27b6bfe1463e88ebb63270183807b15e05aa9fc/multiprocess-0.70.11.zip")
    version("0.70.10", sha256="81f388527a0c8766e94fe084fd8a408da5045a9fe7b28e199f684a796f3c6bf8", url="https://pypi.org/packages/1a/4e/4591c45b85fbcbcc3de9554e20e079e0006c4332e0a780ed0883f2b07965/multiprocess-0.70.10.zip")
    version("0.70.9", sha256="9fd5bd990132da77e73dec6e9613408602a4612e1d73caf2e2b813d2b61508e5", url="https://pypi.org/packages/58/17/5151b6ac2ac9b6276d46c33369ff814b0901872b2a0871771252f02e9192/multiprocess-0.70.9.tar.gz")
    version("0.70.7", sha256="46479a327388df8e77ad268892f2e73eac06d6271189b868ce9d4f95474e58e3", url="https://pypi.org/packages/31/60/6d74caa02b54ca43092e745640c7d98f367f07160441682a01602ce00bc5/multiprocess-0.70.7.tar.gz")
    version("0.70.5", sha256="c4c196f3c4561dc1d78139c3e73709906a222d2fc166ef3eef895d8623df7267", url="https://pypi.org/packages/65/03/bd8ac79948049b5a0f7ee5f2642f76dbb2d9cb83cc5433dfb2112f89d69a/multiprocess-0.70.5.zip")
    version("0.70.4", sha256="a692c6dc8392c25b29391abb58a9fbdc1ac38bca73c6f27d787774201e68e12c", url="https://pypi.org/packages/fb/44/308000ee233ce789e139978b15c1da4a8cdb0126522f2cb8a4ba560f4fb3/multiprocess-0.70.4.zip")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-dill@0.3.8:", when="@0.70.16:")
        depends_on("py-dill@0.3.2:", when="@0.70.10")
        depends_on("py-dill@0.2.9:", when="@0.70.7")
    # END DEPENDENCIES

