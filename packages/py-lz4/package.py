# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyLz4(PythonPackage):
    # BEGIN VERSIONS
    version("4.3.3", sha256="01fe674ef2889dbb9899d8a67361e0c4a2c833af5aeb37dd505727cf5d2a131e", url="https://pypi.org/packages/a4/31/ec1259ca8ad11568abaf090a7da719616ca96b60d097ccc5799cd0ff599c/lz4-4.3.3.tar.gz")
    version("4.0.2", sha256="083b7172c2938412ae37c3a090250bfdd9e4a6e855442594f86c3608ed12729b", url="https://pypi.org/packages/65/8d/4d913798e17735839c7666e81985bd230f739927d066890b511a78c542d8/lz4-4.0.2.tar.gz")
    version("3.1.3", sha256="081ef0a3b5941cb03127f314229a1c78bd70c9c220bb3f4dd80033e707feaa18", url="https://pypi.org/packages/d9/c5/080234f5b6b698f56339edf7715d9256eca4eb3d35b36893227c399e69f9/lz4-3.1.3.tar.gz")
    version("3.1.0", sha256="debe75513db3eb9e5cdcd82a329ff38374b6316ab65b848b571e0404746c1e05", url="https://pypi.org/packages/4c/c3/97c5aaeb8c70eafb0cba7dcbcb7709c2697d8a92bdef90d36b018dc502f6/lz4-3.1.0.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.8:", when="@4.3.3:")
        depends_on("python@3.7:", when="@4:4.3.2")
    # END DEPENDENCIES

