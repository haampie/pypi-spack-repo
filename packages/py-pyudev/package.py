##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyudev(PythonPackage):
    version("0.21.0", sha256="094b7a100150114748aaa3b70663485dd360457a709bfaaafe5a977371033f2b", url="https://pypi.org/packages/bc/a2/31a07829acea8e70a28c247f43fa5d981229ae0f9edfeddedf52de00709b/pyudev-0.21.0.tar.gz")
    version("0.15", sha256="12f462b777388c447edaac9e4b423a38a76eeb43f36b1a42288e771309d663c2", url="https://pypi.org/packages/13/8d/437e226f9c4518a821b141009142d24b11b0fe1acc92d135de95daa9953e/pyudev-0.15.tar.gz")
    version("0.9", sha256="5282ff7178942cfe0cb56316b7743ad6d0189e2749d80f452bf2e04740b81eb2", url="https://pypi.org/packages/90/97/44add096d9401d0b03d6b70898f622d6e7c549398b6e66d66b05b2cadc27/pyudev-0.9.tar.gz")


