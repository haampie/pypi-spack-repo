# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyGhpImport(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("2.1.0", sha256="8337dd7b50877f163d4c0289bc1f1c7f127550241988d568c1db512c4324a619", url="https://pypi.org/packages/f7/ec/67fbef5d497f86283db54c22eec6f6140243aae73265799baaaa19cd17fb/ghp_import-2.1.0-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-python-dateutil@2.8.1:", when="@2.0.1:")
    # END DEPENDENCIES

