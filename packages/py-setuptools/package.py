# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PySetuptools(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("69.2.0", sha256="c21c49fb1042386df081cb5d86759792ab89efca84cf114889191cd09aacc80c", url="https://pypi.org/packages/92/e1/1c8bb3420105e70bdf357d57dd5567202b4ef8d27f810e98bb962d950834/setuptools-69.2.0-py3-none-any.whl")
    version("69.1.1", sha256="02fa291a0471b3a18b2b2481ed902af520c69e8ae0919c13da936542754b4c56", url="https://pypi.org/packages/c0/7a/3da654f49c95d0cc6e9549a855b5818e66a917e852ec608e77550c8dc08b/setuptools-69.1.1-py3-none-any.whl")
    version("69.1.0", sha256="c054629b81b946d63a9c6e732bc8b2513a7c3ea645f11d0139a2191d735c60c6", url="https://pypi.org/packages/bb/0a/203797141ec9727344c7649f6d5f6cf71b89a6c28f8f55d4f18de7a1d352/setuptools-69.1.0-py3-none-any.whl")
    version("69.0.3", sha256="385eb4edd9c9d5c17540511303e39a147ce2fc04bc55289c322b9e5904fe2c05", url="https://pypi.org/packages/55/3a/5121b58b578a598b269537e09a316ad2a94fdd561a2c6eb75cd68578cc6b/setuptools-69.0.3-py3-none-any.whl")
    version("69.0.2", sha256="1e8fdff6797d3865f37397be788a4e3cba233608e9b509382a2777d25ebde7f2", url="https://pypi.org/packages/bb/e1/ed2dd0850446b8697ad28d118df885ad04140c64ace06c4bd559f7c8a94f/setuptools-69.0.2-py3-none-any.whl")
    version("69.0.1", sha256="6875bbd06382d857b1b90cd07cee6a2df701a164f241095706b5192bc56c5c62", url="https://pypi.org/packages/f9/59/701df637517d6af0434cbb580bfc35a9c536aa7f47e0c2e222f1ef83547c/setuptools-69.0.1-py3-none-any.whl")
    version("69.0.0", sha256="eb03b43f23910c5fd0909cb677ad017cd9531f493d27f8b3f5316ff1fb07390e", url="https://pypi.org/packages/0f/93/daae527a7ad3ea3a4f7d84d05fd74b7cc637360a7e7b4df1df9a5046be17/setuptools-69.0.0-py3-none-any.whl")
    version("68.2.2", sha256="b454a35605876da60632df1a60f736524eb73cc47bbc9f3f1ef1b644de74fd2a", url="https://pypi.org/packages/bb/26/7945080113158354380a12ce26873dd6c1ebd88d47f5bc24e2c5bb38c16a/setuptools-68.2.2-py3-none-any.whl")
    version("68.2.1", sha256="eff96148eb336377ab11beee0c73ed84f1709a40c0b870298b0d058828761bae", url="https://pypi.org/packages/95/79/6b47c6a872b40743a480687dc0c79ffb4202710789f3e4d54a84fff8b550/setuptools-68.2.1-py3-none-any.whl")
    version("68.2.0", sha256="af3d5949030c3f493f550876b2fd1dd5ec66689c4ee5d5344f009746f71fd5a8", url="https://pypi.org/packages/82/3b/0715493246eb08e93506f4da0efe1d05a3c9d9ac3b76e97cc362890e6adf/setuptools-68.2.0-py3-none-any.whl")
    version("66.1.1", sha256="6f590d76b713d5de4e49fe4fbca24474469f53c83632d5d0fd056f7ff7e8112b", url="https://pypi.org/packages/c2/8b/abb577ca6ab2c71814d535b1ed1464c5f4aaefe1a31bbeb85013eb9b2401/setuptools-66.1.1-py3-none-any.whl")
    version("66.1.0", sha256="fc19f9f62120a763300fd78e234b3cbd3417be098f08c156eaaf36420627e57b", url="https://pypi.org/packages/c5/94/00e3d21daa5a47c4f13d278ff08c1b3dbd167231e4a1c4b2c99e4616790e/setuptools-66.1.0-py3-none-any.whl")
    version("66.0.0", sha256="a78d01d1e2c175c474884671dde039962c9d74c7223db7369771fcf6e29ceeab", url="https://pypi.org/packages/bd/ef/76cffd20061a0c6512dad4ba3537314904c6350738b99526c2f48992ff58/setuptools-66.0.0-py3-none-any.whl")
    version("65.7.0", sha256="8ab4f1dbf2b4a65f7eec5ad0c620e84c34111a68d3349833494b9088212214dd", url="https://pypi.org/packages/ff/97/9dc902414912192d68364cc01cf17e826d259ef9753504b7ae1a256f2e35/setuptools-65.7.0-py3-none-any.whl")
    version("65.6.3", sha256="57f6f22bde4e042978bcd50176fdb381d7c21a9efa4041202288d3737a0c6a54", url="https://pypi.org/packages/ef/e3/29d6e1a07e8d90ace4a522d9689d03e833b67b50d1588e693eec15f26251/setuptools-65.6.3-py3-none-any.whl")
    version("65.6.2", sha256="97a4a824325146ebc8dc29b0aa5f3b1eaa590a0f00cacbfdf81831670f07862d", url="https://pypi.org/packages/45/0a/0d9b81fa11d177e057b7f761b367dc409077ffd7ba3dc46d79c78444961c/setuptools-65.6.2-py3-none-any.whl")
    version("65.6.1", sha256="9b1b1b4129877c74b0f77de72b64a1084a57ccb106e7252f5fb70f192b3d9055", url="https://pypi.org/packages/b2/0f/945bdfe5007ebd4a7ead88d8e95f6f1326d8f3ad206bbb5824b515c61dcd/setuptools-65.6.1-py3-none-any.whl")
    version("65.6.0", sha256="6211d2f5eddad8757bd0484923ca7c0a6302ebc4ab32ea5e94357176e0ca0840", url="https://pypi.org/packages/1f/97/c03668380f278f1f8b0486d820c142cf224bba1bd78416e1797b52e0e81c/setuptools-65.6.0-py3-none-any.whl")
    version("65.5.1", sha256="d0b9a8433464d5800cbe05094acf5c6d52a91bfac9b52bcfc4d41382be5d5d31", url="https://pypi.org/packages/b6/40/353c051f77ee5618adaf1fd96f4f6bae9714ed0a22c7142c01c24eb77fe4/setuptools-65.5.1-py3-none-any.whl")
    version("65.5.0", sha256="f62ea9da9ed6289bfe868cd6845968a2c854d1427f8548d52cae02a42b4f0356", url="https://pypi.org/packages/41/82/7f54bbfe5c247a8c9f78d8d1d7c051847bcb78843c397b866dba335c1e88/setuptools-65.5.0-py3-none-any.whl")
    version("65.4.1", sha256="1b6bdc6161661409c5f21508763dc63ab20a9ac2f8ba20029aaaa7fdb9118012", url="https://pypi.org/packages/bd/b4/f120561bc94a04bae5d71ea86fe2c7d97f57ab89635b4739ec4abceda92d/setuptools-65.4.1-py3-none-any.whl")
    version("65.4.0", sha256="c2d2709550f15aab6c9110196ea312f468f41cd546bceb24127a1be6fdcaeeb1", url="https://pypi.org/packages/d5/e6/e3a70a77dda22766b9ef4ff47ff8320720311e78d11d1401baffca3f6879/setuptools-65.4.0-py3-none-any.whl")
    version("65.3.0", sha256="2e24e0bec025f035a2e72cdd1961119f557d78ad331bb00ff82efb2ab8da8e82", url="https://pypi.org/packages/d9/5f/2daccd14278b6b780ae6799f85998377c06019354982391245f4b58a927d/setuptools-65.3.0-py3-none-any.whl")
    version("65.2.0", sha256="a3ca5857c89f82f5c9410e8508cb32f4872a3bafd4aa7ae122a24ca33bccc750", url="https://pypi.org/packages/e5/6f/942e63ec2a5c881df147782b97dc4715ca082dec9de41f43e1013faef710/setuptools-65.2.0-py3-none-any.whl")
    version("65.1.1", sha256="1c664b23706b753986b0f4b13e20bb82177ab29450d5b4d5d6d244c34a2235bd", url="https://pypi.org/packages/6d/1e/ff7c90e2a0514cef2ed4fb7d49944d45674fe7c7a305d6553a5025ae09fa/setuptools-65.1.1-py3-none-any.whl")
    version("65.1.0", sha256="10602cd0a6f5feab6656e9587f9075292ab777c5200f3bf00293ecd23d9f2788", url="https://pypi.org/packages/18/1e/7cd4bf0d0c4e109595b5e69621f72c4e01079c533ccb94003dfe361c62ea/setuptools-65.1.0-py3-none-any.whl")
    version("65.0.2", sha256="39275e7aafa4a4f0f4308f2302c6ee384dcdacdbaacc1e30dcbb6fd824c625bb", url="https://pypi.org/packages/02/70/40276081ce5d29e7610618a857909e4eba264c0c9cfb4ecb613a4f7ad0ef/setuptools-65.0.2-py3-none-any.whl")
    version("65.0.1", sha256="7a2e7e95c3bf33f356b4c59aee7a6848585c4219dd3e941e43cc117888f210e4", url="https://pypi.org/packages/9d/b9/48de2d69a45354b20ca754e6c61736f1db3707c208ea04908766b184fd23/setuptools-65.0.1-py3-none-any.whl")
    version("59.6.0", sha256="4ce92f1e1f8f01233ee9952c04f6b81d1e02939d6e1b488428154974a4d0783e", url="https://pypi.org/packages/b0/3a/88b210db68e56854d0bcf4b38e165e03be377e13907746f825790f3df5bf/setuptools-59.6.0-py3-none-any.whl")
    version("59.5.0", sha256="6d10741ff20b89cd8c6a536ee9dc90d3002dec0226c78fb98605bfb9ef8a7adf", url="https://pypi.org/packages/40/a9/7deac76c58fa47c95360116a06b53b9b62f6db11336fe61b6ab53784d98b/setuptools-59.5.0-py3-none-any.whl")
    version("59.4.0", sha256="feb5ff19b354cde9efd2344ef6d5e79880ce4be643037641b49508bbb850d060", url="https://pypi.org/packages/6f/ea/e12311dabc63a6a434be25e6011c1513cc95d0cf22e5f13036f75b3ec508/setuptools-59.4.0-py3-none-any.whl")
    version("59.3.0", sha256="10635f160e9e71546b883e337646567156a02808ecc0e7fafc12021deabf205e", url="https://pypi.org/packages/29/e3/a1edb6bef52fd8d4cbe62cf2b6b444e7145edf89fae7ce9bffbfb92ae8b9/setuptools-59.3.0-py3-none-any.whl")
    version("59.2.0", sha256="4adde3d1e1c89bde1c643c64d89cdd94cbfd8c75252ee459d4500bccb9c7d05d", url="https://pypi.org/packages/18/ad/ec41343a49a0371ea40daf37b1ba2c11333cdd121cb378161635d14b9750/setuptools-59.2.0-py3-none-any.whl")
    version("59.1.1", sha256="fb537610c2dfe77b5896e3ee53dd53fbdd9adc48076c8f28cee3a30fb59a5038", url="https://pypi.org/packages/ed/60/15ee37d6d3385e6a432d39b5ac51f8467178ad989ba50f2b55681c1a038e/setuptools-59.1.1-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    # END DEPENDENCIES

