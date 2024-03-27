##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyAsyncLru(PythonPackage):
    version("2.0.4", sha256="ff02944ce3c288c5be660c42dbcca0742b32c3b279d6dceda655190240b99224", url="https://pypi.org/packages/fa/9f/3c3503693386c4b0f245eaf5ca6198e3b28879ca0a40bde6b0e319793453/async_lru-2.0.4-py3-none-any.whl")
    version("2.0.3", sha256="00c0a8899c20b9c88663a47732689ff98189c9fa08ad9f734d7722f934d250b1", url="https://pypi.org/packages/65/7e/06ed5a62dd348c5d94b0bed1be495aec9772e418af296ce4c75266391297/async_lru-2.0.3-py3-none-any.whl")
    version("2.0.2", sha256="d7c2b873e9af5c5a1f0a87a6c145e7e0b4eb92342b7235dda9dd5b10e950d6e2", url="https://pypi.org/packages/17/f8/bdc723f93ec2458db76352e0f2c017331fe284e4e6b749db262199803f81/async_lru-2.0.2-py3-none-any.whl")
    version("2.0.1", sha256="4abb67e22d36fa92205602798fdface58e396c1555c2ab57e29b35725b016d2f", url="https://pypi.org/packages/0b/33/50e8d5fe5bb5ba8ab1b2c4ee8cec961ff7a81723afb2a49d6d1bf6012cc5/async_lru-2.0.1-py3-none-any.whl")
    version("2.0.0", sha256="1340c02462a350f5098ea11af397924b7142a2e1fc7596e67a7baa304cc683eb", url="https://pypi.org/packages/e9/43/2f9cfb08f228a9f18736c06e1baf801e3171db22f1f102943e8304725e97/async_lru-2.0.0-py3-none-any.whl")
    version("1.0.3", sha256="ea692c303feb6211ff260d230dae1583636f13e05c9ae616eada77855b7f415c", url="https://pypi.org/packages/7e/31/a374a167be43c68e369ab954b4bf843f63484b6e1a739f90109a2d6864fb/async_lru-1.0.3-py3-none-any.whl")
    version("1.0.2", sha256="baa898027619f5cc31b7966f96f00e4fc0df43ba206a8940a5d1af5336a477cb", url="https://pypi.org/packages/7e/c1/a3d6207deaaeb582d16dc9a0fd217f192efc9487ce59897131cf9a2bdc1c/async_lru-1.0.2.tar.gz")
    version("1.0.1", sha256="ac1f7138b54d68570391615b1ff758e189ce2b841a16653aae1255f5be5d4d0b", url="https://pypi.org/packages/30/fc/a9a15a5fc778c425320b31da972ea241b9d660f6c95f82a2f134704a96fe/async_lru-1.0.1.tar.gz")
    version("1.0.0", sha256="851318e5e6f6f758efe3f6a083a05d292ccc3a9dae3fdcd2edfe0d7b8bd97ed9", url="https://pypi.org/packages/13/ee/c4ead3f64d50659818ba25baffbf09f48454ff42d4cf2aae0938298c68f5/async_lru-1.0.0.tar.gz")

    with default_args(type="run"):
        depends_on("py-typing-extensions@4:", when="@2.0.3: ^python@:3.10")
        depends_on("py-typing-extensions@4:", when="@2:2.0.2")

