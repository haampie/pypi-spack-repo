##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyOsqp(PythonPackage):
    version("0.6.5", sha256="b2810aee7be2373add8b6c0be5ad99b810288774abca421751cb032d6a5aedef", url="https://pypi.org/packages/fa/2d/a8b4a4e2c531fb96c384f3b060ee62425dbf36cb4503f3b4aaef59ff5585/osqp-0.6.5.tar.gz")
    version("0.6.4", sha256="cfa33e0be422ee5d3e792e7c081bcbf6fa222fc2175b6fdde4c4a219354c5e42", url="https://pypi.org/packages/7a/23/786fed3b3bf90a3a097c011ca0125676253acbb287906ff00e577ab853c7/osqp-0.6.4.tar.gz")
    version("0.6.3", sha256="03e460e683ec2ce0f839353ddfa3c4c8ffa509ab8cf6a2b2afbb586fa453e180", url="https://pypi.org/packages/f8/ce/951a029a1d783025242c4ee6a42f14d37c58fc6cba104c1be5c1fc6ecfee/osqp-0.6.3.tar.gz")
    version("0.6.2.post9", sha256="16b03bc7c5db921de0d97a308ed874d21af9080660eddd5e7cadb2ba3428b0ff", url="https://pypi.org/packages/3a/50/e15039ce9d1916022f6214067922d98200712023e0e5873f2cbb9f1c2fa4/osqp-0.6.2.post9.tar.gz")
    version("0.6.2.post8", sha256="23d6bae4a3612f60d5f652d0e5fa4b2ead507cabfff5d930d822057ae6ed6677", url="https://pypi.org/packages/5a/61/7b94eb7de2b7c9d12d8757ef9d0f5dfe3c5dc0ba0e88f08d4ae929996a34/osqp-0.6.2.post8.tar.gz")
    version("0.6.2.post7", sha256="f0934ae8668c8fc48fea66e9838a3c30777e027fa6bc151da23d79045342b0de", url="https://pypi.org/packages/06/d8/8119b64ac3d2d27141859c9ed1206de07d259fa0d2147d219786f12f5ae5/osqp-0.6.2.post7.tar.gz")
    version("0.6.2.post5", sha256="b2fa17aae42a7ed498ec261b33f262bb4b3605e7e8464062159d9fae817f0d61", url="https://pypi.org/packages/b5/1c/cc191ce88cb3f0d1aa6eee99553df0b1cc3659e3c01ca6414c3675add8ad/osqp-0.6.2.post5.tar.gz")
    version("0.6.2.post4", sha256="23831d407c52a67789e0490257f91a62b86ddeaf31dbcdefb7d3801e56596154", url="https://pypi.org/packages/17/d2/ab54ca05546939c72e5b410ab6d2d079f542c2d39f3d31e67fd3f2fe64f8/osqp-0.6.2.post4.tar.gz")
    version("0.6.2.post0", sha256="5f0695f26a3bef0fae91254bc283fab790dcca0064bfe0f425167f9c9e8b4cbc", url="https://pypi.org/packages/c0/90/4cf48c200a89e46bcad87e12469ee36fc03d0c3f16b703b747e8c4bf618e/osqp-0.6.2.post0.tar.gz")
    version("0.6.2", sha256="262162039f6ad6c9ffee658541b18cfae8240b65edbde71d9b9e3af42fbfe4b3", url="https://pypi.org/packages/7a/b8/291caf5b448de7b35969b71df83b0733c853656b0304516f6fea8f1c9f78/osqp-0.6.2.tar.gz")
    version("0.6.1", sha256="47b17996526d6ecdf35cfaead6e3e05d34bc2ad48bcb743153cefe555ecc0e8c", url="https://pypi.org/packages/ba/17/49790ce2ce7a6b95cd250642ebc68bd723ddefdd052ee8dcc1e0dcf4ffca/osqp-0.6.1.tar.gz")

    with default_args(type="run"):
        depends_on("py-future", when="@0.2:0.2.0,0.4:0.6.1")
        depends_on("py-numpy@1.7:", when="@0.2:0.2.0,0.4:0.6.1,0.6.4:0")
        depends_on("py-qdldl", when="@0.6.4:0")
        depends_on("py-scipy@0.13.2:1.11", when="@0.6.5:0")
        depends_on("py-scipy@0.13.2:", when="@0.2:0.2.0,0.4:0.6.1,0.6.4")

