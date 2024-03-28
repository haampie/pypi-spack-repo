# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPydotplus(PythonPackage):
    # BEGIN VERSIONS
    version("2.0.2", sha256="91e85e9ee9b85d2391ead7d635e3d9c7f5f44fd60a60e59b13e2403fa66505c4", url="https://pypi.org/packages/60/bf/62567830b700d9f6930e9ab6831d6ba256f7b0b730acb37278b0ccdffacf/pydotplus-2.0.2.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    variant("docs", default=False)
    # END VARIANTS

    # BEGIN DEPENDENCIES
    # END DEPENDENCIES

