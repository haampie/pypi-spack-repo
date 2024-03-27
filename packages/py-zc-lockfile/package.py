##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyZcLockfile(PythonPackage):
    version("3.0.post1", sha256="ddb2d71088c061dc8a5edbaa346b637d742ca1e1564be75cb98e7dcae715de19", url="https://pypi.org/packages/a7/aa/47f00f32605177a945f3a1b36a1b2bb9a39260566541280fcee27cbff5cf/zc.lockfile-3.0.post1-py3-none-any.whl")
    version("3.0", sha256="d65acf321e5c92ee594c3030e59ddd832f03f6dc3c7d7cae1c5607e99fa80dc7", url="https://pypi.org/packages/ae/e0/d1133fa4fa3943d47115088c0dd98dcdfb59c00d42cc379534c1b174a391/zc.lockfile-3.0-py3-none-any.whl")
    version("2.0", sha256="cc33599b549f0c8a248cb72f3bf32d77712de1ff7ee8814312eb6456b42c015f", url="https://pypi.org/packages/6c/2a/268389776288f0f26c7272c70c36c96dcc0bdb88ab6216ea18e19df1fadd/zc.lockfile-2.0-py2.py3-none-any.whl")
    version("1.4", sha256="95a8e3846937ab2991b61703d6e0251d5abb9604e18412e2714e1b90db173253", url="https://pypi.org/packages/58/c2/d7c89bdad237b4b7837609172be3e8bf5630796c0020494a15b97ece8eb1/zc.lockfile-1.4.tar.gz")
    version("1.3.0", sha256="96cb13769e042988ea25d23d44cf09342ea0f887083d0f9736968f3617665853", url="https://pypi.org/packages/f5/fe/efb94907d8b2b81c3beab1bd628ff67e310d82816b94aa00b52062727ea9/zc.lockfile-1.3.0.tar.gz")
    version("1.2.1", sha256="11db91ada7f22fe8aae268d4bfdeae012c4fe655f66bbb315b00822ec00d043e", url="https://pypi.org/packages/bd/84/0299bbabbc9d3f84f718ba1039cc068030d3ad723c08f82a64337edf901e/zc.lockfile-1.2.1.tar.gz")
    version("1.2.0", sha256="072f47bae2b9bf7aec8e30448f475172d74c6c7d6b54dd7304e31f3fad6ee4f4", url="https://pypi.org/packages/23/c7/b17e6fe624d0e7c581ca4392b4811d534ff82e036cbe9993a278a38c8aae/zc.lockfile-1.2.0.tar.gz")
    version("1.1.0", sha256="1489ff1c4f655420793c46af5b427537e62435b02e83e92d7f74a73ed8a56198", url="https://pypi.org/packages/87/11/885923d10a17a88dd8f8c9cb7dbc20830d6a630bc311dc9cd4faa343f75d/zc.lockfile-1.1.0.zip")
    version("1.0.2", sha256="96bb2aa0438f3e29a31e4702316f832ec1482837daef729a92e28c202d8fba5c", url="https://pypi.org/packages/ed/80/412ad00eb5dc988d1b1f2307e70b3b3d9fb6cf1b0ca69fb989c8a06a558b/zc.lockfile-1.0.2.tar.gz")
    version("1.0.1", sha256="4698b5d90234fff41e585420aec9206aa4c9f783818f7a263ab31f52ead73d34", url="https://pypi.org/packages/e2/8d/fa7aab5b03a96bb6a90facb6fb37a83985e83fc1866c265a8d2b271749cd/zc.lockfile-1.0.1.tar.gz")

    with default_args(type="run"):
        depends_on("py-setuptools", when="@2:")
