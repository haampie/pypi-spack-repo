# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyTypedAst(PythonPackage):
    # BEGIN VERSIONS
    version("1.5.4", sha256="39e21ceb7388e4bb37f4c679d72707ed46c2fbf2a5609b8b8ebc4b067d977df2", url="https://pypi.org/packages/07/d2/d55702e8deba2c80282fea0df53130790d8f398648be589750954c2dcce4/typed_ast-1.5.4.tar.gz")
    version("1.4.3", sha256="fb1bbeac803adea29cedd70781399c99138358c26d05fcbd23c13016b7f5ec65", url="https://pypi.org/packages/6e/08/c04a49ee26a94c1ec211e7b1e5f2971d692e04818ea67ef70f1e879cf525/typed_ast-1.4.3.tar.gz")
    version("1.4.2", sha256="9fc0b3cb5d1720e7141d103cf4819aea239f7d136acf9ee4a69b047b7986175a", url="https://pypi.org/packages/36/8c/efd8ffe7d242cd389632a11cbc6ce596de49b46ece22760a67b742534368/typed_ast-1.4.2.tar.gz")
    version("1.4.1", sha256="8c8aaad94455178e3187ab22c8b01a3837f8ee50e09cf31f1ba129eb293ec30b", url="https://pypi.org/packages/18/09/b6a6b14bb8c5ec4a24fe0cf0160aa0b784fd55a6fd7f8da602197c5c461e/typed_ast-1.4.1.tar.gz")
    version("1.4.0", sha256="66480f95b8167c9c5c5c87f32cf437d585937970f3fc24386f313a4c97b44e34", url="https://pypi.org/packages/34/de/d0cfe2ea7ddfd8b2b8374ed2e04eeb08b6ee6e1e84081d151341bba596e5/typed_ast-1.4.0.tar.gz")
    version("1.3.5", sha256="5315f4509c1476718a4825f45a203b82d7fdf2a6f5f0c8f166435975b1c9f7d4", url="https://pypi.org/packages/d3/b1/959c3ed4a9cc100feba7ad1a7d6336d8888937ee89f4a577f7698e09decd/typed-ast-1.3.5.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    variant("wheel", default=False, description="wheel")
    # END VARIANTS

    # BEGIN DEPENDENCIES
    # END DEPENDENCIES

