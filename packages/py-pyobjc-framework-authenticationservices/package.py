# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkAuthenticationservices(PythonPackage):
    # BEGIN VERSIONS
    version("10.2", sha256="1be0f05458c4ebfc3e018cb59b4a8bd9022c42b18fea449b0fbf5def0b5f7ef7", url="https://pypi.org/packages/41/98/6c874be70ae4fc24936ac8d90cf1fbfcdaeff484444080b35cd04fc2adf8/pyobjc-framework-AuthenticationServices-10.2.tar.gz")
    version("10.1", sha256="2d686019564f18390ac16d3b225c6c8fead03d929e8cee16942fc532599e15be", url="https://pypi.org/packages/c5/41/f342cce611abb071edabf2a0fad606e41aa3a949bbfbc6d6e95d5c49156c/pyobjc-framework-AuthenticationServices-10.1.tar.gz")
    version("10.0", sha256="0ee315ccae58e9821d92052ac937f26d4a033b1fbbda1e213b1752b10653ba5b", url="https://pypi.org/packages/55/38/237a6c7581c523eca7cbcaa8834cd17351fbce2793e6f6e91bc4533ceeb3/pyobjc-framework-AuthenticationServices-10.0.tar.gz")
    version("9.2", sha256="3ec9bf583ae9a19f21d862ee1e4599bc492cbc203f85036157befe08486f4e0b", url="https://pypi.org/packages/69/a4/a5b198e4dd54c74a74742e927c14a9f6b47d60fb30796a5d5cdd2f56dc30/pyobjc-framework-AuthenticationServices-9.2.tar.gz")
    version("9.1.1", sha256="cc70578d3dacc1bb11316f3052d986737e997b7ce084380373a47e260c633a86", url="https://pypi.org/packages/fd/7d/fbd5f46237212989763df3f65041b74124d3a6047d37a22966c2e259bf49/pyobjc-framework-AuthenticationServices-9.1.1.tar.gz")
    version("9.1", sha256="1541a36c16435623aade2b3aabdbb841e413de38c3e3cb377e5e45136a9e0ad5", url="https://pypi.org/packages/a4/83/2acb5da2d2ca7ae1f3c1ccfa6fbef1fb011ca8ae7a7c12f90085e2417e32/pyobjc-framework-AuthenticationServices-9.1.tar.gz")
    version("9.0.1", sha256="746b02771f1b53d4649a1014b8986aa595100790202fd3e9f8160074ceb0083b", url="https://pypi.org/packages/2b/fb/adb25224677f4f10d8bef29f29ab8067cad06c1315e2ea4dc61c9aabebf9/pyobjc-framework-AuthenticationServices-9.0.1.tar.gz")
    version("9.0", sha256="3c2f128a9698b4c478672270cb50ef353b69f8a97035dcd0b9e449e5dc905745", url="https://pypi.org/packages/f8/f8/b068975a06a6785cf76aaf856b474266b34e170f2d01b6fb99e1d64e6206/pyobjc-framework-AuthenticationServices-9.0.tar.gz")
    version("8.5.1", sha256="56248a372b88b9febb68af6d54bd74ef066e09d42ba2d7229b5d6933c0974fb2", url="https://pypi.org/packages/a7/ae/9baacefc51a2841a71204cac7bb746399ee57fe1741c3a7a8491f77850a9/pyobjc-framework-AuthenticationServices-8.5.1.tar.gz")
    version("8.5", sha256="f88d2d1d9c5f55836421d20010dea06a5ac0839b503b56415d3c3103f4d84fa2", url="https://pypi.org/packages/1a/c7/a36d8bb2f3f172a23e3a15949361bcfb78defc9107a7ee900e26ae92bcbc/pyobjc-framework-AuthenticationServices-8.5.tar.gz")
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

