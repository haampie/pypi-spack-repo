# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPacificaDownloader(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.4.1", sha256="edbf3d06e2188c65a5108ae1c71546e10747197b661389c27c4768a1eb771fbc", url="https://pypi.org/packages/b9/8c/b747dc45acf69fdb093ffe9a21572741bd974e1dfab56289d8f7a1dfb3f7/pacifica_downloader-0.4.1-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-requests", when="@0.4.1:")
    # END DEPENDENCIES

