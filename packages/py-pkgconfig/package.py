# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPkgconfig(PythonPackage):
    # BEGIN VERSIONS
    version("1.5.5", sha256="d20023bbeb42ee6d428a0fac6e0904631f545985a10cdd71a20aa58bc47a4209", url="https://pypi.org/packages/32/af/89487c7bbf433f4079044f3dc32f9a9f887597fe04614a37a292e373e16b/pkgconfig-1.5.5-py3-none-any.whl")
    version("1.5.1", sha256="cddf2d7ecadb272178a942eb852a9dee46bda2adcc36c3416b0fef47a4ed9f38", url="https://pypi.org/packages/b4/2c/bf434cb5a6590417e1d4468050ec317ea17fd6231c2a256df4646c11e588/pkgconfig-1.5.1-py2.py3-none-any.whl")
    version("1.4.0", sha256="3eb03a6345d4916489d3433f60e6d044a21f50e1d86fb611a52fd28061582065", url="https://pypi.org/packages/e1/8a/c205fad800317a59e8d218981a8a7a3a00ec69c7fd55eca58dd08e6b0a18/pkgconfig-1.4.0-py2.py3-none-any.whl")
    version("1.2.2", sha256="3685ba02a9b72654a764b728b559f327e1dbd7dc6ebc310a1bd429666ee202aa", url="https://pypi.org/packages/9d/ba/80910bbed2b4e646a6adab4474d2e506744c260c7002a0e6b41ef8750d8d/pkgconfig-1.2.2.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@:3", when="@1.5.3:")
    # END DEPENDENCIES

