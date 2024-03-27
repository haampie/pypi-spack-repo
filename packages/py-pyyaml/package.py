##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyyaml(PythonPackage):
    version("6.0.1", sha256="bfdf460b1736c775f2ba9f6a92bca30bc2095067b8a9d77876d1fad6cc3b4a43", url="https://pypi.org/packages/cd/e5/af35f7ea75cf72f2cd079c95ee16797de7cd71f29ea7c68ae5ce7be1eda0/PyYAML-6.0.1.tar.gz")
    version("6.0", sha256="68fb519c14306fec9720a2a5b45bc9f0c8d1b9c72adf45c37baedfcd949c35a2", url="https://pypi.org/packages/36/2b/61d51a2c4f25ef062ae3f74576b01638bebad5e045f747ff12643df63844/PyYAML-6.0.tar.gz")
    version("6.0-beta1", sha256="40f637ea3333c0969c3f4127393a5f908f40f7e85605f9e6f568cff2c66849ef", url="https://pypi.org/packages/ac/2b/f872e3b78e6b2471c00e559bef89a89715888538dd3fa87528afa669ae08/PyYAML-6.0b1.tar.gz")
    version("5.4.1", sha256="607774cbba28732bfa802b54baa7484215f530991055bb562efbed5b2f20a45e", url="https://pypi.org/packages/a0/a4/d63f2d7597e1a4b55aa3b4d6c5b029991d3b824b5bd331af8d4ab1ed687d/PyYAML-5.4.1.tar.gz")
    version("5.4", sha256="3c49e39ac034fd64fd576d63bb4db53cda89b362768a67f07749d55f128ac18a", url="https://pypi.org/packages/b5/fd/15638de2da0a5aa91c095718444624aa565f766fc178249ca6faa372f71a/PyYAML-5.4.tar.gz")
    version("5.4-beta2", sha256="fa995979ff3037b5989812f320fc7f84564f43a1e23b6348ab343c576fe2409d", url="https://pypi.org/packages/38/81/586bed445a69c8368fad395f0ea73b604a5269bbdc2b5202b5d83b844365/PyYAML-5.4b2.tar.gz")
    version("5.4-beta1", sha256="1dd4545a58abb94b9b623d7658109d2cb66dc09f3389025defc1ca17b9557884", url="https://pypi.org/packages/70/1b/9546dfbd01b4cb017aa54676e66e6f5c62d5a50d20f9140d3bb9fe0e7dc5/PyYAML-5.4b1.tar.gz")
    version("5.3.1", sha256="b8eac752c5e14d3eca0e6dd9199cd627518cb5ec06add0de9d32baeee6fe645d", url="https://pypi.org/packages/64/c2/b80047c7ac2478f9501676c988a5411ed5572f35d1beff9cae07d321512c/PyYAML-5.3.1.tar.gz")
    version("5.3", sha256="e9f45bd5b92c7974e59bcd2dcc8631a6b6cc380a904725fce7bc08872e691615", url="https://pypi.org/packages/3d/d9/ea9816aea31beeadccd03f1f8b625ecf8f645bd66744484d162d84803ce5/PyYAML-5.3.tar.gz")
    version("5.3-beta1", sha256="74ad685bfb065f4bdd36d24aa97092f04bcbb1179b5ffdd3d5f994023fb8c292", url="https://pypi.org/packages/a0/18/842b84b53383d64bffa8e3aa45eaebd8842131d8439fecc82b6d969cda7b/PyYAML-5.3b1.tar.gz")
    version("5.2", sha256="c0ee8eca2c582d29c3c2ec6e2c4f703d1b7f1fb10bc72317355a746057e7346c", url="https://pypi.org/packages/8d/c9/e5be955a117a1ac548cdd31e37e8fd7b02ce987f9655f5c7563c656d5dcb/PyYAML-5.2.tar.gz")
    version("5.2-beta1", sha256="3fd57916529381a46619e1cbfe1d372c7e008d5945fb1953da4a03b195630c33", url="https://pypi.org/packages/57/74/37f7e9703d488e832ef41672cd3ee303fae71fa189aa00681afb1bd71f9c/PyYAML-5.2b1.tar.gz")
    version("5.1.2", sha256="01adf0b6c6f61bd11af6e10ca52b7d4057dd0be0343eb9283c878cf3af56aee4", url="https://pypi.org/packages/e3/e8/b3212641ee2718d556df0f23f78de8303f068fe29cdaa7a91018849582fe/PyYAML-5.1.2.tar.gz")
    version("5.1.1", sha256="b4bb4d3f5e232425e25dda21c070ce05168a786ac9eda43768ab7f3ac2770955", url="https://pypi.org/packages/a3/65/837fefac7475963d1eccf4aa684c23b95aa6c1d033a2c5965ccb11e22623/PyYAML-5.1.1.tar.gz")
    version("5.1", sha256="436bc774ecf7c103814098159fbb84c2715d25980175292c648f2da143909f95", url="https://pypi.org/packages/9f/2c/9417b5c774792634834e730932745bc09a7d36754ca00acf1ccd1ac2594d/PyYAML-5.1.tar.gz")
    version("3.13", sha256="3ef3092145e9b70e3ddd2c7ad59bdd0252a94dfe3949721633e41344de00a6bf", url="https://pypi.org/packages/9e/a3/1d13970c3f36777c583f136c136f804d70f500168edc1edea6daa7200769/PyYAML-3.13.tar.gz")
    version("3.13-rc1", sha256="5679fb8e06e6b7c8341a488dfc80c776675493d50b0931d174116f03e544f06c", url="https://pypi.org/packages/03/f0/fa8d547b6b36cdba50009795bf7ae4df2491677efc9cd2cab655730830bf/PyYAML-3.13rc1.tar.gz")
    version("3.13-beta1", sha256="8a3dd5b3cfae5240925b66884d22cf6a80d1c5991863ef0b836fda2e2bcccc49", url="https://pypi.org/packages/d2/44/f2f50916afc03f48bd2bea7ff87fc73bb3d6454544b6c1267535ed87ad9b/PyYAML-3.13b1.tar.gz")
    version("3.12", sha256="5ac82e411044fb129bae5cfbeb3ba626acb2af31a8d17d175004b70862a741a7", url="https://pypi.org/packages/6b/f0/a0250248ea260d55748fff586d89a32afbb22656f4498b08d2636a48d4ec/PyYAML-3.12.zip")
    version("3.11", sha256="19bb3ac350ef878dda84a62d37c7d5c17a137386dde9c2ce7249c7a21d7f6ac9", url="https://pypi.org/packages/04/60/abfb3a665ee0569b60c89148b7187ddd8a36cb65e254fba945ae1315645d/PyYAML-3.11.zip")


