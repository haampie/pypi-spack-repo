# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPymongo(PythonPackage):
    # BEGIN VERSIONS
    version("4.2.0", sha256="72f338f6aabd37d343bd9d1fdd3de921104d395766bcc5cdc4039e4c2dd97766", url="https://pypi.org/packages/16/5c/def5ee5112e834ce41a86feb37d076b586e51f5ff7acce072073fc616147/pymongo-4.2.0.tar.gz")
    version("3.12.1", sha256="704879b6a54c45ad76cea7c6789c1ae7185050acea7afd15b58318fa1932ed45", url="https://pypi.org/packages/5f/95/de771196bfc9449097e2d03aedc117d0f7a67a93be7e69b34d7b5e3e9bb0/pymongo-3.12.1.tar.gz")
    version("3.9.0", sha256="4249c6ba45587b959292a727532826c5032d59171f923f7f823788f413c2a5a3", url="https://pypi.org/packages/c0/69/9388b715d013444ae8e5d497a6825d120f6a7a67ef5aa8ddea62f601cbff/pymongo-3.9.0.tar.gz")
    version("3.6.0", sha256="c6de26d1e171cdc449745b82f1addbc873d105b8e7335097da991c0fc664a4a8", url="https://pypi.org/packages/69/8a/2384c55f4bd494eeb6104a9b35c36714ba1178dcd08ee5a73b92eed3d8c1/pymongo-3.6.0.tar.gz")
    version("3.3.0", sha256="3d45302fc2622fabf34356ba274c69df41285bac71bbd229f1587283b851b91e", url="https://pypi.org/packages/31/63/5a7826bdee88db6d49ef1737a17de63cf6f50f8cb04f2a0339f048cb33b5/pymongo-3.3.0.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    # END DEPENDENCIES

