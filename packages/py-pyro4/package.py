# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyro4(PythonPackage):
    # BEGIN VERSIONS
    version("4.81", sha256="589e233511b620884dd115d0ae51dc2e8bd8eb5deb255b7dab99c3cbb9ec64b0", url="https://pypi.org/packages/12/da/e7f90b0c6de8cffe967d02fc57e0e5ab648dc0d75cc0de4ecb37e1f75a1e/Pyro4-4.81-py2.py3-none-any.whl")
    version("4.80", sha256="f195a4a9403f58807e66ca269c771e1d268064945f65cfbbf59a1feb12a1695f", url="https://pypi.org/packages/c3/3c/422f6f761076c5679215178a00eca9a68aacfbbc88152c85b15928b60e25/Pyro4-4.80-py2.py3-none-any.whl")
    version("4.79", sha256="d2d258df297c24540f3eaa591df8fe7b1ac22f7339a2b56a4bde560c63341219", url="https://pypi.org/packages/00/83/b05a3e6e253dc6bed35edb1ae0c29f1bc589c038dabaa85ce5ee37c72bd0/Pyro4-4.79-py2.py3-none-any.whl")
    version("4.78", sha256="98c2c9547d111ecbf2c1f327953ee1919db60b701b8fe9a612f40359b2ea70ba", url="https://pypi.org/packages/e5/24/123d570d039bbe167f266025c2551683e115ffa475ed5d66208b0c8c97c1/Pyro4-4.78-py2.py3-none-any.whl")
    version("4.77", sha256="7c4712257ba5bed8bc4ed037bdad5b4683a483a5fd634a2ac3effa5ba787f511", url="https://pypi.org/packages/97/a2/70bf3d3aa6707eb264b9eb0e0899f3a90a3e062b2178da54e53ba4de2185/Pyro4-4.77-py2.py3-none-any.whl")
    version("4.76", sha256="6d7b74ba2f80eaab0548759767ee46e8aeeea059fcc1ecc9758deb0f51a3bff7", url="https://pypi.org/packages/7f/95/2b4f9828a750545a7932400547a756db863561f01cd003d585b6fc255be8/Pyro4-4.76-py2.py3-none-any.whl")
    version("4.75", sha256="f430be91443dd2f22ad67228863abaa5e176e786e7234f3e715d2203beadb635", url="https://pypi.org/packages/15/93/219968d8bdc3eab73b8971b155b2006e11cf1e0b284d2e81611da8c3e7ca/Pyro4-4.75-py2.py3-none-any.whl")
    version("4.74", sha256="a92a27dd3f1125f17de88512c6add0c041831503e0171ff5677afd05e095d358", url="https://pypi.org/packages/55/97/d489cf7aebf77c4bfa245b26f446c5e3a1644c11ba41f871c08ed32da379/Pyro4-4.74-py2.py3-none-any.whl")
    version("4.73", sha256="4a71a613015d1a2bca6939d9ce4d5866ccd1fd30365ebbbf67482b6341867cf8", url="https://pypi.org/packages/0b/06/74f9170f8bec778a8487c95a26a4fc842f6af4b0e815a74084b75aef2729/Pyro4-4.73-py2.py3-none-any.whl")
    version("4.72", sha256="12e7a279d0205d3f0260d001dfe6e951c373160a8208ff450d5e0280192ac22d", url="https://pypi.org/packages/9d/75/a1191238485e89a0ae16f64a45fb1dd6f3e69358c1c867886553745706cb/Pyro4-4.72-py2.py3-none-any.whl")
    version("4.71", sha256="a04898be3c8f190b596ae20e65816e4e2087c6d72cddfe988bbdd5c5dc939f91", url="https://pypi.org/packages/cc/46/b36ca811c4761666d6059103de123921706c1a8334d16a5d55f808a8e5dc/Pyro4-4.71-py2.py3-none-any.whl")
    version("4.70", sha256="746ceaf95cd4f83ff02af56787f2e8081477a36d858630ffc62792cf7b763753", url="https://pypi.org/packages/49/1a/3b61c1f7574ebee65f6c13504a04f0330f9597f15dbc6d13028cbd5d3c09/Pyro4-4.70-py2.py3-none-any.whl")
    version("4.63", sha256="ce53712a86590e1bd4deeb201cdd057ccd1586ab41b1b6e3a3f61a9bd6412ba4", url="https://pypi.org/packages/5c/a1/28a5dcd453044efbcfe368a6cc1bc5f1518dadbc310ee1107d9b7b7cbaaa/Pyro4-4.63-py2.py3-none-any.whl")
    version("4.62", sha256="67268f60b6de82a2cca411cd47d41560d79e74f2781ed36c1b7adaaeb434dd6f", url="https://pypi.org/packages/6c/a1/fab368ea678d6318ed434a0291d3d688ac5c1fe6bb634b37af25a7ca86bb/Pyro4-4.62-py2.py3-none-any.whl")
    version("4.61", sha256="540f8dd5ecf81e83fe909c3a83c8e1275d3469f6a5650fbc729948680fcb6bed", url="https://pypi.org/packages/1d/91/f547b63dcb717aa7d98b95b2beb0d7eb62a3b4ca0a6372a779e69fd22d53/Pyro4-4.61-py2.py3-none-any.whl")
    version("4.60", sha256="ffe5e9a2e6025fda3d34c0dbdad2e00df219d129f9addee5d22b4a05fbe6f586", url="https://pypi.org/packages/7c/e2/c6d4059f7b9f2ae627ede66d1f8bfe7779b8048e35255689970e963f3f05/Pyro4-4.60-py2.py3-none-any.whl")
    version("4.59", sha256="2edcd659013f24f9565a15c4b922a692977295b4e44d1fac01cfbe7536d31b55", url="https://pypi.org/packages/d1/88/50a541183cc4366e9e889340268e11503c86ab04e81dda0bd2f03c69ed2d/Pyro4-4.59-py2.py3-none-any.whl")
    version("4.58", sha256="605f40ac094ea82867fa32d2f9568ebf1abaa95d2e5f4f1a1aeb225bf69adf0c", url="https://pypi.org/packages/00/c6/0361bd70ee36892dd68cfe660091367636273d9652c4b0216f23d632b131/Pyro4-4.58-py2.py3-none-any.whl")
    version("4.57", sha256="8ff841272d829f2e1f882fb811e5903147a2623f00fccc40da47d6868e7c42a5", url="https://pypi.org/packages/17/75/41dca2258b3bb987476afa188e9fd1914caea1e882a2ee372972adec6814/Pyro4-4.57-py2.py3-none-any.whl")
    version("4.56", sha256="7199f6f9957776df38b9da507ce0f13c20acf1747a4aa76563bf8c2824901950", url="https://pypi.org/packages/f3/f7/b3122361de40b8a23551dc2a6325c59aecc6456379f8424e32c573fc0287/Pyro4-4.56-py2.py3-none-any.whl")
    version("4.55", sha256="813566c12582af71e76a9b923a5e35ed204a64a6d00c1969d94b2c0f627caf11", url="https://pypi.org/packages/73/da/e8d902ca918e54317f80fb05e3a7be0043c5ade75a9c0b77c424bc6f607f/Pyro4-4.55-py2.py3-none-any.whl")
    version("4.54", sha256="5178d213cc4d1ec38c79aeb94270e7240f57a3608ab7429c274b6d8e4cc29d82", url="https://pypi.org/packages/23/7b/e7f44432c35fe7dd0c2e96b6dbee01a99ce741b5317005bca26df87afc15/Pyro4-4.54-py2.py3-none-any.whl")
    version("4.53", sha256="d0b53d60ad42647a16518497965597fcbfa4930771bb42b708bc803d81478eff", url="https://pypi.org/packages/7d/38/a8151075e91652d70c6e639d6d8c8e9ed4375a976a6f9cfdf98db0fbf1d2/Pyro4-4.53-py2.py3-none-any.whl")
    version("4.52", sha256="a947f1ec698c2d8c268b31acc373f7842d6758c468c0c540ca5a249f64a503d4", url="https://pypi.org/packages/ad/33/f3863812e7bf8919edaa7e3ebc7dc2478ac56707477384f97a9b82844ea3/Pyro4-4.52-py2.py3-none-any.whl")
    version("4.51", sha256="2d78bfe965cf75e46c73f39bc3646a9c346f69f75a8ffccf49c3a49dacd84b2c", url="https://pypi.org/packages/54/f8/023a1496aabae5d83f79a9a3400ddb06f92b8c4c3e5294318fe84683467e/Pyro4-4.51-py2.py3-none-any.whl")
    version("4.50", sha256="ae237fb81525507640945762854399fa83c1cea7ee27c7eaf0b3225f543816f9", url="https://pypi.org/packages/3d/92/71cd6a75fb28cb3d581d15b5bd71a3b2f3e1d5665bdd1c0c19d6902d2afa/Pyro4-4.50-py2.py3-none-any.whl")
    version("4.49", sha256="2425f6fcda5d4146d1ba6ef82b5bebc93ad615c61753dcbc04c877832a792046", url="https://pypi.org/packages/1a/20/1dd3457256fd0e40f6ebaeac8c70b175177d5914c2ffa826e3662083add5/Pyro4-4.49-py2.py3-none-any.whl")
    version("4.48", sha256="e7671b23b405b9bf43a10284cb677e5cef9c1cdfc6d95193099e73bc15102653", url="https://pypi.org/packages/c5/5f/a2fa0c88c730ed94190e6fed003836c7c54466f2d0b3a7d583ba195f780d/Pyro4-4.48-py2.py3-none-any.whl")
    version("4.47", sha256="4b706b865a78eb7e428ac83910ebc539f174aa4a019b91437c3dec8f39f64afa", url="https://pypi.org/packages/c5/6c/944720c7dae363ac1493d831bc84c9561d92aa788fa32b74f995b0f8060d/Pyro4-4.47-py2.py3-none-any.whl")
    version("4.46", sha256="49a9de345ec6aaeb0076ed55c27201d69c382736f5000eb75558afdefb21fc9c", url="https://pypi.org/packages/be/05/7c35110b88672e07929a4e5201660673c12a271bd424f0aa4ce21b728485/Pyro4-4.46-py2.py3-none-any.whl")
    version("4.45", sha256="de78f46c966aaac8e3289657532ccef89d5d5e185fa5a7f7cc675daa48e2311b", url="https://pypi.org/packages/44/e3/679867a25df3ca08264dcd2742f7db313945c833ef20267bb779c017b99a/Pyro4-4.45-py2.py3-none-any.whl")
    version("4.43", sha256="e269c477096c625c23a9409542df466b230d0a7d5e65228eb66b97fd429195b5", url="https://pypi.org/packages/be/f9/59164d58c724d91ebf45dea23a2ae58d7ec157c1338966e35b1a9822f737/Pyro4-4.43-py2.py3-none-any.whl")
    version("4.42", sha256="723a1aa8b6663c6b9775526187a6029dc41c7f416c73ff7f88f10779b3904ef3", url="https://pypi.org/packages/01/af/56b5184d98336b7b964637091aa6032450ecffe2cf357523e64179af9bbb/Pyro4-4.42-py2.py3-none-any.whl")
    version("4.41", sha256="33ff0d3428549e7ad88bb1ba7022331defd7004ab75eca4bc1dae22b1284fbb3", url="https://pypi.org/packages/82/58/1605f375b384c2f1cee3069d879e03a856beff8c81160ba4cad8f4272c04/Pyro4-4.41-py2.py3-none-any.whl")
    version("4.40", sha256="c8445c957f5cfa5794e78b4bb6b6ec73c2cccf83706a762a621b3426e7c01e69", url="https://pypi.org/packages/2b/64/bbaaeb62e4285dddf62048ea2f8971a33c5f0965bf26274b50612d60ff07/Pyro4-4.40-py2.py3-none-any.whl")
    version("4.39", sha256="fca9b25b43bcfe62f0bb34088825d046b42956ee829d17707efc2f27c554a7b9", url="https://pypi.org/packages/25/ab/218754d832707d28af602e653b6a06769023cdfcdc1e525d75e0872e3407/Pyro4-4.39-py2.py3-none-any.whl")
    version("4.38", sha256="9da0aa41500315f871229f38038d8f5b8a4d495329b35e45fb1acf94f80db0ad", url="https://pypi.org/packages/eb/9e/de0a73306a87984c9df04aa07a3e9936d895979305807eef1aefd69175e0/Pyro4-4.38-py2.py3-none-any.whl")
    version("4.37", sha256="9c0c135f96200b07a65687aa39bfa196d33388b909691df18bc440e5e9131e8c", url="https://pypi.org/packages/86/e7/f0e9a387758e266a358d4eabf3685185ebe7af38c15bbc4d8f463822f387/Pyro4-4.37-py2.py3-none-any.whl")
    version("4.36", sha256="71b192dc0056bf7952a0084d2008d9012f66abfe47f11e1daf988bd20cf50902", url="https://pypi.org/packages/0a/8b/0a72bb185b29648d089c96e90c60e02a2723bdf480f297c0c7bf6fd069d7/Pyro4-4.36-py2.py3-none-any.whl")
    version("4.35", sha256="8e8e2d2ca2ca96eb35b4da5c8f297ba9fc8994e52249ded961c6ef0d15470778", url="https://pypi.org/packages/3b/fe/f6e52f8488a1873a959e118951d91336913e2849adf178455b134e3d7f50/Pyro4-4.35-2-py2.py3-none-any.whl")
    version("4.34", sha256="0ffe692e976c0457237e9e4635a7da5bc83a185d919dcbd04f5c757a114330ee", url="https://pypi.org/packages/cd/05/402b00a87374f824bf87c03aba2b800e3faae240b1a1cdad5a256a8eef13/Pyro4-4.34-py2.py3-none-any.whl")
    version("4.33", sha256="fd810c6523516a0f4f6188507fd4dc5d087217a118179a01c8746b27497f1c88", url="https://pypi.org/packages/1f/30/9d045b3b2499dc57ecb09245e21d6a35e8319d0cc39451fdfcd4403fea84/Pyro4-4.33-py2.py3-none-any.whl")
    version("4.32", sha256="a60d56872c4f08a3775f9b85f4267142d3346c91b37ca3a57fa5f6026e598eb0", url="https://pypi.org/packages/d8/1e/cd731e4a0c3761fde0bb72acbf5039e1e8de4a61355d87d8281c1342cf92/Pyro4-4.32-py2.py3-none-any.whl")
    version("4.31", sha256="c9d4bc474367ca5ec05a934ccc4a90ee34057e54c70e6337de888381185b40a5", url="https://pypi.org/packages/da/2e/ba269c08586ee2a4e765205101de4bca4eaa381f0aeda4f7c5b4746106a2/Pyro4-4.31-py2.py3-none-any.whl")
    version("4.30", sha256="d43bc0d7427f6d5bc758ffd4478913f92103adb8a659c0d85f17d0d612fae145", url="https://pypi.org/packages/3a/b0/6037396878e5e21b443f341a2bb8ea69f917e58e4b27196d767dab7066ea/Pyro4-4.30-py2.py3-none-any.whl")
    version("4.29", sha256="690d2ca055a6a78a14c2b92c8cedbfa495a74f075c84d96318386b5f39e6e169", url="https://pypi.org/packages/36/3d/a7868eb4f6c95ccf521493a42f060b2f777d19175641a04e1555f5eb4b6f/Pyro4-4.29-py2.py3-none-any.whl")
    version("4.28", sha256="f05d79b78457048083f8d1d7149896b325efc5ed72ad48b2796df8d34222ccca", url="https://pypi.org/packages/8f/35/232aa7554263681a410212fb56a97fd0764d976d16cdeec17c44cdcc4072/Pyro4-4.28-py2.py3-none-any.whl")
    version("4.27", sha256="39bb9429163ba92e76ed32b27baed901ced0af08ab049bb474c43b9473c18334", url="https://pypi.org/packages/5a/92/66f3726c68048afd216c777bb9b2078ee543cff4d7659b1be7f2e5b5ef69/Pyro4-4.27-py2.py3-none-any.whl")
    version("4.26", sha256="18d1bce57989b7d0bca564c2524e4b70bc9c503b06155b670b96f5419d8d19ee", url="https://pypi.org/packages/77/e2/e4f108b22b4523f26ce7c63b447b2947048c296009e7850913b078d46f02/Pyro4-4.26-py2.py3-none-any.whl")
    version("4.25", sha256="f32ed15462f945106906578365508a5deb8e17728299c77b912dc9f5ad984b4e", url="https://pypi.org/packages/f4/23/dc7a7b873c614e506fd1e14c707ed6befd8625aaa9c45fe264b6d57531fb/Pyro4-4.25-py2.py3-none-any.whl")
    version("4.24", sha256="c32df9365b2409eda60a8f6b8f589050977c160a0ab1d79999bf6b465816e8d7", url="https://pypi.org/packages/31/01/1644c59ce801e08dcdadb06a71b2cdc9f6ac9ffb3fa41183e6b04ecc7de5/Pyro4-4.24-py2.py3-none-any.whl")
    version("4.23", sha256="57d6feee20a565f9de3302376a2531cfda50755088442102963b16e6f70b2e3b", url="https://pypi.org/packages/f7/e8/a2e71fb632c1d6ee66b042475ff5b9c637245036e1ffa25a3ef0a49387a0/Pyro4-4.23.tar.gz")
    version("4.22", sha256="d8f611f384edbd240006d8c0f56135e74199ab88e9416cfc78cf5472f1ff337d", url="https://pypi.org/packages/9b/53/7a2369db28d557392c02990e9ce0a676aec7990aca55b19da5d9b461a43c/Pyro4-4.22.tar.gz")
    version("4.21", sha256="96bc4bdccab27d935a44f1d9a8df94986d4b3361f5ff9382e86300ed5b9fdfa2", url="https://pypi.org/packages/a6/28/c8500b2369d0946907b0c5fa5c38ea8bc4b43bda1f66ee93303dd41f8ba0/Pyro4-4.21.tar.gz")
    version("4.20", sha256="72d3fb6dc653e6ae36bd47f2667fbff3c587c72f8bfb3f0dcb1763ee86c906f8", url="https://pypi.org/packages/d3/88/6923fe1502d9a81ad48fca72490fa0209f769ebf306d5ff0f5e39a4fa6d9/Pyro4-4.20.tar.gz")
    version("4.18", sha256="52d7f6e10c44475052ac8b6828ed6f8b728a1c5d7e674b441eb0e930029ea4cd", url="https://pypi.org/packages/36/ab/c56bc34e4a30e8db84bc70949fe9383adf8adb5f69ef21dc57b28510f4ba/Pyro4-4.18.tar.gz")
    version("4.17", sha256="1d0cecdd3340dca695d6f833830e7a59f937d4bedbcff53109abe66e5a65d22c", url="https://pypi.org/packages/bf/a2/8a8fe53aa9f4e1785700c8f8aac7eb36a68eb2688789ff22251b61387a80/Pyro4-4.17.tar.gz")
    version("4.16", sha256="6a996700b877d268b48f91f91e356d2a4b20cb12207c05943d04504f6a0de0c7", url="https://pypi.org/packages/e2/66/26278136856474b228d5af76cf73ded1703fcb182b3be14ba92dd219bec8/Pyro4-4.16.tar.gz")
    version("4.15", sha256="7b9dc43d6be79e4e542b8520715cb3ab7f9095afccc93bce9cacc271c665bf7d", url="https://pypi.org/packages/4f/03/a341f154f3a68b3f4e0526040227df8cf1d3b53fcefe4d1cc906fd7b4a73/Pyro4-4.15.tar.gz")
    version("4.14", sha256="90c4f84ae9932d66825c61af9cd67b0b2877b477c967812a5d6953d67f3b003d", url="https://pypi.org/packages/01/eb/2d19e3c631e383b0a04c7d4c1257be7dc4ed20e698f8501e6dda819d70e5/Pyro4-4.14.tar.gz")
    version("4.13", sha256="afbc6964e593e7efed3fa5c91af45c4491cfdb994e7fdbe285cbb3719162cb90", url="https://pypi.org/packages/0c/4c/31a190e64f86be08953e6128be11a490e501cc56502c50230f1cf909c578/Pyro4-4.13.tar.gz")
    version("4.12", sha256="69f1beeafbe8f27bdac18e29ce97dd63cc1bdf847ff221ed0a6f0042047fa237", url="https://pypi.org/packages/34/82/a28f036b1b78556e918611d4b8fc2f429db1477a2ac7070a8b713f5d164f/Pyro4-4.12.tar.gz")
    version("4.11", sha256="d84ccfe85b14b3cb086f98d70dbf05671d6cb8498bd6f20f0041d6010dd320da", url="https://pypi.org/packages/19/27/1a85daef299b0c94df229f8208d0a2779ac16736bc2dac98599b333c9489/Pyro4-4.11.tar.gz")
    version("4.10", sha256="de74e5e020a8a26cd357f5917afb48f7e14e161ca58574a1c653441bdbe9711c", url="https://pypi.org/packages/f4/cf/aeb79f29f6b29e6c5998d967c79914c5be9f1b78cc223b8687a500f8069f/Pyro4-4.10.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-serpent@1.27:", when="@4.74,4.78:")
    # END DEPENDENCIES

