##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyUproot3Methods(PythonPackage):
    version("0.10.1", sha256="10e4be8dbcabdf3efb5cce185b0b8ede2ed8390e875750649c6f1c277c26d28c", url="https://pypi.org/packages/3f/57/598207abeb64bf3e0af3fdc19217e56936b6bebabaac6ee270fb151790ce/uproot3_methods-0.10.1-py3-none-any.whl")
    version("0.10.0", sha256="d7db997f218984cb8e9fb8e9e7823a04265f9fdbf86bcf4b9f0cf82e383ad6fe", url="https://pypi.org/packages/b7/bc/0cc6e815361218923dc27e8f511036d6d96ab366ea25994a89ac9ac9ba6f/uproot3_methods-0.10.0-py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-awkward0")
        depends_on("py-numpy@1.13.1:")

