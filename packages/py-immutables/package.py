# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyImmutables(PythonPackage):
    # BEGIN VERSIONS
    version("0.20", sha256="1d2f83e6a6a8455466cd97b9a90e2b4f7864648616dfa6b19d18f49badac3876", url="https://pypi.org/packages/7d/63/27f038a28ff2110bc04908a047817fd316d5a16ae06d0d3707732dee8013/immutables-0.20.tar.gz")
    version("0.19", sha256="df17942d60e8080835fcc5245aa6928ef4c1ed567570ec019185798195048dcf", url="https://pypi.org/packages/c3/bf/113933c9d098c58cee52c68a205cd449bcc331c32156267d337125780bf6/immutables-0.19.tar.gz")
    version("0.18", sha256="5336c7974084cce62f7e29aaff81a3c3f75e0fd0a23a2faeb986ae0ea08d8cf4", url="https://pypi.org/packages/65/f7/6d863110a1e4c6d115efa900dcab8b51b9bcc3cb654a3e7a393ad2d178a1/immutables-0.18.tar.gz")
    version("0.16", sha256="d67e86859598eed0d926562da33325dac7767b7b1eff84e232c22abea19f4360", url="https://pypi.org/packages/45/e5/743bc53f6ff11de2eb1dc29eef92693a51ded22039affb7316391dad67f5/immutables-0.16.tar.gz")
    version("0.14", sha256="a0a1cc238b678455145bae291d8426f732f5255537ed6a5b7645949704c70a78", url="https://pypi.org/packages/6b/58/c6be0577cccbe1658fcb1ec3673e9ac7508af26a2f5c814cc041c7d21212/immutables-0.14.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.8:", when="@0.20:")
    # END DEPENDENCIES

