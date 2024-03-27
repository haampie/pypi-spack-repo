##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyCmake(PythonPackage):
    version("3.27.9", sha256="f564e739b0ef37c1422fe91938b2ab971e21756b848bf840e3672ef3acacf73f", url="https://pypi.org/packages/b5/a9/e27e499fa7280a110976560ac7bf65289d60107a13f75538e9d9f57d8540/cmake-3.27.9-py2.py3-none-win_arm64.whl")
    version("3.22.2", sha256="9f5f563e89a3ee8873a4c48c69d8a32331749da3c3b657d0f0ac74b659e87954", url="https://pypi.org/packages/8f/2a/db8ca9077c97d9db6269f4feaea35679b0c1cc944a6bbfa913b5749f1cfb/cmake-3.22.2-py2.py3-none-win_amd64.whl")
    version("3.21.4", sha256="d7bbf5e3f7bedcb8ab7478c383739098af11170edad204659e6191ff95b960f4", url="https://pypi.org/packages/ab/d9/8975d2a731abb5530c4c030a74dfd01bd73150399df4e421242909883757/cmake-3.21.4-py2.py3-none-win_amd64.whl")
    version("3.18.0", sha256="52b98c5ee70b5fa30a8623e96482227e065292f78794eb085fdf0fecb204b79b", url="https://pypi.org/packages/bf/b6/bc83a846ac9ffbcb7f9490af135c42002e12f3adc8253c9e55c07de49cf3/cmake-3.18.0.tar.gz")


