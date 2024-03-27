##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPytorchMsssim(PythonPackage):
    version("1.0.0", sha256="0b4b7bbf7035fe9dc8084244237aac13b1f104852c45b63a7e9fab4363bede54", url="https://pypi.org/packages/e2/8c/856047f955acc30179e9255fdc488059ca22f0938519523d53494f7cfee8/pytorch_msssim-1.0.0-py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-torch")

