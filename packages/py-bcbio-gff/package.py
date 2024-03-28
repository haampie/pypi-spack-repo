# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyBcbioGff(PythonPackage):
    # BEGIN VERSIONS
    version("0.7.0", sha256="9f1bc9629ef1be13e713971c208223e1812ba1a6119979e9ce80b25212120d65", url="https://pypi.org/packages/65/ca/a662629e1b030af679d228aed5c813f0a8ceedec69f30885f1ec5571ea8a/bcbio_gff-0.7.0-py3-none-any.whl")
    version("0.6.2", sha256="c682dc46a90e9fdb124ab5723797a5f71b2e3534542ceff9f6572b64b9814e68", url="https://pypi.org/packages/d2/02/722db105394093e107c6d4aeb7b8526909a2580b984e9b4f90202e9db1ab/bcbio-gff-0.6.2.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-biopython", when="@0.7:")
        depends_on("py-six", when="@0.7:")
    # END DEPENDENCIES

