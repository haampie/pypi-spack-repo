##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyNetket(PythonPackage):
    version("2.1.1", sha256="4cc7fec26cd95297fa1a85355e19701ed0450649662742c7a4d09bdfef8b0b09", url="https://pypi.org/packages/45/a8/3b5dbeffa787442dee6f4026ff76ecb8aeb936b8725a94fef63eea2071d3/netket-2.1.1.tar.gz")
    version("2.1", sha256="d908b6b09ba94d77ffde377f8c2c73a0aae00657094df5fd0bd30058b1a4e71d", url="https://pypi.org/packages/d4/22/8c03543a8debcb0a626b0ca8324a8b45a039199b7b46d5a9bb841446179f/netket-2.1.tar.gz")
    version("2.0", sha256="49145701341d21b2dc5b96d474c5888274405f42cd8d0fc259d18be8c262a50e", url="https://pypi.org/packages/70/32/1c5e3ef004f4f89b72a32ead3148fd56a0cbad43aafe72e1c6a9d8faafd4/netket-2.0.tar.gz")

    with default_args(type="run"):
        depends_on("python@3.9:", when="@3.10:")

