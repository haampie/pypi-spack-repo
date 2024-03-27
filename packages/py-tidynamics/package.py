##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyTidynamics(PythonPackage):
    version("1.1.2", sha256="3edd862271ef136e35129b303153e790914b66644b2641c92a72a7878a16a858", url="https://pypi.org/packages/df/75/ec8466118646fa6523d7703c2deba7c6f7bba3f2bae383234662e76fd73e/tidynamics-1.1.2-py3-none-any.whl")
    version("1.0.0", sha256="2f0fb8e9b813c01062d950a1eacf99ce23d49161d9a49f26628e4e0afdf566d1", url="https://pypi.org/packages/22/55/b4c455c67b85694ffdcd91ad81067b69c436fada21f78b228c079278362e/tidynamics-1.0.0-py2.py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-numpy", when="@0.1.2:")

