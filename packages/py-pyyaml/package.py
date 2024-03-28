# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyyaml(PythonPackage):
    # BEGIN VERSIONS
    version("6.0", sha256="68fb519c14306fec9720a2a5b45bc9f0c8d1b9c72adf45c37baedfcd949c35a2", url="https://pypi.org/packages/36/2b/61d51a2c4f25ef062ae3f74576b01638bebad5e045f747ff12643df63844/PyYAML-6.0.tar.gz")
    version("5.4.1", sha256="607774cbba28732bfa802b54baa7484215f530991055bb562efbed5b2f20a45e", url="https://pypi.org/packages/a0/a4/d63f2d7597e1a4b55aa3b4d6c5b029991d3b824b5bd331af8d4ab1ed687d/PyYAML-5.4.1.tar.gz")
    version("5.3.1", sha256="b8eac752c5e14d3eca0e6dd9199cd627518cb5ec06add0de9d32baeee6fe645d", url="https://pypi.org/packages/64/c2/b80047c7ac2478f9501676c988a5411ed5572f35d1beff9cae07d321512c/PyYAML-5.3.1.tar.gz")
    version("5.2", sha256="c0ee8eca2c582d29c3c2ec6e2c4f703d1b7f1fb10bc72317355a746057e7346c", url="https://pypi.org/packages/8d/c9/e5be955a117a1ac548cdd31e37e8fd7b02ce987f9655f5c7563c656d5dcb/PyYAML-5.2.tar.gz")
    version("5.1.2", sha256="01adf0b6c6f61bd11af6e10ca52b7d4057dd0be0343eb9283c878cf3af56aee4", url="https://pypi.org/packages/e3/e8/b3212641ee2718d556df0f23f78de8303f068fe29cdaa7a91018849582fe/PyYAML-5.1.2.tar.gz")
    version("5.1", sha256="436bc774ecf7c103814098159fbb84c2715d25980175292c648f2da143909f95", url="https://pypi.org/packages/9f/2c/9417b5c774792634834e730932745bc09a7d36754ca00acf1ccd1ac2594d/PyYAML-5.1.tar.gz")
    version("3.13", sha256="3ef3092145e9b70e3ddd2c7ad59bdd0252a94dfe3949721633e41344de00a6bf", url="https://pypi.org/packages/9e/a3/1d13970c3f36777c583f136c136f804d70f500168edc1edea6daa7200769/PyYAML-3.13.tar.gz")
    version("3.12", sha256="5ac82e411044fb129bae5cfbeb3ba626acb2af31a8d17d175004b70862a741a7", url="https://pypi.org/packages/6b/f0/a0250248ea260d55748fff586d89a32afbb22656f4498b08d2636a48d4ec/PyYAML-3.12.zip")
    version("3.11", sha256="19bb3ac350ef878dda84a62d37c7d5c17a137386dde9c2ce7249c7a21d7f6ac9", url="https://pypi.org/packages/04/60/abfb3a665ee0569b60c89148b7187ddd8a36cb65e254fba945ae1315645d/PyYAML-3.11.zip")
    # END VERSIONS

    # BEGIN VARIANTS
    variant("libyaml", default=False)
    # END VARIANTS

    # BEGIN DEPENDENCIES
    # END DEPENDENCIES

