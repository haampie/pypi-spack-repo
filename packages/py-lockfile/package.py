# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyLockfile(PythonPackage):
    # BEGIN VERSIONS
    version("0.12.2", sha256="6c3cb24f344923d30b2785d5ad75182c8ea7ac1b6171b08657258ec7429d50fa", url="https://pypi.org/packages/c8/22/9460e311f340cb62d26a38c419b1381b8593b0bb6b5d1f056938b086d362/lockfile-0.12.2-py2.py3-none-any.whl")
    version("0.11.0", sha256="6591deec873a9ccccc5aeb35a1146e065cc6cd0fdaf0786da8b7b84c31d41455", url="https://pypi.org/packages/73/83/9474c4a257b75b9a08aacd7de0a30ad97d9cdaeb1cbf48efa46bcb1969ea/lockfile-0.11.0-py2-none-any.whl")
    version("0.10.2", sha256="81ee2d4b0923a2ee3e51b93af0db82efa3f049c7435a00549f9a3ba22cf70cbf", url="https://pypi.org/packages/14/00/cf7b269d28ba8919b64a2139f65c4ecc853dec61992cd542c202ed91a9e6/lockfile-0.10.2-py2-none-any.whl")
    version("0.9.1", sha256="23da589c91f59cb7c644d5ce5df539d448341bd479917d6dde973f82e2719147", url="https://pypi.org/packages/fb/89/af965281e233d8722002a4b7b7b0b650d46875d03faa7e83a1463d6789e1/lockfile-0.9.1.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-pbr@0.6,0.8:0", when="@0.11")
    # END DEPENDENCIES

