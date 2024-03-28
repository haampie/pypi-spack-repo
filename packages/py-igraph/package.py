# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyIgraph(PythonPackage):
    # BEGIN VERSIONS
    version("0.10.6", sha256="76f7aad294514412f835366a7d9a9c1e7a34c3e6ef0a6c3a1a835234323228e8", url="https://pypi.org/packages/75/a9/3351da0a498502707f548ca48b2c4abc9e2f6e1901ad143c8559a95b0985/igraph-0.10.6.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    variant("matplotlib", default=False)
    # END VARIANTS

    # BEGIN DEPENDENCIES
    # END DEPENDENCIES

