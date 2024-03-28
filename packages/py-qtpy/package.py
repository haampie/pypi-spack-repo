# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyQtpy(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("2.4.1", sha256="1c1d8c4fa2c884ae742b069151b0abe15b3f70491f3972698c683b8e38de839b", url="https://pypi.org/packages/7e/a9/2146d5117ad8a81185331e0809a6b48933c10171f5bac253c6df9fce991c/QtPy-2.4.1-py3-none-any.whl")
    version("2.4.0", sha256="4d4f045a41e09ac9fa57fcb47ef05781aa5af294a0a646acc1b729d14225e741", url="https://pypi.org/packages/be/a1/13bdd2f6237379744c52cec33d417a5819a07455d880e3c5f517c13a0f21/QtPy-2.4.0-py3-none-any.whl")
    version("2.3.1", sha256="5193d20e0b16e4d9d3bc2c642d04d9f4e2c892590bd1b9c92bfe38a95d5a2e12", url="https://pypi.org/packages/51/9f/495736f9bbebc56b9f2ba3d95df1045fd367378254f799e86463b0037ab0/QtPy-2.3.1-py3-none-any.whl")
    version("2.3.0", sha256="8d6d544fc20facd27360ea189592e6135c614785f0dec0b4f083289de6beb408", url="https://pypi.org/packages/ca/56/3dfbcf8a6808d2b3566b75759c48a281bcdc2b9547760e5d044e6ec7e33b/QtPy-2.3.0-py3-none-any.whl")
    version("2.2.1", sha256="268cf5328f41353be1b127e04a81bc74ec9a9b54c9ac75dd8fe0ff48d8ad6ead", url="https://pypi.org/packages/7f/bc/7d1e8276b6519aba7d619472f8dd4d3298f24cff3431c6c23f4532857ce6/QtPy-2.2.1-py3-none-any.whl")
    version("2.2.0", sha256="d283cfba378b0dbe36a55b68aea8ee2f86cd6ccf06c023af25bbe705ffbb29e5", url="https://pypi.org/packages/8b/51/898d185af59cf0c7e035c0dc2739909d48396f1a08b3231bd0e09564a3e0/QtPy-2.2.0-py3-none-any.whl")
    version("2.1.0", sha256="aee0586081f943029312becece9f63977b0a9e3788f77a6ac8cc74802bb173d6", url="https://pypi.org/packages/3e/66/141c5753d759864a051af23b86584ccf6338348efdfec3e52014aaf16531/QtPy-2.1.0-py3-none-any.whl")
    version("2.0.1", sha256="d93f2c98e97387fcc9d623d509772af5b6c15ab9d8f9f4c5dfbad9a73ad34812", url="https://pypi.org/packages/ae/b0/56e602873b05108f0ef9189a237fefcfbcd2fa3d84130b59e50c84fc90e8/QtPy-2.0.1-py3-none-any.whl")
    version("2.0.0", sha256="74bf26be3288aadc843cf3381d5ef0b82f11417ecdcbf26718a408f32590f1ac", url="https://pypi.org/packages/66/da/b1f7184b82eed20a76066aa0c8482eeababc816012836e47f24090c9f655/QtPy-2.0.0-py3-none-any.whl")
    version("1.11.3", sha256="e121fbee8e95645af29c5a4aceba8d657991551fc1aa3b6b6012faf4725a1d20", url="https://pypi.org/packages/cf/a2/562edbf7be613bd6584543b27f67b30a2fcc39a2e0d5e5f4b9284dbb823e/QtPy-1.11.3-py2.py3-none-any.whl")
    version("1.11.2", sha256="83c502973e9fdd7b648d8267a421229ea3d9a0651c22e4c65a4d9228479c39b6", url="https://pypi.org/packages/73/47/cc42c2b4fe4ddb7e289ef8f098c7249903ad09cd3f6ee8ec17c63de2b728/QtPy-1.11.2-py2.py3-none-any.whl")
    version("1.7.1", sha256="166766ec89365e43b9a7c733f2362b66325ea039dc4806cfa7aec4199f43662c", url="https://pypi.org/packages/14/a8/6145994bd4eb03f2bfe54a87665588891dacf2dd5e96ca6546cf16d76f45/QtPy-1.7.1-py2.py3-none-any.whl")
    version("1.2.1", sha256="fdeceddd7933906b96785c752e5be6705f890929df5d42e0985b6ef4206a41ad", url="https://pypi.org/packages/ed/38/17a3d96166824662d162d886f263905dbf3a0a66fec74989a3ac9a88afb6/QtPy-1.2.1-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    variant("api", default=False)
    # END VARIANTS

    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-packaging", when="@2:")
    # END DEPENDENCIES

