# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyMultiurl(PythonPackage):
    # BEGIN VERSIONS
    version("0.2.3.2", sha256="b625892ef3a5b8d4bd323f1dcd4750b6ea7e4e2e2e4574b6e88cdf92e10579e9", url="https://pypi.org/packages/12/6e/269c394f385931b9808d464cac1aaba28bf1a2d59993909ac65fdb431acf/multiurl-0.2.3.2.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-python-dateutil", when="@0.2.3:")
        depends_on("py-pytz", when="@0.2.3:")
        depends_on("py-requests", when="@0.2.3:")
        depends_on("py-tqdm", when="@0.2.3:")
    # END DEPENDENCIES

