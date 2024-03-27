##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyBackportsTempfile(PythonPackage):
    version("1.0", sha256="05aa50940946f05759696156a8c39be118169a0e0f94a49d0bb106503891ff54", url="https://pypi.org/packages/b4/5c/077f910632476281428fe254807952eb47ca78e720d059a46178c541e669/backports.tempfile-1.0-py2.py3-none-any.whl")
    version("1.0-rc1", sha256="1492e2fd8e8abcae6a9c9e78edc52aae4234937c5d462fd3ce0e29c1a4687d3b", url="https://pypi.org/packages/d6/68/49955c14c22b73e5a0eb2e08d431f031e7ce226b2d29894f891bade22e82/backports.tempfile-1.0rc1.tar.gz")


