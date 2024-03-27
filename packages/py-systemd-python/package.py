##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PySystemdPython(PythonPackage):
    version("235", sha256="4e57f39797fd5d9e2d22b8806a252d7c0106c936039d1e71c8c6b8008e695c0a", url="https://pypi.org/packages/10/9e/ab4458e00367223bda2dd7ccf0849a72235ee3e29b36dce732685d9b7ad9/systemd-python-235.tar.gz")
    version("234", sha256="fd0e44bf70eadae45aadc292cb0a7eb5b0b6372cd1b391228047d33895db83e7", url="https://pypi.org/packages/e8/a8/00ba0f605837a8f69523e6c3a4fb14675a6430c163f836540129c50b3aef/systemd-python-234.tar.gz")


