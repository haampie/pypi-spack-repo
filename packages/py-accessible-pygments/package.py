##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyAccessiblePygments(PythonPackage):
    version("0.0.4", sha256="416c6d8c1ea1c5ad8701903a20fcedf953c6e720d64f33dc47bfb2d3f2fa4e8d", url="https://pypi.org/packages/20/d7/45cfa326d945e411c7e02764206845b05f8f5766aa7ebc812ef3bc4138cd/accessible_pygments-0.0.4-py2.py3-none-any.whl")
    version("0.0.3", sha256="6a643a2979b1f14fead79a8bbf51a6ae09e9df70d5ed60bb61a6eb9092cdcb81", url="https://pypi.org/packages/b3/12/8b34b4ecf56bd4d30b100c0eed43ebe30394eeb063998a9b739dc8d46281/accessible_pygments-0.0.3-py2.py3-none-any.whl")
    version("0.0.2", sha256="30b6b4bd0c1b7ee49c85b4b01a62c88df7957436783d8b46ae782dafdc627d8b", url="https://pypi.org/packages/87/57/75d37069faa4bcfb0b2d4fc768b84bb2fb2234c64dc9518e1b7ecafe683f/accessible_pygments-0.0.2-py2.py3-none-any.whl")
    version("0.0.1", sha256="777d288d094d61ce18fdfc1e299615d29ad7760ebd9f4d76557fcac0c4f5c3a6", url="https://pypi.org/packages/a4/00/536a9d9ad7930a582e7320ad80b6ea7179d63d2e42c6e23abccde9b4a1ca/accessible_pygments-0.0.1-py2.py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-pygments@1.5:")

