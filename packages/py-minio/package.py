# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyMinio(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("7.1.2", sha256="51318733496f37617bebfefe116453406a0d5afc6add8c421df07f32e0843c2b", url="https://pypi.org/packages/78/16/a252d8cb3c3178480820a005426b67cb7a94efbdb18962b7af1e4c67ee6d/minio-7.1.2-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-certifi")
        depends_on("py-urllib3", when="@:7.2.1,7.2.3:")
    # END DEPENDENCIES

