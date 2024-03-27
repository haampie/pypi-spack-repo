##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyMplhepData(PythonPackage):
    version("0.0.3", sha256="a1eba7727fab31902e6fcd113c8f4b12ff3fb0666781e7514f8b79093cdc1c65", url="https://pypi.org/packages/b9/f2/97faf68c79fc135061190092e8e6db9a024de4249a7e82acc83d9443db2b/mplhep_data-0.0.3-py3-none-any.whl")
    version("0.0.2", sha256="ee75933a92d9c5ead57692aa102f4f43f12cd15f429bc5d50798a6c9690f7672", url="https://pypi.org/packages/bd/61/83bdeb0a0a32b9b7234d0472c23a6d8172df085390d59219bb24d842d8f8/mplhep_data-0.0.2-py3-none-any.whl")
    version("0.0.1", sha256="5cdceea559beede523c7ac25544e96f158533d5b10b4273be8c4c93668f9f46b", url="https://pypi.org/packages/76/f4/aaf2a74c65dc3d659d7a9e59aee8481908e78c20648f906501f4a6b4011c/mplhep_data-0.0.1-py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-numpy@1.13.3:", when="@:0.0.1")

