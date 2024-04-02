# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PySunpy(PythonPackage):
    # BEGIN VERSIONS
    version("5.1.1", sha256="9367ec9af2a397fcd59638b2007208d4eeaf9ed24e3e8dc2596c26b1896c2e1f", url="https://pypi.org/packages/d9/92/7123c9d3e721f069c493cdebb453aea7db393990e8f735d3aad901ea10b6/sunpy-5.1.1.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.9:", when="@5:")
        depends_on("py-astropy@5.0.6:5.1-rc1,5.1.1:", when="@5.0.1:")
        depends_on("py-numpy@1.21.0:", when="@5.0.1:")
        depends_on("py-packaging@19:", when="@5.0.1:")
        depends_on("py-parfive@2.0.0:+ftp", when="@5.0.1:")
    # END DEPENDENCIES

