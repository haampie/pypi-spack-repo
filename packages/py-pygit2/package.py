# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPygit2(PythonPackage):
    # BEGIN VERSIONS
    version("1.12.1", sha256="8218922abedc88a65d5092308d533ca4c4ed634aec86a3493d3bdf1a25aeeff3", url="https://pypi.org/packages/48/6b/1c20d9adf9906e699bdb505322b27c71e12d7250d8454ae88dcecdf10296/pygit2-1.12.1.tar.gz")
    version("1.11.1", sha256="793f583fd33620f0ac38376db0f57768ef2922b89b459e75b1ac440377eb64ec", url="https://pypi.org/packages/43/9a/f4375f39d2de971750a7c16bd7ab9cc53368f395edaac59b32e9b3f62ce9/pygit2-1.11.1.tar.gz")
    version("1.6.0", sha256="7aacea4e57011777f4774421228e5d0ddb9a6ddb87ac4b542346d17ab12a4d62", url="https://pypi.org/packages/1d/e6/54e1b5001ddca917727ddf84c95028cc724697a040a32d361b7774dba4d4/pygit2-1.6.0.tar.gz")
    version("1.4.0", sha256="cbeb38ab1df9b5d8896548a11e63aae8a064763ab5f1eabe4475e6b8a78ee1c8", url="https://pypi.org/packages/3a/42/f69de8c7a1e33f365a91fa39093f4e7a64609c2bd127203536edc813cbf7/pygit2-1.4.0.tar.gz")
    version("1.3.0", sha256="0be93f6a8d7cbf0cc79ae2f0afb1993fc055fc0018c27e2bd01ba143e51d4452", url="https://pypi.org/packages/20/02/25077cf7ac6599e0e6bd2c6836e7c7360244d2d7224d54e51218dbe00711/pygit2-1.3.0.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.8:", when="@1.11:1.13")
    # END DEPENDENCIES

