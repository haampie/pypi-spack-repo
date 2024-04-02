# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPylibmagic(PythonPackage):
    # BEGIN VERSIONS
    version("0.2.2", sha256="17551b5259db4045c63e595577d42df172e35147e26160a47f4a5ba3933281e7", url="https://pypi.org/packages/54/b6/d732dccb2d98c3d78f4112b8b1bd55115ed163d6a3532b227ecb2b143d5a/pylibmagic-0.2.2.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.7:")
    # END DEPENDENCIES

