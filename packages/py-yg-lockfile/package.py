# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyYgLockfile(PythonPackage):
    # BEGIN VERSIONS
    version("2.3", sha256="b3fe554a90a7ee97393bc0d2f27068894c401c91b7d92b76c04348fd13b86570", url="https://pypi.org/packages/39/86/19446e44425d4986e156af8990b399afe19df87bcb83b1e3023623143839/yg.lockfile-2.3-py2.py3-none-any.whl")
    version("2.2.2", sha256="470646bba7d0a27f8c63726ce0236dacf78b5dab49b6b1c36b96110968235b95", url="https://pypi.org/packages/4f/f4/147a7b281816c4023485c1d712edd4afb42cc845b530ef7edf4939d6215d/yg.lockfile-2.2.2-py2.py3-none-any.whl")
    version("2.2.1", sha256="770e81da5ea95e161d679ef1de8780c811790d7038442cb94522624e0100a9fe", url="https://pypi.org/packages/f3/a5/820bcb20b5f53aded6cf9f37b40e7a8b21734dade821bbdf0092895693a9/yg.lockfile-2.2.1-py2.py3-none-any.whl")
    version("2.2", sha256="e8411cb70280d8b0d0d82c1de4a1277ff2caee6278b578132c42d1e6a0e19ef5", url="https://pypi.org/packages/9f/ab/c54308d06305c285fb50dd6d2a27dcb05bccaed6ec1acbaffc3af1b0b59d/yg.lockfile-2.2-py2.py3-none-any.whl")
    version("2.1.1", sha256="3156ee5f4fa2511a6e1d544f4dbed39961f4ac40637dc157c0549fca6942ba72", url="https://pypi.org/packages/28/ae/00ac89c07ace97502d530a3cf0cbeac9f171bf166e7f3043f1c932be2483/yg.lockfile-2.1.1.tar.gz")
    version("2.1", sha256="392d62661b027eaf030388996d20c5e5652e65a7a1dff6d3671054ffafc58652", url="https://pypi.org/packages/84/ca/aec8399f6d24297b67a8ed1ce0e0a676a9d1d7561e7d73a6458a63919770/yg.lockfile-2.1.tar.gz")
    version("2.0", sha256="755d8b9d882f6ef809de99a8e288aaf192b225cf521c74681d3b29269f4d19ef", url="https://pypi.org/packages/2d/d7/6c4e92be9e55f6802e8ab65cb5866df752ac7c33fd223b1d7c2a253b9543/yg.lockfile-2.0.zip")
    version("1.1.2", sha256="a6b87c7f2f02375975865f8ff572bf1e041df85f9f1e66aec6ca5ed69da2612f", url="https://pypi.org/packages/61/5b/b70b2e3e97b07ad2da547f5cd8bcdb0768bd2743d57e29b3c7f1a8d4243c/yg.lockfile-1.1.2.zip")
    version("1.1.1", sha256="e1bddddd5f70a5fb7495ff8992347d39fde338d4edceb8e2831e63098c18967a", url="https://pypi.org/packages/ec/35/219f8d8aea24b070cff9b0a9bd1f4e0010896e959ac845f3c0fb8c9d5d16/yg.lockfile-1.1.1.zip")
    version("1.0", sha256="0589c1a46ff52d4fe9cf10a2d6c50671552d093e182d8cc4cedf5f5b65ed76c1", url="https://pypi.org/packages/74/eb/bfb410b11ab65a2b213acbf0ecdd2cd643be44ee45d1555acd4179bb820e/yg.lockfile-1.0.zip")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-jaraco-functools@1.16:", when="@2.3:")
        depends_on("py-jaraco-timing", when="@2.2")
        depends_on("py-tempora", when="@2.3:")
        depends_on("py-zc-lockfile", when="@2.2:")
    # END DEPENDENCIES

