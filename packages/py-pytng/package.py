##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPytng(PythonPackage):
    version("0.3.0", sha256="f563f9ea260ca8c8e17b3bcf9458bae35aedd5c58e1c5ac4dfff77a1e036506e", url="https://pypi.org/packages/2e/ae/d9b5e5d9b48c6509d9ea5013a9f9d4618fca3b1ec7c4f8cfa0477b370c54/pytng-0.3.0.tar.gz")

    with default_args(type="run"):
        depends_on("python@3.9:", when="@0.3.1:")

