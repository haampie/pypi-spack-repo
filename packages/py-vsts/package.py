# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyVsts(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.1.25", sha256="c5595a42c9447888ebc91494d2db03c2b867cbca9f1f5f05c113261b92383e35", url="https://pypi.org/packages/9a/4a/c9a5c90659bf0df577067cf8baf9c690501306290e5688d8aeae07fbd9f8/vsts-0.1.25-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-msrest@0.6.0:0.6", when="@0.1.20:")
    # END DEPENDENCIES

