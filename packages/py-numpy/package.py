# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyNumpy(PythonPackage):
    # BEGIN VERSIONS
    version("1.26.4", sha256="2a02aba9ed12e4ac4eb3ea9421c420301a0c6460d9830d74a9df87efa4912010", url="https://pypi.org/packages/65/6e/09db70a523a96d25e115e71cc56a6f9031e7b8cd166c1ac8438307c14058/numpy-1.26.4.tar.gz")
    version("1.26.3", sha256="697df43e2b6310ecc9d95f05d5ef20eacc09c7c4ecc9da3f235d39e71b7da1e4", url="https://pypi.org/packages/d0/b0/13e2b50c95bfc1d5ee04925eb5c105726c838f922d0aaddd57b7c8be0f8b/numpy-1.26.3.tar.gz")
    version("1.26.2", sha256="f65738447676ab5777f11e6bbbdb8ce11b785e105f690bc45966574816b6d3ea", url="https://pypi.org/packages/dd/2b/205ddff2314d4eea852e31d53b8e55eb3f32b292efc3dd86bd827ab9019d/numpy-1.26.2.tar.gz")
    version("1.26.1", sha256="c8c6c72d4a9f831f328efb1312642a1cafafaa88981d9ab76368d50d07d93cbe", url="https://pypi.org/packages/78/23/f78fd8311e0f710fe1d065d50b92ce0057fe877b8ed7fd41b28ad6865bfc/numpy-1.26.1.tar.gz")
    version("1.26.0", sha256="f93fc78fe8bf15afe2b8d6b6499f1c73953169fad1e9a8dd086cdff3190e7fdf", url="https://pypi.org/packages/55/b3/b13bce39ba82b7398c06d10446f5ffd5c07db39b09bd37370dc720c7951c/numpy-1.26.0.tar.gz")
    version("1.25.2", sha256="fd608e19c8d7c55021dffd43bfe5492fab8cc105cc8986f813f8c3c048b38760", url="https://pypi.org/packages/a0/41/8f53eff8e969dd8576ddfb45e7ed315407d27c7518ae49418be8ed532b07/numpy-1.25.2.tar.gz")
    version("1.25.1", sha256="9a3a9f3a61480cc086117b426a8bd86869c213fc4072e606f01c4e4b66eb92bf", url="https://pypi.org/packages/cf/7a/f68d1d658a0e68084097beb212fa9356fee7eabff8b57231cc4acb555b12/numpy-1.25.1.tar.gz")
    version("1.25.0", sha256="f1accae9a28dc3cda46a91de86acf69de0d1b5f4edd44a9b0c3ceb8036dfff19", url="https://pypi.org/packages/d0/b2/fe774844d1857804cc884bba67bec38f649c99d0dc1ee7cbbf1da601357c/numpy-1.25.0.tar.gz")
    version("1.24.4", sha256="80f5e3a4e498641401868df4208b74581206afbee7cf7b8329daae82676d9463", url="https://pypi.org/packages/a4/9b/027bec52c633f6556dba6b722d9a0befb40498b9ceddd29cbe67a45a127c/numpy-1.24.4.tar.gz")
    version("1.24.3", sha256="ab344f1bf21f140adab8e47fdbc7c35a477dc01408791f8ba00d018dd0bc5155", url="https://pypi.org/packages/2c/d4/590ae7df5044465cc9fa2db152ae12468694d62d952b1528ecff328ef7fc/numpy-1.24.3.tar.gz")
    version("1.24.2", sha256="003a9f530e880cb2cd177cba1af7220b9aa42def9c4afc2a2fc3ee6be7eb2b22", url="https://pypi.org/packages/e4/a9/6704bb5e1d1d778d3a6ee1278a8d8134f0db160e09d52863a24edb58eab5/numpy-1.24.2.tar.gz")
    version("1.24.1", sha256="2386da9a471cc00a1f47845e27d916d5ec5346ae9696e01a8a34760858fe9dd2", url="https://pypi.org/packages/ce/b8/c170db50ec49d5845bd771bc5549fe734ee73083c5c52791915f95d8e2bc/numpy-1.24.1.tar.gz")
    version("1.24.0", sha256="c4ab7c9711fe6b235e86487ca74c1b092a6dd59a3cb45b63241ea0a148501853", url="https://pypi.org/packages/5f/c7/5ca7c100dcc85b5ef1b176bdf87be5e4392c2c3018e13cc7cdef828c6a09/numpy-1.24.0.tar.gz")
    version("1.23.5", sha256="1b1766d6f397c18153d40015ddfc79ddb715cabadc04d2d228d4e5a8bc4ded1a", url="https://pypi.org/packages/42/38/775b43da55fa7473015eddc9a819571517d9a271a9f8134f68fb9be2f212/numpy-1.23.5.tar.gz")
    version("1.23.4", sha256="ed2cc92af0efad20198638c69bb0fc2870a58dabfba6eb722c933b48556c686c", url="https://pypi.org/packages/64/8e/9929b64e146d240507edaac2185cd5516f00b133be5b39250d253be25a64/numpy-1.23.4.tar.gz")
    version("1.23.3", sha256="51bf49c0cd1d52be0a240aa66f3458afc4b95d8993d2d04f0d91fa60c10af6cd", url="https://pypi.org/packages/0a/88/f4f0c7a982efdf7bf22f283acf6009b29a9cc5835b684a49f8d3a4adb22f/numpy-1.23.3.tar.gz")
    version("1.23.2", sha256="b78d00e48261fbbd04aa0d7427cf78d18401ee0abd89c7559bbf422e5b1c7d01", url="https://pypi.org/packages/f4/66/17b8e95770478436bf968353c89683ce6f9e14d92e0d4fb3111c09ba18d2/numpy-1.23.2.tar.gz")
    version("1.23.1", sha256="d748ef349bfef2e1194b59da37ed5a29c19ea8d7e6342019921ba2ba4fd8b624", url="https://pypi.org/packages/13/b1/0c22aa7ca1deda4915cdec9562f839546bb252eecf6ad596eaec0592bd35/numpy-1.23.1.tar.gz")
    version("1.23.0", sha256="bd3fa4fe2e38533d5336e1272fc4e765cabbbde144309ccee8675509d5cd7b05", url="https://pypi.org/packages/03/c6/14a17e10813b8db20d1e800ff9a3a898e65d25f2b0e9d6a94616f1e3362c/numpy-1.23.0.tar.gz")
    version("1.22.4", sha256="425b390e4619f58d8526b3dcf656dde069133ae5c240229821f01b5f44ea07af", url="https://pypi.org/packages/f6/d8/ab692a75f584d13c6542c3994f75def5bce52ded9399f52e230fe402819d/numpy-1.22.4.zip")
    version("1.22.3", sha256="dbc7601a3b7472d559dc7b933b18b4b66f9aa7452c120e87dfb33d02008c8a18", url="https://pypi.org/packages/64/4a/b008d1f8a7b9f5206ecf70a53f84e654707e7616a771d84c05151a4713e9/numpy-1.22.3.zip")
    version("1.22.2", sha256="076aee5a3763d41da6bef9565fdf3cb987606f567cd8b104aded2b38b7b47abf", url="https://pypi.org/packages/e9/6c/c0a8130fe198f27bab92f1b28631e0cc2572295f6b7a31e87efe7448aa1c/numpy-1.22.2.zip")
    version("1.22.1", sha256="e348ccf5bc5235fc405ab19d53bec215bb373300e5523c7b476cc0da8a5e9973", url="https://pypi.org/packages/0a/c8/a62767a6b374a0dfb02d2a0456e5f56a372cdd1689dbc6ffb6bf1ddedbc0/numpy-1.22.1.zip")
    version("1.22.0", sha256="a955e4128ac36797aaffd49ab44ec74a71c11d6938df83b1285492d277db5397", url="https://pypi.org/packages/50/e1/9b0c184f04b8cf5f3c941ffa56fbcbe936888bdac9aa7ba6bae405ac752b/numpy-1.22.0.zip")
    version("1.21.6", sha256="ecb55251139706669fdec2ff073c98ef8e9a84473e51e716211b41aa0f18e656", url="https://pypi.org/packages/45/b7/de7b8e67f2232c26af57c205aaad29fe17754f793404f59c8a730c7a191a/numpy-1.21.6.zip")
    version("1.21.5", sha256="6a5928bc6241264dce5ed509e66f33676fc97f464e7a919edc672fb5532221ee", url="https://pypi.org/packages/c2/a8/a924a09492bdfee8c2ec3094d0a13f2799800b4fdc9c890738aeeb12c72e/numpy-1.21.5.zip")
    version("1.21.4", sha256="e6c76a87633aa3fa16614b61ccedfae45b91df2767cf097aa9c933932a7ed1e0", url="https://pypi.org/packages/fb/48/b0708ebd7718a8933f0d3937513ef8ef2f4f04529f1f66ca86d873043921/numpy-1.21.4.zip")
    version("1.21.3", sha256="63571bb7897a584ca3249c86dd01c10bcb5fe4296e3568b2e9c1a55356b6410e", url="https://pypi.org/packages/5f/d6/ad58ded26556eaeaa8c971e08b6466f17c4ac4d786cd3d800e26ce59cc01/numpy-1.21.3.zip")
    version("1.21.2", sha256="423216d8afc5923b15df86037c6053bf030d15cc9e3224206ef868c2d63dd6dc", url="https://pypi.org/packages/3a/be/650f9c091ef71cb01d735775d554e068752d3ff63d7943b26316dc401749/numpy-1.21.2.zip")
    version("1.21.1", sha256="dff4af63638afcc57a3dfb9e4b26d434a7a602d225b42d746ea7fe2edf1342fd", url="https://pypi.org/packages/0b/a7/e724c8df240687b5fd62d8c71f1a6709d455c4c09432c7412e3e64f4cbe5/numpy-1.21.1.zip")
    version("1.21.0", sha256="e80fe25cba41c124d04c662f33f6364909b985f2eb5998aaa5ae4b9587242cce", url="https://pypi.org/packages/66/03/818876390c7ff4484d5a05398a618cfdaf0a2b9abb3a7c7ccd59fe181008/numpy-1.21.0.zip")
    version("1.20.3", sha256="e55185e51b18d788e49fe8305fd73ef4470596b33fc2c1ceb304566b99c71a69", url="https://pypi.org/packages/f3/1f/fe9459e39335e7d0e372b5e5dcd60f4381d3d1b42f0b9c8222102ff29ded/numpy-1.20.3.zip")
    version("1.20.2", sha256="878922bf5ad7550aa044aa9301d417e2d3ae50f0f577de92051d739ac6096cee", url="https://pypi.org/packages/82/a8/1e0f86ae3f13f7ce260e9f782764c16559917f24382c74edfb52149897de/numpy-1.20.2.zip")
    version("1.20.1", sha256="3bc63486a870294683980d76ec1e3efc786295ae00128f9ea38e2c6e74d5a60a", url="https://pypi.org/packages/d2/48/f445be426ccd9b2fb64155ac6730c7212358882e589cd3717477d739d9ff/numpy-1.20.1.zip")
    version("1.20.0", sha256="3d8233c03f116d068d5365fed4477f2947c7229582dad81e5953088989294cec", url="https://pypi.org/packages/c3/97/fd507e48f8c7cab73a9f002e52e15983b5636b4ac6cf69b83ae240324b44/numpy-1.20.0.zip")
    version("1.19.5", sha256="a76f502430dd98d7546e1ea2250a7360c065a5fdea52b2dffe8ae7180909b6f4", url="https://pypi.org/packages/51/60/3f0fe5b7675a461d96b9d6729beecd3532565743278a9c3fe6dd09697fa7/numpy-1.19.5.zip")
    version("1.19.4", sha256="141ec3a3300ab89c7f2b0775289954d193cc8edb621ea05f99db9cb181530512", url="https://pypi.org/packages/c5/63/a48648ebc57711348420670bb074998f79828291f68aebfff1642be212ec/numpy-1.19.4.zip")
    version("1.19.3", sha256="35bf5316af8dc7c7db1ad45bec603e5fb28671beb98ebd1d65e8059efcfd3b72", url="https://pypi.org/packages/cb/c0/7b3d69e6ee68bc54c97ba51f8c3c3e43ff1dbc7bd97347cc19a1f944e60a/numpy-1.19.3.zip")
    version("1.19.2", sha256="0d310730e1e793527065ad7dde736197b705d0e4c9999775f212b03c44a8484c", url="https://pypi.org/packages/bf/e8/15aea783ea72e2d4e51e3ec365e8dc4a1a32c9e5eb3a6d695b0d58e67cdd/numpy-1.19.2.zip")
    version("1.19.1", sha256="b8456987b637232602ceb4d663cb34106f7eb780e247d51a260b84760fd8f491", url="https://pypi.org/packages/2c/2f/7b4d0b639a42636362827e611cfeba67975ec875ae036dd846d459d52652/numpy-1.19.1.zip")
    version("1.19.0", sha256="76766cc80d6128750075378d3bb7812cf146415bd29b588616f72c943c00d598", url="https://pypi.org/packages/f1/2c/717bdd12404c73ec0c8c734c81a0bad7048866bc36a88a1b69fd52b01c07/numpy-1.19.0.zip")
    version("1.18.5", sha256="34e96e9dae65c4839bd80012023aadd6ee2ccb73ce7fdf3074c62f301e63120b", url="https://pypi.org/packages/01/1b/d3ddcabd5817be02df0e6ee20d64f77ff6d0d97f83b77f65e98c8a651981/numpy-1.18.5.zip")
    version("1.18.4", sha256="bbcc85aaf4cd84ba057decaead058f43191cc0e30d6bc5d44fe336dc3d3f4509", url="https://pypi.org/packages/2d/f3/795e50e3ea2dc7bc9d1a2eeea9997d5dce63b801e08dfc37c2efce341977/numpy-1.18.4.zip")
    version("1.18.3", sha256="e46e2384209c91996d5ec16744234d1c906ab79a701ce1a26155c9ec890b8dc8", url="https://pypi.org/packages/0c/e8/c49cb52ed2ad734efb49eb1f7766888b0e65df1848f71fa7f7fd52183392/numpy-1.18.3.zip")
    version("1.18.2", sha256="e7894793e6e8540dbeac77c87b489e331947813511108ae097f1715c018b8f3d", url="https://pypi.org/packages/84/1e/ff467ac56bfeaea51d4a2e72d315c1fe440b20192fea7e460f0f248acac8/numpy-1.18.2.zip")
    version("1.18.1", sha256="b6ff59cee96b454516e47e7721098e6ceebef435e3e21ac2d6c3b8b02628eb77", url="https://pypi.org/packages/40/de/0ea5092b8bfd2e3aa6fdbb2e499a9f9adf810992884d414defc1573dca3f/numpy-1.18.1.zip")
    version("1.18.0", sha256="a9d72d9abaf65628f0f31bbb573b7d9304e43b1e6bbae43149c17737a42764c4", url="https://pypi.org/packages/31/0a/5df350c29a06835d534a6c4f5681075304da38d85f1c69e5226a635a67ce/numpy-1.18.0.zip")
    version("1.17.5", sha256="16507ba6617f62ae3c6ab1725ae6f550331025d4d9a369b83f6d5a470446c342", url="https://pypi.org/packages/d9/09/8e89c05abc450ea347f40b4fa917ec5c69b5228da344487f178586a3187c/numpy-1.17.5.zip")
    version("1.17.4", sha256="f58913e9227400f1395c7b800503ebfdb0772f1c33ff8cb4d6451c06cabdf316", url="https://pypi.org/packages/ff/59/d3f6d46aa1fd220d020bdd61e76ca51f6548c6ad6d24ddb614f4037cf49d/numpy-1.17.4.zip")
    version("1.17.3", sha256="a0678793096205a4d784bd99f32803ba8100f639cf3b932dc63b21621390ea7e", url="https://pypi.org/packages/b6/d6/be8f975f5322336f62371c9abeb936d592c98c047ad63035f1b38ae08efe/numpy-1.17.3.zip")
    version("1.16.1", sha256="31d3fe5b673e99d33d70cfee2ea8fe8dccd60f265c3ed990873a88647e3dd288", url="https://pypi.org/packages/2b/26/07472b0de91851b6656cbc86e2f0d5d3a3128e7580f23295ef58b6862d6c/numpy-1.16.1.zip")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.9:", when="@1.25,1.26.2:")
        depends_on("python@3.9:3.12", when="@1.26:1.26.1")
        depends_on("python@3.8:", when="@1.22:1.24")
        depends_on("python@3.7:", when="@1.20:1.21.1")
        depends_on("python@3.7:3.10", when="@1.21.2:1.21")
    # END DEPENDENCIES

