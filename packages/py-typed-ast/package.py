# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyTypedAst(PythonPackage):
    # BEGIN VERSIONS
    version("1.5.5", sha256="94282f7a354f36ef5dbce0ef3467ebf6a258e370ab33d5b40c249fa996e590dd", url="https://pypi.org/packages/f9/7e/a424029f350aa8078b75fd0d360a787a273ca753a678d1104c5fa4f3072a/typed_ast-1.5.5.tar.gz")
    version("1.5.4", sha256="39e21ceb7388e4bb37f4c679d72707ed46c2fbf2a5609b8b8ebc4b067d977df2", url="https://pypi.org/packages/07/d2/d55702e8deba2c80282fea0df53130790d8f398648be589750954c2dcce4/typed_ast-1.5.4.tar.gz")
    version("1.5.3", sha256="27f25232e2dd0edfe1f019d6bfaaf11e86e657d9bdb7b0956db95f560cceb2b3", url="https://pypi.org/packages/cf/b4/c47a1dc4767a9c98f238b6ad7eb873747eaf640f965d5a4b3e5814bc0b72/typed_ast-1.5.3.tar.gz")
    version("1.5.2", sha256="525a2d4088e70a9f75b08b3f87a51acc9cde640e19cc523c7e41aa355564ae27", url="https://pypi.org/packages/4a/9c/f35b20518e633f4df40e9e47eb17b92ec122be52153ac0d6f28419489cf1/typed_ast-1.5.2.tar.gz")
    version("1.5.1", sha256="484137cab8ecf47e137260daa20bafbba5f4e3ec7fda1c1e69ab299b75fa81c5", url="https://pypi.org/packages/39/ea/548f05abe9604a08ae99c64bf75a4061a4eb9b0062162501bfb4fafdf68f/typed_ast-1.5.1.tar.gz")
    version("1.5.0", sha256="ff4ad88271aa7a55f19b6a161ed44e088c393846d954729549e3cde8257747bb", url="https://pypi.org/packages/41/f3/3762315a4cb5db2eb4b7d8d22042fda845591e3c966e084bb988d8d35be9/typed_ast-1.5.0.tar.gz")
    version("1.4.3", sha256="fb1bbeac803adea29cedd70781399c99138358c26d05fcbd23c13016b7f5ec65", url="https://pypi.org/packages/6e/08/c04a49ee26a94c1ec211e7b1e5f2971d692e04818ea67ef70f1e879cf525/typed_ast-1.4.3.tar.gz")
    version("1.4.2", sha256="9fc0b3cb5d1720e7141d103cf4819aea239f7d136acf9ee4a69b047b7986175a", url="https://pypi.org/packages/36/8c/efd8ffe7d242cd389632a11cbc6ce596de49b46ece22760a67b742534368/typed_ast-1.4.2.tar.gz")
    version("1.4.1", sha256="8c8aaad94455178e3187ab22c8b01a3837f8ee50e09cf31f1ba129eb293ec30b", url="https://pypi.org/packages/18/09/b6a6b14bb8c5ec4a24fe0cf0160aa0b784fd55a6fd7f8da602197c5c461e/typed_ast-1.4.1.tar.gz")
    version("1.4.0", sha256="66480f95b8167c9c5c5c87f32cf437d585937970f3fc24386f313a4c97b44e34", url="https://pypi.org/packages/34/de/d0cfe2ea7ddfd8b2b8374ed2e04eeb08b6ee6e1e84081d151341bba596e5/typed_ast-1.4.0.tar.gz")
    version("1.3.5", sha256="5315f4509c1476718a4825f45a203b82d7fdf2a6f5f0c8f166435975b1c9f7d4", url="https://pypi.org/packages/d3/b1/959c3ed4a9cc100feba7ad1a7d6336d8888937ee89f4a577f7698e09decd/typed-ast-1.3.5.tar.gz")
    version("1.3.4", sha256="68c362848d9fb71d3c3e5f43c09974a0ae319144634e7a47db62f0f2a54a7fa7", url="https://pypi.org/packages/a6/4e/ff9d7b7091e2308d2cdb04a1a317e13f293f4408990ee4a52b7028657917/typed-ast-1.3.4.tar.gz")
    version("1.3.2", sha256="244bc007c2da0750e323657da76dab686327939fe4ff77b23ce49a01b0a85da7", url="https://pypi.org/packages/17/87/9a04174f68273388e2eaca66398fe17771d217e27eb6c130b90f8d6e261b/typed-ast-1.3.2.tar.gz")
    version("1.3.1", sha256="606d8afa07eef77280c2bf84335e24390055b478392e1975f96286d99d0cb424", url="https://pypi.org/packages/fc/c6/61d6410fc70fda073bd1810f9b7f7022f00146b108f278a0c00041bfe5b0/typed-ast-1.3.1.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    variant("wheel", default=False)
    # END VARIANTS

    # BEGIN DEPENDENCIES
    # END DEPENDENCIES

