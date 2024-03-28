# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkSafariservices(PythonPackage):
    # BEGIN VERSIONS
    version("10.2", sha256="723de09afb718b05d03cbbed42f90d36356294b038ca6422c88d50240047b067", url="https://pypi.org/packages/19/dd/df3b26cd620ec9dcb7ce58c6ceb67831fb1f430e36e9c4f5b582ffe9b62a/pyobjc-framework-SafariServices-10.2.tar.gz")
    version("10.1", sha256="5a9105d3aea43cd214583acd06609f56ed704ce816cb103916324e8ed8388fce", url="https://pypi.org/packages/e7/67/ec37c91435ae7e1f86522cf3d0e536522ce96dac85f2a5d5f74470b12f87/pyobjc-framework-SafariServices-10.1.tar.gz")
    version("10.0", sha256="7f7a477b77b17161e22bdddc8a16fb3000eeccc430a730cb144e1a84a5f6e4e3", url="https://pypi.org/packages/f0/7a/f30aa5a29d37caa63d62a1560cbe2255921a3d59f69e4b90650517e65060/pyobjc-framework-SafariServices-10.0.tar.gz")
    version("9.2", sha256="2b83ebe4f855638341f838781534d3cc7148fa7259d0a223da9cbc28436dec54", url="https://pypi.org/packages/fc/1f/cc4d9e370138ae6a16d32efc009949463850901952d436b0cdfae5b77da3/pyobjc-framework-SafariServices-9.2.tar.gz")
    version("9.1.1", sha256="e820296401fde9dd920c0640182cd0b36f432e74f3054cf4588b184cea702668", url="https://pypi.org/packages/79/b9/5ea2d2c9e2b7bf03d616b823d58616cdd5669daba4f7ea0e70fbc297ebf5/pyobjc-framework-SafariServices-9.1.1.tar.gz")
    version("9.1", sha256="f3dd8d50a89c4c26a628cdedc80988e813e3728091c4c02f70662f4450c28a4a", url="https://pypi.org/packages/84/60/b74696038a957a5d0806b3c8d10f1b040f889d977962f6812f0ad69dc8ac/pyobjc-framework-SafariServices-9.1.tar.gz")
    version("9.0.1", sha256="a6433583192e30f7f70b0d3282237389f56bfc1ab3ac00fc616606b869e9e0d8", url="https://pypi.org/packages/05/ce/ed0533c57c2876a8facc456b7feb5866e06e199f6c24df2481de67d1716e/pyobjc-framework-SafariServices-9.0.1.tar.gz")
    version("9.0", sha256="be32f4d4a010fb68b71782f1ee1787de9c7507171ccccb5937c63cfb3cc3fe01", url="https://pypi.org/packages/e8/11/5c57a61af4e4b0f75b2f6af44a179d6919bbd3952e38d0adf98f655ad6b1/pyobjc-framework-SafariServices-9.0.tar.gz")
    version("8.5.1", sha256="551a8ec407d455288efa8b31a5f50b4607399e53a0f41283d958709c87fee20d", url="https://pypi.org/packages/3d/ef/d2608316c502269b1a343ca905b4f318a66359db78074f3c545f4861e6ab/pyobjc-framework-SafariServices-8.5.1.tar.gz")
    version("8.5", sha256="eb802ef43ad8c39aebcd2ff4a03db4d6d6ba3a2cbf65a377c0a5676003dd8da2", url="https://pypi.org/packages/54/3b/4d28911c26fe3c39e41a09d9647ef55b32353fac6586a084eb092dcbf35c/pyobjc-framework-SafariServices-8.5.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-pyobjc-core@10.2:", when="@10.2:")
        depends_on("py-pyobjc-core@10.1:", when="@10.1")
        depends_on("py-pyobjc-core@10:", when="@10:10.0")
        depends_on("py-pyobjc-framework-cocoa@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-cocoa@10.1:", when="@10.1")
        depends_on("py-pyobjc-framework-cocoa@10:", when="@10:10.0")
    # END DEPENDENCIES

