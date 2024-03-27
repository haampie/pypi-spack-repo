##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyBoostHistogram(PythonPackage):
    version("1.4.0", sha256="cf9826cfcfe10335096b57a61f6c6569f65f0159259eeb2251c5bf31d859d753", url="https://pypi.org/packages/dd/9c/028fab7b6082e18c5f25ffb45a8536021bddc825ad2f778c1c4bdcd39cc6/boost_histogram-1.4.0.tar.gz")
    version("1.3.2", sha256="e175efbc1054a27bc53fbbe95472cac9ea93999c91d0611840d776b99588d51a", url="https://pypi.org/packages/de/1a/e55f7c104168e2c28ce52a3a68b06d8e26c7d3ae66cab87d6b559034e124/boost_histogram-1.3.2.tar.gz")
    version("1.3.1", sha256="31cd396656f3a37834e07d304cdb84d9906bc2172626a3d92fe577d08bcf410f", url="https://pypi.org/packages/fa/2d/79cad54cc2579836d048809e6f29fc294f9b4f7c4eedee6fda4425daaf30/boost_histogram-1.3.1.tar.gz")
    version("1.3.0", sha256="62240dae889cbf05f8b4f2203f0b7d6c7a2e029502723a377fc33226e425ce50", url="https://pypi.org/packages/0a/9a/1ebde600886eee433a99434e0ddb462630a0b25ab1f58efb91ffc385a0ff/boost_histogram-1.3.0.tar.gz")
    version("1.2.1", sha256="a27842b2f1cfecc509382da2b25b03056354696482b38ec3c0220af0fc9b7579", url="https://pypi.org/packages/26/45/6cfc7f8a36aa9537dfbb4e3495180303ce98c3b1307c8bc8dfc3548e0507/boost_histogram-1.2.1.tar.gz")
    version("1.2.0", sha256="004ccfae0450012f35c8e815c8011a50e6e772652f52515cb5fee7b1c8cfb47c", url="https://pypi.org/packages/c4/c8/f663185fddbaf814cedc4da676ca54c1cd5e08f1ee5b67cd3e53c89494d5/boost_histogram-1.2.0.tar.gz")
    version("1.1.0", sha256="370e8e44a0bac4ebbedb7e62570be3a75a7a3807a297d6e82a94301b4681fc22", url="https://pypi.org/packages/88/fc/c1c61d704089bae0a6d29edcf785406eaa279032a0a343a4b9070e9f075a/boost_histogram-1.1.0.tar.gz")
    version("1.0.2", sha256="b79cb9a00c5b8e44ff24ffcbec0ce5d3048dd1570c8592066344b6d2f2369fa2", url="https://pypi.org/packages/91/72/1d6b6404f2e325b62b7a8e0a6e7e53041ff093ed08ba0e593935a17119da/boost_histogram-1.0.2.tar.gz")
    version("1.0.1", sha256="142d82ce0dfc97a98ccd6f498f91b45de33249c143c7263d690d78227ea1c77a", url="https://pypi.org/packages/07/07/4a58094ee42ee9a4982b414a83d261ba3046a05cf37c4976927f7699f51e/boost_histogram-1.0.1.tar.gz")
    version("1.0.0", sha256="88f2a58a77d273e9e09783036f23bb39ba2fcfc7e13d14639151245eb90ec0b2", url="https://pypi.org/packages/63/8f/8d782f7b5d167c6bb2d3a6fc20a92a82210dc6b8fe46a54831292c9d9441/boost_histogram-1.0.0.tar.gz")

    with default_args(type="run"):
        depends_on("py-numpy@1.26:", when="@1.4: ^python@3.12:")
        depends_on("py-numpy", when="@1.4: ^python@:3.11")
        depends_on("py-numpy", when="@0.5:0.10.0")

