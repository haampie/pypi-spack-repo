# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyLightgbm(PythonPackage):
    # BEGIN VERSIONS
    version("3.1.1", sha256="babece2e3613e97748a67ed45387bb0e984bdb1f4126e39f010fbfe7503c7b20", url="https://pypi.org/packages/cf/65/368931f1f234149e14fc6075dbeb1ad8a8aebb105aa11fe8631c72c1bdcf/lightgbm-3.1.1.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    variant("mpi", default=False)
    # END VARIANTS

    # BEGIN DEPENDENCIES
    # END DEPENDENCIES

