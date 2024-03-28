# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkAddressbook(PythonPackage):
    # BEGIN VERSIONS
    version("10.2", sha256="d6969fcbde1d78ec9fa0ebcefc2f453090e35d7590c4b4baf62174e060de6bce", url="https://pypi.org/packages/a4/71/2a4b96d82e240c8b8d5ff266e36edabd51fad5648dfdf365b1e2f9d5b2cb/pyobjc-framework-AddressBook-10.2.tar.gz")
    version("10.1", sha256="9b8e01da07703990f0e745945b01cc75c59ade41913edbd6824194e21522efff", url="https://pypi.org/packages/bf/d3/ba75c7f4693d063571037d2221c5edd387e12e5e7a5391ea1447cb5626c2/pyobjc-framework-AddressBook-10.1.tar.gz")
    version("10.0", sha256="e61dbd593113721ff45bbc706884727dc483502eb4d514fd4c53f56b9a86bef7", url="https://pypi.org/packages/0e/01/73bec168c829304c210ee15fda1ba66f88b0582883e4c3618a4d7d026e6c/pyobjc-framework-AddressBook-10.0.tar.gz")
    version("9.2", sha256="5debb3cf0d083e083fc19dfe03ef184c68751de619e6675d3ae512a200cea0f4", url="https://pypi.org/packages/c9/a5/006f2d38509711edd92ed14651b41c95fa2ccb0d5f20286bbd96af335f48/pyobjc-framework-AddressBook-9.2.tar.gz")
    version("9.1.1", sha256="8849edfe591dca4e6bfe45abcb7c451f2ee2ba4ecb8adc2f35d4e5bd14d66247", url="https://pypi.org/packages/42/d3/91afca5c1e7db2a867414298c479b72398c94600fd86262c5da13c9cc136/pyobjc-framework-AddressBook-9.1.1.tar.gz")
    version("9.1", sha256="326b45084675fa7d72d5ce52f15e03f9b34eba113b0f633f62376a1d5c1eb141", url="https://pypi.org/packages/b2/cf/c61be0afb4c4c62dcf7ea6fa152ed7aa87af90132c93d1c7f4f48f74dd58/pyobjc-framework-AddressBook-9.1.tar.gz")
    version("9.0.1", sha256="1f2f2426122d69a9a981b8c3d9f408d9d9440a47e31a31f725c09997c7698ff9", url="https://pypi.org/packages/96/9e/b93644b1675712adadfebb69f4354957576675ea94238143c0fdd9897553/pyobjc-framework-AddressBook-9.0.1.tar.gz")
    version("9.0", sha256="77392568e2e21877642b8fb84987190359378f5507108433117efd588d6ff91a", url="https://pypi.org/packages/3e/ca/134c4dae5a2d9af0ca618bda8454615380bfbfcf467509d9fc393f669c1f/pyobjc-framework-AddressBook-9.0.tar.gz")
    version("8.5.1", sha256="adee5caf53e3ad71f20113096966bf76c956f66dde6089a8562de7d218d2f496", url="https://pypi.org/packages/c1/8f/15939dc0c97ab7ce4bbc89c949fec5098acde65408df2b54f1d18ebc7c78/pyobjc-framework-AddressBook-8.5.1.tar.gz")
    version("8.5", sha256="d41a8a5b088e7eba6a828477ec221e61de2a75e1769ce060c2713b44d7be439b", url="https://pypi.org/packages/28/15/e37ef6853d9851974592b2a3747db0808e07a916f2be62a4665979a56fd2/pyobjc-framework-AddressBook-8.5.tar.gz")
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

