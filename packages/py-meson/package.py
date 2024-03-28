# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyMeson(PythonPackage):
    # BEGIN VERSIONS
    version("1.4.0", sha256="476a458d51fcfa322a6bdc64da5138997c542d08e6b2e49b9fa68c46fd7c4475", url="https://pypi.org/packages/33/75/b1a37fa7b2dbca8c0dbb04d5cdd7e2720c8ef6febe41b4a74866350e041c/meson-1.4.0-py3-none-any.whl")
    version("1.4.0-rc2", sha256="204444cc4a2d86606d028215ae2e9b2087874f3f64a147ec92a4d2564635447e", url="https://pypi.org/packages/70/fa/69564edd377b7a855820eaf4081e3fada8462bf372ca41e9b5e6a1f83cfa/meson-1.4.0rc2-py3-none-any.whl")
    version("1.4.0-rc1", sha256="bcae6bc400c3add0530110da09c49dfd27a3a48087ecb5aa4ba1f75e3339daa9", url="https://pypi.org/packages/60/63/9c7856d213b34af92b375c46e67a498d167d39982160417ec7b92483da98/meson-1.4.0rc1-py3-none-any.whl")
    version("1.3.2", sha256="0ba4a71fbc060c44721c7b674807598c5af9ea51335073cae7a3e9a95b375c89", url="https://pypi.org/packages/39/7c/ff115bec047c5127567048db40818b83b47fd0d3bfcfd0d87630d44ed66f/meson-1.3.2-py3-none-any.whl")
    version("1.3.1", sha256="d5223ecca9564d735d36daaba2571abc6c032c8c3a7ffa0674e803ef0c7e0219", url="https://pypi.org/packages/53/37/bb38e78b36cb923c65fd70b3027406e9667b2ff31f054584ab23282c07f6/meson-1.3.1-py3-none-any.whl")
    version("1.3.0", sha256="e9f54046ce5b9a1f3024f7a7d52f19f085fd57c9d26a5db0cfcf0750572a8fd8", url="https://pypi.org/packages/f8/af/e6f06610fcb778e1935d0648c7a42baeb1f51756b3849951a82c40a6193b/meson-1.3.0-py3-none-any.whl")
    version("1.3.0-rc3", sha256="dca4a94fe6f095a9a8db7f31bd9df9a66c0481ba5cc4d5532a4c8bb08040bfbe", url="https://pypi.org/packages/34/f2/55f4d1200a7deca8a1d64600cc8e68c3173e0c2229b6004a30f8f746ea06/meson-1.3.0rc3-py3-none-any.whl")
    version("1.3.0-rc2", sha256="0240fcb71e6cc2e319d6bb475bd70cb6ce46e2448a75bf0825fc2d0ec3abf92f", url="https://pypi.org/packages/50/dc/c0dd4a253286d131b7eaf1bdaffb5ff5518f3aede50bcaba547c4002b1a8/meson-1.3.0rc2-py3-none-any.whl")
    version("1.3.0-rc1", sha256="194883d5f7a17162a18f1583c57301c440d85025863576d7f1baa8a6e8cd7384", url="https://pypi.org/packages/b3/fe/9c30551def432acb21e5ec4f0b3f29868d9638c5dc115295f2ae0c5a217b/meson-1.3.0rc1.tar.gz")
    version("1.2.3", sha256="17d9124ffad38f5bbb6b198a8de5ecc55ebcd164d35a1d9dae06b8de0605a252", url="https://pypi.org/packages/b0/74/73a0d5264f04c9193d2d588400ae913a167911b4342320cbdde3040b753d/meson-1.2.3-py3-none-any.whl")
    version("1.2.2", sha256="6d0f9cb45aaf70bc032ecb894d5e22a512224b778837bc7e052588c7ce87571d", url="https://pypi.org/packages/4b/62/602e91c1da05abf88d86dbc89e05e09665cf06f42ccebca67401bbce90fe/meson-1.2.2-py3-none-any.whl")
    version("1.2.1", sha256="08f83fc17513e99cd6e82c7554c1f58af70425211887f8f9c7363b2a90209462", url="https://pypi.org/packages/e5/74/a1f1c6ba14e11e0fb050d2c61a78b6db108dd38383b6c0ab51c1becbbeff/meson-1.2.1-py3-none-any.whl")
    version("1.2.0", sha256="10c0364edc67a1b3146f405800b300f0535f42b8736e79c744a8029a855b7c6b", url="https://pypi.org/packages/ae/33/6f4a76e7139cffc2e3d4bab02824875c842922c0689438fc25092d85aecd/meson-1.2.0-py3-none-any.whl")
    version("1.1.1", sha256="1c5a46660dfbe5f45ef7588d78429d04ebdb6f84b96b4b015033572d2facbbe5", url="https://pypi.org/packages/ce/55/52776f722af3db59e1f15b15934d736c3dca31b4964a78fe8fdddf06ec57/meson-1.1.1-py3-none-any.whl")
    version("1.1.0", sha256="f7e17450a00c2c2366e5f2ad605a4bf7328961b7455ace1b00ea0c4375fdb252", url="https://pypi.org/packages/f4/70/c784cd848995cedeaafa4f160e6d6da13f93fd770bb1805c9fba31c7374b/meson-1.1.0-py3-none-any.whl")
    version("1.0.2", sha256="ed50351d24d4d62fcc895a8980d8db429aee3c392aa93a2f449c6c77e9867104", url="https://pypi.org/packages/65/0d/27a9e5fa632906fbfac4228f87058b8b80654ae07ebb667b8a4347403754/meson-1.0.2-py3-none-any.whl")
    version("1.0.1", sha256="98d6158c71e34dfd32c77014109003304eeda1c7e24b8e2448261dcd9d95f968", url="https://pypi.org/packages/4f/54/0e79b014d6389cba46cfd15a27e178d1bd82559142a2c66eb43b1afa8d61/meson-1.0.1-py3-none-any.whl")
    version("1.0.0", sha256="501b2d7bb7d47a44a221369eeb12b5e6aadbdc8b267ff57de32b25e9202a7d94", url="https://pypi.org/packages/2b/8c/694a2dda825ae6157fe0780bf4fbb1fc780cb7905bca7a8d0db87e0f50bc/meson-1.0.0-py3-none-any.whl")
    version("0.64.1", sha256="8cf376d3b8640d8957d335eb4b61f2e30412c4aea3fa2affe72ae4c98145d51d", url="https://pypi.org/packages/87/e6/a2f56e3fc1433a2530862d65e8a93b9dbd7461186752d4d3a6295325a7ed/meson-0.64.1-py3-none-any.whl")
    version("0.64.0", sha256="556226cc3c279416fa59169b715cbc89d47fdd768d4c58e62d5dbc458cd298f5", url="https://pypi.org/packages/bd/9c/c1669f9d4f0765e497dba04648ee0c4a15995a69d9920945e7f3ee613ac9/meson-0.64.0-py3-none-any.whl")
    version("0.63.3", sha256="d677b809c4895dcbaac9bf6c43703fcb3609a4b24c6057c78f828590049cf43a", url="https://pypi.org/packages/df/1d/fba853811ed15a7196e839e6c1a45cd623dc2e1eb36750a55094b8c92e63/meson-0.63.3-py3-none-any.whl")
    version("0.63.2", sha256="64a83ef257b2962b52c8b07ad9ec536c2de1b72fd9f14bcd9c21fe45730edd46", url="https://pypi.org/packages/11/9e/a4730ddfdc5634a7f135c290d52a2f8e3f4dc49756cf53dd78fc6a8b03b2/meson-0.63.2-py3-none-any.whl")
    version("0.63.1", sha256="b90d3ff3ba5ce4d192a7441f288966d904b7ddb9cb20fe0c8929e871aef6a638", url="https://pypi.org/packages/27/c5/89b95f014f0c10fa5d79e7b4b795c31509d4c270d37c9b12056b1504d74e/meson-0.63.1-py3-none-any.whl")
    version("0.62.2", sha256="c245d2b39e1ce1d1968e0b7067771fd02ca1bade1990adb3cf4088375ba188c9", url="https://pypi.org/packages/19/88/7828cd8edfa840363a1d52d0c61eecf57dabd6e84732edb0f8f2b1defb93/meson-0.62.2-py3-none-any.whl")
    version("0.62.1", sha256="e901c0d5d49bd42fb9b90a55900f7cbdf80b0bbc498a235b8293682cf6d71a7b", url="https://pypi.org/packages/f4/64/eea064f91d176762499111a6109dc0fdbca2b1ac5a2d4147fd8c1b4edcd9/meson-0.62.1-py3-none-any.whl")
    version("0.62.0", sha256="00e06dccac7d3b0568b5da82e70c2028c80c359aab6dc517bcbd1825511898c3", url="https://pypi.org/packages/fb/0d/1acf7e1a3a5aeb0b2e94f08222939b8aadff97607de2971cc1d6458a267a/meson-0.62.0-py3-none-any.whl")
    version("0.61.4", sha256="b3048be6e6bcf9ace1433a6799e885b54651cf10ab7aee582eb09720ef83c2dc", url="https://pypi.org/packages/95/0a/c961c525cd1b2914fa9cc85692f25a44012759ca1f25a96bda3fec74aa09/meson-0.61.4-py3-none-any.whl")
    version("0.61.2", sha256="2e2d71c4d8e47624cc9fdff6de92915b3e143fc800cc44ccedd2a88362ebe4dd", url="https://pypi.org/packages/77/04/8de56b69d805406bf8c1d73934938680cec9d417fa39b4a68833729505a5/meson-0.61.2-py3-none-any.whl")
    version("0.60.3", sha256="b74083e2d8608f5a499827b09e1692f31fc4be0370841439379f413c75f4b438", url="https://pypi.org/packages/f1/a9/7e0d0f0dd334c5f02a99f386a0b3bf2b2d657a59d9c4c60ae4e475fcc5f0/meson-0.60.3-py3-none-any.whl")
    version("0.60.0", sha256="40cc2426b482c8b0d7931a2ed69aaf85caf1ae7653d0435e82e39c5867cfa28c", url="https://pypi.org/packages/05/7e/ef9b8dfce67619b53519564dc0fcdffc76be228efdd9395964f1d45ac911/meson-0.60.0-py3-none-any.whl")
    version("0.59.2", sha256="13dee549a7ba758b7e33ce7719f28d1d337a98d10d378a4779ccc996f5a2fc49", url="https://pypi.org/packages/32/a2/b31eb5fe8d75e29b9b271404f50fe46eae5b143794105d0ae2371e7e93d5/meson-0.59.2.tar.gz")
    version("0.59.1", sha256="db586a451650d46bbe10984a87b79d9bcdc1caebf38d8e189f8848f8d502356d", url="https://pypi.org/packages/dd/01/3dba211a922c371044baa3ade48f3021e9b67e83c07b397f8eeeea99d3a6/meson-0.59.1.tar.gz")
    version("0.59.0", sha256="e376c298df64b643dfe01eccb2d7b6f1e02e95aa38c19f19d120d129612ce476", url="https://pypi.org/packages/63/2d/a030b1b53166776890883a521220433959e315c83ed975846b5484f43c7c/meson-0.59.0.tar.gz")
    version("0.58.2", sha256="7634ec32955d3f897d623b88e9d2988451035f43d73c17a29caf767387baedb7", url="https://pypi.org/packages/df/bf/cc6e8a31958b6f3ad2766517b091a92142076104b8b0d8d4abeb0dc53222/meson-0.58.2.tar.gz")
    version("0.58.1", sha256="3144a3da662fcf79f1e5602fa929f2821cba4eba28c2c923fe0a7d3e3db04d5d", url="https://pypi.org/packages/e6/e4/11fc433adb18567dcf90041c54e5e65b03e9451bc1a45f9cd2dac9e9bb05/meson-0.58.1.tar.gz")
    version("0.58.0", sha256="f4820df0bc969c99019fd4af8ca5f136ee94c63d8a5ad67e7eb73bdbc9182fdd", url="https://pypi.org/packages/66/0c/6e600a3dfdaca5d0e7455c1355472f09994d3c5a1466554ba0ea40affe1a/meson-0.58.0.tar.gz")
    version("0.57.2", sha256="3a83e7b1c5de94fa991ec34d9b198d94f38ed699d3524cb0fdf3b99fd23d4cc5", url="https://pypi.org/packages/5d/0e/0c72dadd01af2da712eb987e2b7662e2e2c2c34fcdfe3cc6d765bddb2db3/meson-0.57.2.tar.gz")
    version("0.57.1", sha256="72e1c782ba9bda204f4a1ed57f98d027d7b6eb9414c723eebbd6ec7f1955c8a6", url="https://pypi.org/packages/0f/f8/e67e447cb3c8fe391ad8cedd67cab81486831e37a3a028c9a6974fe63a38/meson-0.57.1.tar.gz")
    version("0.57.0", sha256="7ccb75fe1a4d404bcab86e72678abc7f75793401aa9054f881a4eb3cb990f5d9", url="https://pypi.org/packages/07/9e/fcdaaaf4f27394e9ee1be666b68ccd01d26fb741ffcef35e5bc7a905c7dc/meson-0.57.0.tar.gz")
    version("0.56.2", sha256="3cb8bdb91383f7f8da642f916e4c44066a29262caa499341e2880f010edb87f4", url="https://pypi.org/packages/b6/0a/9ae8a4d83263eee8f7357447f1e14f0e39b04a4994aa9884b7e14a91f530/meson-0.56.2.tar.gz")
    version("0.56.0", sha256="291dd38ff1cd55fcfca8fc985181dd39be0d3e5826e5f0013bf867be40117213", url="https://pypi.org/packages/08/a0/4d3a1eb46c83a96b49c100c30762c8f1a60b62367dd052ab8730e73ab46b/meson-0.56.0.tar.gz")
    version("0.55.3", sha256="6bed2a25a128bbabe97cf40f63165ebe800e4fcb46db8ab7ef5c2b5789f092a5", url="https://pypi.org/packages/5e/da/e6f22f0d3730635aa8504cc0d7ae16406b3794bbfea04c854e2c215c7acb/meson-0.55.3.tar.gz")
    version("0.55.2", sha256="78a3f4ee3864a8fce9f028d38d900ef997fd398b851765e35a0185e5c01b11f7", url="https://pypi.org/packages/19/44/40014da9bcfc4704e88b0e946a2bcb3836d1514da6844292e4f373479006/meson-0.55.2.tar.gz")
    version("0.55.1", sha256="3b5741f884e04928bdfa1947467ff06afa6c98e623c25cef75adf71ca39ce080", url="https://pypi.org/packages/33/fa/79ee2dedf921e5573b8fbf2cfb120d86d12097a446d3f59fc1d71ca0362a/meson-0.55.1.tar.gz")
    version("0.55.0", sha256="0a1ae2bfe2ae14ac47593537f93290fb79e9b775c55b4c53c282bc3ca3745b35", url="https://pypi.org/packages/44/05/8ac9e7747e5cdf817c2916cc15980374ef04cb2ecf4f6818392928c61923/meson-0.55.0.tar.gz")
    version("0.54.3", sha256="f2bdf4cf0694e696b48261cdd14380fb1d0fe33d24744d8b2df0c12f33ebb662", url="https://pypi.org/packages/04/db/53fe14aa9a45e34b76e58f4b479276eb8dd0591552f941a4aea28cd3d760/meson-0.54.3.tar.gz")
    version("0.54.2", sha256="a7716eeae8f8dff002e4147642589ab6496ff839e4376a5aed761f83c1fa0455", url="https://pypi.org/packages/78/14/53d77eeb196efb1230eedaba556c920fc59989f1ebd429e990cb129b41d3/meson-0.54.2.tar.gz")
    version("0.54.1", sha256="2f76fb4572762be13ee479292610091b4509af5788bcceb391fe222bcd0296dc", url="https://pypi.org/packages/cc/d5/81df16955431a2a0bb73587e913c7ec23a6ad665ad16499af88b7b743f6d/meson-0.54.1.tar.gz")
    version("0.54.0", sha256="dde5726d778112acbd4a67bb3633ab2ee75d33d1e879a6283a7b4a44c3363c27", url="https://pypi.org/packages/4f/6a/79cc8a3bbb5baacbb39f6bd958f55dd4e6fbb25a776fbe9d0048aa2c106b/meson-0.54.0.tar.gz")
    version("0.53.2", sha256="3e8f830f33184397c2eb0b651ec502adb63decb28978bdc84b3558d71284c21f", url="https://pypi.org/packages/49/d7/38a71de6adaa7a25a72587e69429ce78e137f4d545c7516341aa081f43e7/meson-0.53.2.tar.gz")
    version("0.49.1", sha256="1a944b01de151c2d19594c652e484b0c04628afca974fc1713182b84ec249917", url="https://pypi.org/packages/3d/df/9a86a979a870627c4264ee2b9305d58b49da85d371c6afe95c8ae9b8690e/meson-0.49.1.tar.gz")
    version("0.49.0", sha256="a0cd55372208730eca5cd7cdff7948e439a006d8587c50c4445be1a0e88b2521", url="https://pypi.org/packages/b6/22/55d0b08695abf2f425e7b4130b37f6202ca5e37c93dca7512f2ee2b8f4f4/meson-0.49.0.tar.gz")
    version("0.42.0", sha256="4ef46250beea2af272a2ab5bdf835dd06e8c8d341c18529d502b5f7be0ac73fe", url="https://pypi.org/packages/10/44/0899bf05d79a90a345252c38172d5359672119bc6125fe491a8263f173d1/meson-0.42.0.tar.gz")
    version("0.41.2", sha256="ad1707717987fe8b7b65392b8327580105fcbdd5f2032bf3b7232b647284c95c", url="https://pypi.org/packages/6d/32/a474702fcba1144aef89e7ec5d8a33d49be8389a0f983d11aab486c8392b/meson-0.41.2.tar.gz")
    version("0.41.1", sha256="df57b79494a310d02791e3b24527536c0bcfcf8df32b30a6e4b4e071ec94ddb4", url="https://pypi.org/packages/2f/71/67c0ef454aa958cac484b1a0b9eba4c976083acbe5fdd281676eb79fc8ce/meson-0.41.1.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    # END DEPENDENCIES

