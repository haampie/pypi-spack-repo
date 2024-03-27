##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyBackportsWeakref(PythonPackage):
    version("1.0.post1", sha256="81bc9b51c0abc58edc76aefbbc68c62a787918ffe943a37947e162c3f8e19e82", url="https://pypi.org/packages/88/ec/f598b633c3d5ffe267aaada57d961c94fdfa183c5c3ebda2b6d151943db6/backports.weakref-1.0.post1-py2.py3-none-any.whl")
    version("1.0-rc1", sha256="8813bf712a66b3d8b85dc289e1104ed220f1878cf981e2fe756dfaabe9a82892", url="https://pypi.org/packages/bc/cc/3cdb0a02e7e96f6c70bd971bc8a90b8463fda83e264fa9c5c1c98ceabd81/backports.weakref-1.0rc1.tar.gz")


