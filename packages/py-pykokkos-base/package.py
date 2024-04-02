# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPykokkosBase(PythonPackage):
    # BEGIN VERSIONS
    version("0.0.5", sha256="c2c8870398cff10193383bb0733b1b6a2b67c4ef33241ba8de795299136a22da", url="https://pypi.org/packages/8c/0d/bc2bbb5449c1d5ceed7f6ccbd61b03e873e738c2d6dca257e1cbb6092e0c/pykokkos-base-0.0.5.tar.gz")
    version("0.0.4", sha256="068bb1e416f44011e51adf1d82e9f3aab299bc9757f5b244b37c095f0a383429", url="https://pypi.org/packages/22/37/79ab31748ed14191ed63d747f672003bdab0e298f3fd6d26b96278422fbb/pykokkos-base-0.0.4.tar.gz")
    version("0.0.3", sha256="082d8c05cd4493fd45359170cde076431c88fced6ba4c6d737cb4cdfda4c81fe", url="https://pypi.org/packages/ef/47/18cf8abf1f7d9a2ba4ef73c86a75db994837be0ea0d2189227299d776bcc/pykokkos-base-0.0.3.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    variant("build_type", default=False, description="build_type")
    variant("generator", default=False, description="generator")
    variant("ipo", default=False, description="ipo")
    variant("layouts", default=False, description="layouts")
    variant("memory_traits", default=False, description="memory_traits")
    variant("view_ranks", default=False, description="view_ranks")
    # END VARIANTS

    # BEGIN DEPENDENCIES
    # END DEPENDENCIES

