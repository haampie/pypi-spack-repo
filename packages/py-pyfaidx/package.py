# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyfaidx(PythonPackage):
    # BEGIN VERSIONS
    version("0.8.1.1", sha256="2694af8e3f35f1890a03f04c0f89ba245caf24ff9e435f2c494b132f537e70f6", url="https://pypi.org/packages/84/8c/910b7aa32a60fbbe0c70d469294b70a9ec57281777a917399f96094d5213/pyfaidx-0.8.1.1-py3-none-any.whl")
    version("0.8.1", sha256="67f17ff741dc9eb74a873c287d2a7370081bdec8ecd2e72447951ce80400a143", url="https://pypi.org/packages/6b/19/5f785e9480dcf83df2dbf40f22c5f342b1f7d87a4b010c6ba83c5ed84d08/pyfaidx-0.8.1-py3-none-any.whl")
    version("0.8.0", sha256="0e40f1a45e52131bcc32dc686c7876cc794505e5dd3e3504c3f56cddb5266930", url="https://pypi.org/packages/96/a4/0a293f71573f5b851bbdc3a11e800ba645be8b4d5231960f3275a5d5d851/pyfaidx-0.8.0-py3-none-any.whl")
    version("0.7.2.2", sha256="4e689bc09f3c5de1d2a1099d059b3b9914629c1c5c3ad08b49ff05af33392e0e", url="https://pypi.org/packages/83/bf/269e9b3a18dfda8a22a2d76decf98725f28ff930bd449f87a194625ba913/pyfaidx-0.7.2.2-py3-none-any.whl")
    version("0.7.2.1", sha256="eee13d35bb5f2aa65932a9ad9dd74fa695aefe6e0baafc5836cfa869a7695acc", url="https://pypi.org/packages/eb/93/07273ec98d61de68a966d2ed7a3f4ee5a4501d1be7821c4c36855fc8548f/pyfaidx-0.7.2.1-py3-none-any.whl")
    version("0.7.2", sha256="50346aa7a365c9b965d554a60197fda9e06c25f072a30051baddb3d8065d60f0", url="https://pypi.org/packages/5e/d5/adb7be6603d12ffbc6742c24b86ae203e04e67a7ca36895eee429552bf18/pyfaidx-0.7.2-py3-none-any.whl")
    version("0.7.1", sha256="3977632b7fd29049f8b11035d7e9dea0e2c5da9c235f982b4c3fae06ff1fa23f", url="https://pypi.org/packages/70/e0/0f968d75b061a46ce01102fa9e434f329d3d62d533765a46ebd248da2c81/pyfaidx-0.7.1.tar.gz")
    version("0.7.0", sha256="9ad5cc9381f0de9c43d4bdec0faf106b828cdfb6f8150ec71cab2ca7c8bee770", url="https://pypi.org/packages/41/a7/a48784cf0bcfa30bc82c53ae951d4870b50576a26c6179ae85f09501ae9f/pyfaidx-0.7.0.tar.gz")
    version("0.6.4", sha256="7ba3bdcb1df4ba749f7665b34e6a052aa4e842406a0df95e6df4717cc123f392", url="https://pypi.org/packages/6e/0a/5dd1f5dfdb136aef4a0978ca5d7455c0bcee2f55ae18487d2dc0282a30bf/pyfaidx-0.6.4.tar.gz")
    version("0.6.3.1", sha256="93adf036a75e08dc9b1dcd59de6a4db2f65a48c603edabe2e499764b6535ed50", url="https://pypi.org/packages/7b/96/ffaccc0ee440d0351ecef1c500e9c55171d3589ec0879fed62ebd1129748/pyfaidx-0.6.3.1.tar.gz")
    version("0.5.5.2", sha256="9ac22bdc7b9c5d995d32eb9dc278af9ba970481636ec75c0d687d38c26446caa", url="https://pypi.org/packages/75/a5/7e2569527b3849ea28d79b4f70d7cf46a47d36459bc59e0efa4e10e8c8b2/pyfaidx-0.5.5.2.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-importlib-metadata", when="@0.7.2.2:")
        depends_on("py-setuptools", when="@0.7.2.1:")
        depends_on("py-six", when="@0.7.2:0.7")
    # END DEPENDENCIES

