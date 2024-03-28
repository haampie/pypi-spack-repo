# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPacificaUploader(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.3.1", sha256="ed473819bdcd3d667a5eacfa10cc38112b929aadb0f89625b75b8374857ec3d9", url="https://pypi.org/packages/b1/89/28e3cb1889444c1026e3bfb6548395b8eea15003d7e45b11e0601dac0ad8/pacifica_uploader-0.3.1-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-requests")
    # END DEPENDENCIES

