# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkShazamkit(PythonPackage):
    # BEGIN VERSIONS
    version("10.2", sha256="f3359be7a0ffe0084d047b8813dd9e9b5339a0970baecad89cbe85513e838e74", url="https://pypi.org/packages/5c/ef/080d25bdeec9147d4dc029c9f15d4291c73db311473d5c6dd14f4f82128f/pyobjc-framework-ShazamKit-10.2.tar.gz")
    version("10.1", sha256="d091c5104adda8d54e65463862550e59f86646fdafcdcd234c9a7a2624584f1d", url="https://pypi.org/packages/e6/f2/73183e9b978be5c705261e27d275830f5b6c7689f3fd5d2a9f061d0ca454/pyobjc-framework-ShazamKit-10.1.tar.gz")
    version("10.0", sha256="f5a84113307bac14460abf522ed2e5fc99c5ac1816e652d2bdb437623ada3429", url="https://pypi.org/packages/99/8d/3287082d990b6a5e842fdb2207c6f798219899ca5a84ca0586f12c5f965e/pyobjc-framework-ShazamKit-10.0.tar.gz")
    version("9.2", sha256="612e7a60fde56148d1a9f12a7447198bd57bc6b792c03c58e785664d447c4df6", url="https://pypi.org/packages/14/b7/253167e9c3343dfdc66131830df8dde7175ae0c91331807d3d2e2fede10b/pyobjc-framework-ShazamKit-9.2.tar.gz")
    version("9.1.1", sha256="757410712eba85c227ecca5574b858158757ed143dc05714d9a85bf029ca93f9", url="https://pypi.org/packages/6b/4c/b45b6d410ceb94a8515fa023f62eba857d17e30b509ae6dc57c1a07b735f/pyobjc-framework-ShazamKit-9.1.1.tar.gz")
    version("9.1", sha256="7911e8076f6798fa93589a494e82ff1a44a4d3ea8d9936d9c31c87df7f57caab", url="https://pypi.org/packages/37/50/651b8c17db6eefe121aeb6586d5128eaea1fa10294a994cd35d7af5b7af5/pyobjc-framework-ShazamKit-9.1.tar.gz")
    version("9.0.1", sha256="e9b6d2554b876754613b6ebc668f4b0f1d22ac5d373fa10c3d8eea4d3bd972eb", url="https://pypi.org/packages/7a/6e/95e8b54b1b660267cd71fbbee2065979f59875492a43a7175ac1c0eb848a/pyobjc-framework-ShazamKit-9.0.1.tar.gz")
    version("9.0", sha256="70d1b2207bfaee124489b1f2f9b1ffbd9ee24b5ee2464029b0db4a4708ae6e2d", url="https://pypi.org/packages/85/f8/7c80d4bf9892530593eaa719ace1582a54bcfaf1f062dfa5a143f4b1694e/pyobjc-framework-ShazamKit-9.0.tar.gz")
    version("8.5.1", sha256="df349c8fa3dfa29fb8da5acae661483528f00a2604f0ac4b7c70393bb06ea486", url="https://pypi.org/packages/a2/4c/e292c5a843483cf337d2e26fdb5e071514d204e9df90ac4b0193e1dfe574/pyobjc-framework-ShazamKit-8.5.1.tar.gz")
    version("8.5", sha256="72fe03ce245352364e99abddce86044c25ff0de6aa334efd97cf68d6d91c4d63", url="https://pypi.org/packages/28/4e/df89360d20cd973808ef8fb60ec31f6ba846bd7b28e9eda21305cee2d7a5/pyobjc-framework-ShazamKit-8.5.tar.gz")
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

