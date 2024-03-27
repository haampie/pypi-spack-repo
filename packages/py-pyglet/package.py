##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyglet(PythonPackage):
    version("2.0.10", sha256="e10a1f1a6a2dcfbf23155913746ff6fbf8ea18c5ee813b6d0e79d273bb2b3c18", url="https://pypi.org/packages/e9/33/cbff7525a357c950e76717ea9741127a662a7ed49a92874897b8a4036db9/pyglet-2.0.10-py3-none-any.whl")
    version("2.0.9", sha256="8520b22dde75f47167e1fedeed58ac0bb0c890c0dca17d8528427d6b318cd9cc", url="https://pypi.org/packages/94/a1/475458ccf34d2996abdb6ef29fa8d3fed2e62f72df5f2a7f4b4b076915c7/pyglet-2.0.9-py3-none-any.whl")
    version("1.4.2", sha256="c1c49b2c384bc310aa3dca87817d2b4d22383e35776e73dace5a38235f0992a4", url="https://pypi.org/packages/d4/eb/e3742cc05eb640b6b59618ad8c8ae38f43aa57539e4cd1b40576c93afccb/pyglet-1.4.2-py2.py3-none-any.whl")
    version("1.2.1", sha256="41edc43fd41890e772b2f09f3878ebd5d41566c14d2bf7e9732e47ce97f1db78", url="https://pypi.org/packages/8e/de/ab8e0957e61c98c23adb920317e7dd7a5269f18fd336c99ab317760a3e39/pyglet-1.2.1.zip")

    with default_args(type="run"):
        depends_on("py-future", when="@1.3:1.5.0")

