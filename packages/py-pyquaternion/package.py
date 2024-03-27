##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyquaternion(PythonPackage):
    version("0.9.5", sha256="2d89d19259d62a8fbd25219eee7dacc1f6bb570becb70e1e883f622597c7d81d", url="https://pypi.org/packages/ae/c8/02b30c4a86744d2e15f7f16ab353f7231bd0241117713e5d60f466044994/pyquaternion-0.9.5.tar.gz")

    with default_args(type="run"):
        depends_on("py-numpy", when="@0.9.5")

