# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyCryptography(PythonPackage):
    # BEGIN VERSIONS
    version("42.0.5", sha256="6fe07eec95dfd477eb9530aef5bead34fec819b3aaf6c5bd6d20565da607bfe1", url="https://pypi.org/packages/13/9e/a55763a32d340d7b06d045753c186b690e7d88780cafce5f88cb931536be/cryptography-42.0.5.tar.gz")
    version("42.0.4", sha256="831a4b37accef30cccd34fcb916a5d7b5be3cbbe27268a02832c3e450aea39cb", url="https://pypi.org/packages/81/d8/214d25515bf6034dce99aba22eeb47443b14c82160114e3d3f33067c6d3b/cryptography-42.0.4.tar.gz")
    version("42.0.3", sha256="069d2ce9be5526a44093a0991c450fe9906cdf069e0e7cd67d9dee49a62b9ebe", url="https://pypi.org/packages/b3/cc/988dee9e00be594cb1e20fd0eb83facda0c229fdef4cd7746742ecd44371/cryptography-42.0.3.tar.gz")
    version("42.0.2", sha256="e0ec52ba3c7f1b7d813cd52649a5b3ef1fc0d433219dc8c93827c57eab6cf888", url="https://pypi.org/packages/0f/6f/40f1b5c6bafc809dd21a9e577458ecc1d8062a7e10148d140f402b535eaa/cryptography-42.0.2.tar.gz")
    version("42.0.1", sha256="fd33f53809bb363cf126bebe7a99d97735988d9b0131a2be59fbf83e1259a5b7", url="https://pypi.org/packages/3f/ed/a233522ab5201b988a482cbb19ae3b63bef8ad2ad3e11fc5216b7053b2e4/cryptography-42.0.1.tar.gz")
    version("42.0.0", sha256="6cf9b76d6e93c62114bd19485e5cb003115c134cf9ce91f8ac924c44f8c8c3f4", url="https://pypi.org/packages/1d/95/e81ad3a9caadfc6a4367de7432fd3b779a2e2af760ce9a9cb4f5704d57ca/cryptography-42.0.0.tar.gz")
    version("41.0.7", sha256="13f93ce9bea8016c253b34afc6bd6a75993e5c40672ed5405a9c832f0d4a00bc", url="https://pypi.org/packages/ce/b3/13a12ea7edb068de0f62bac88a8ffd92cc2901881b391839851846b84a81/cryptography-41.0.7.tar.gz")
    version("41.0.6", sha256="422e3e31d63743855e43e5a6fcc8b4acab860f560f9321b0ee6269cc7ed70cc3", url="https://pypi.org/packages/4d/b4/828991d82d3f1b6f21a0f8cfa54337ed33fdb52135f694130060839cfc33/cryptography-41.0.6.tar.gz")
    version("41.0.5", sha256="392cb88b597247177172e02da6b7a63deeff1937fa6fec3bbf902ebd75d97ec7", url="https://pypi.org/packages/16/a7/38fdcdd634515f589c8c723608c0f0b38d66c6c2320b3095967486f3045a/cryptography-41.0.5.tar.gz")
    version("41.0.4", sha256="7febc3094125fc126a7f6fb1f420d0da639f3f32cb15c8ff0dc3997c4549f51a", url="https://pypi.org/packages/ef/33/87512644b788b00a250203382e40ee7040ae6fa6b4c4a31dcfeeaa26043b/cryptography-41.0.4.tar.gz")
    version("41.0.3", sha256="6d192741113ef5e30d89dcb5b956ef4e1578f304708701b8b73d38e3e1461f34", url="https://pypi.org/packages/8e/5d/2bf54672898375d081cb24b30baeb7793568ae5d958ef781349e9635d1c8/cryptography-41.0.3.tar.gz")
    version("41.0.2", sha256="7d230bf856164de164ecb615ccc14c7fc6de6906ddd5b491f3af90d3514c925c", url="https://pypi.org/packages/93/b7/b6b3420a2f027c1067f712eb3aea8653f8ca7490f183f9917879c447139b/cryptography-41.0.2.tar.gz")
    version("41.0.1", sha256="d34579085401d3f49762d2f7d6634d6b6c2ae1242202e860f4d26b046e3a1006", url="https://pypi.org/packages/19/8c/47f061de65d1571210dc46436c14a0a4c260fd0f3eaf61ce9b9d445ce12f/cryptography-41.0.1.tar.gz")
    version("41.0.0", sha256="6b71f64beeea341c9b4f963b48ee3b62d62d57ba93eb120e1196b31dc1025e78", url="https://pypi.org/packages/bf/92/3301a5d4fb734290a8bca5a9aad61ea61327ed53cb19be110d4f3548df76/cryptography-41.0.0.tar.gz")
    version("40.0.2", sha256="c33c0d32b8594fa647d2e01dbccc303478e16fdd7cf98652d5b3ed11aa5e5c99", url="https://pypi.org/packages/f7/80/04cc7637238b78f8e7354900817135c5a23cf66dfb3f3a216c6d630d6833/cryptography-40.0.2.tar.gz")
    version("40.0.1", sha256="2803f2f8b1e95f614419926c7e6f55d828afc614ca5ed61543877ae668cc3472", url="https://pypi.org/packages/15/d9/c679e9eda76bfc0d60c9d7a4084ca52d0631d9f24ef04f818012f6d1282e/cryptography-40.0.1.tar.gz")
    version("40.0.0", sha256="f421f6777592eb199ca8abac7c20b9ecef27c50ad63546e6c614b29771b46d0d", url="https://pypi.org/packages/e6/ca/c0e8aa240a95098b49369a4efe67e073e53b169506f0a40b972125c5e252/cryptography-40.0.0.tar.gz")
    version("39.0.2", sha256="bc5b871e977c8ee5a1bbc42fa8d19bcc08baf0c51cbf1586b0e87a2694dde42f", url="https://pypi.org/packages/fa/f3/f4b8c175ea9a1de650b0085858059050b7953a93d66c97ed89b93b232996/cryptography-39.0.2.tar.gz")
    version("39.0.1", sha256="d1f6198ee6d9148405e49887803907fe8962a23e6c6f83ea7d98f1c0de375695", url="https://pypi.org/packages/6a/f5/a729774d087e50fffd1438b3877a91e9281294f985bda0fd15bf99016c78/cryptography-39.0.1.tar.gz")
    version("39.0.0", sha256="f964c7dcf7802d133e8dbd1565914fa0194f9d683d82411989889ecd701e8adf", url="https://pypi.org/packages/12/e3/c46c274cf466b24e5d44df5d5cd31a31ff23e57f074a2bb30931a8c9b01a/cryptography-39.0.0.tar.gz")
    version("38.0.4", sha256="175c1a818b87c9ac80bb7377f5520b7f31b3ef2a0004e2420319beadedb67290", url="https://pypi.org/packages/e3/3f/41186b1f2fd86a542d399175f6b8e43f82cd4dfa51235a0b030a042b811a/cryptography-38.0.4.tar.gz")
    version("38.0.3", sha256="bfbe6ee19615b07a98b1d2287d6a6073f734735b49ee45b11324d85efc4d5cbd", url="https://pypi.org/packages/13/dd/a9608b7aebe5d2dc0c98a4b2090a6b815628efa46cc1c046b89d8cd25f4c/cryptography-38.0.3.tar.gz")
    version("38.0.2", sha256="7a022ec87c7a8bdad99f516a4ee6ffcb3a2bc31487577f9eccbc9b2edb1a8fd4", url="https://pypi.org/packages/63/82/a6e21842f2e31b3874f01c112093b8bf8af119f5ed999bbd667a81de720b/cryptography-38.0.2.tar.gz")
    version("38.0.1", sha256="1db3d807a14931fa317f96435695d9ec386be7b84b618cc61cfa5d08b0ae33d7", url="https://pypi.org/packages/6d/0c/5e67831007ba6cd7e52c4095f053cf45c357739b0a7c46a45ddd50049019/cryptography-38.0.1.tar.gz")
    version("38.0.0", sha256="24d4137f3118900db02a2ec9a585d6dec2e79697fc90e84f19e5462dd1eeca44", url="https://pypi.org/packages/53/e6/9a144127f3a1c1e6d9c4d305390d82a38e9e0fc7e34166c44f59a1576247/cryptography-38.0.0.tar.gz")
    version("37.0.4", sha256="63f9c17c0e2474ccbebc9302ce2f07b55b3b3fcb211ded18a42d5764f5c10a82", url="https://pypi.org/packages/89/d9/5fcd312d5cce0b4d7ee8b551a0ea99e4ea9db0fdbf6dd455a19042e3370b/cryptography-37.0.4.tar.gz")
    version("36.0.1", sha256="53e5c1dc3d7a953de055d77bef2ff607ceef7a2aac0353b5d630ab67f7423638", url="https://pypi.org/packages/f9/4b/1cf8e281f7ae4046a59e5e39dd7471d46db9f61bb564fddbff9084c4334f/cryptography-36.0.1.tar.gz")
    version("35.0.0", sha256="9933f28f70d0517686bd7de36166dda42094eac49415459d9bdf5e7df3e0086d", url="https://pypi.org/packages/10/91/90b8d4cd611ac2aa526290ae4b4285aa5ea57ee191c63c2f3d04170d7683/cryptography-35.0.0.tar.gz")
    version("3.4.8", sha256="94cc5ed4ceaefcbe5bf38c8fba6a21fc1d365bb8fb826ea1688e3370b2e24a1c", url="https://pypi.org/packages/cc/98/8a258ab4787e6f835d350639792527d2eb7946ff9fc0caca9c3f4cf5dcfe/cryptography-3.4.8.tar.gz")
    version("3.4.7", sha256="3d10de8116d25649631977cb37da6cbdd2d6fa0e0281d014a5b7d337255ca713", url="https://pypi.org/packages/9b/77/461087a514d2e8ece1c975d8216bc03f7048e6090c5166bc34115afdaa53/cryptography-3.4.7.tar.gz")
    version("3.4.6", sha256="2d32223e5b0ee02943f32b19245b61a62db83a882f0e76cc564e1cec60d48f87", url="https://pypi.org/packages/fa/2d/2154d8cb773064570f48ec0b60258a4522490fcb115a6c7c9423482ca993/cryptography-3.4.6.tar.gz")
    version("3.4.5", sha256="4f6761a82b51fe02cda8f45af1c2f698a10f50003dc9c2572d8a49eda2e6d35b", url="https://pypi.org/packages/60/6d/b32368327f600a12e59fb51a904fc6200dd7e65e953fd6fc6ae6468e3423/cryptography-3.4.5.tar.gz")
    version("3.4.4", sha256="ee5e19f0856b6fbbdbab15c2787ca65d203801d2d65d0b8de6218f424206c848", url="https://pypi.org/packages/27/5a/007acee0243186123a55423d49cbb5c15cb02d76dd1b6a27659a894b13a2/cryptography-3.4.4.tar.gz")
    version("3.4.3", sha256="d70065c42de45e15776a53216000283a2a183ae37379badb37f527a2bdfd6221", url="https://pypi.org/packages/f8/04/51dc8a4ccb37b69a4e165a94837f70653b0b6ca49a6346361062b1f6bb09/cryptography-3.4.3.tar.gz")
    version("3.4.2", sha256="c460e296c8cb3a796cdcc7d56c62a78fcd0a09409ccd9c658ace4f987ce935c4", url="https://pypi.org/packages/35/52/a3b9c3d8ce84544bfe8d663ba993e0593d9c518d6c08f01f6f8fff87b895/cryptography-3.4.2.tar.gz")
    version("3.4.1", sha256="be70bdaa29bcacf70896dae3a6f3eef91daf51bfba8a49dbfb9c23bb2cc914ba", url="https://pypi.org/packages/06/ed/cb79cc94ec58d9d92557238fc6c629cd6e07d72334d2de556aecc2211370/cryptography-3.4.1.tar.gz")
    version("3.4", sha256="9f7aa11ea95723359f914be3217d8b378bc3897f65a1ec1ab4e0118c336f51fc", url="https://pypi.org/packages/ea/d8/2afd2890fe451a3c109d2bdb6bc4ded55ec43059e524344d5e0004e36412/cryptography-3.4.tar.gz")
    version("3.3.2", sha256="5a60d3780149e13b7a6ff7ad6526b38846354d11a15e21068e57073e29e19bed", url="https://pypi.org/packages/d4/85/38715448253404186029c575d559879912eb8a1c5d16ad9f25d35f7c4f4c/cryptography-3.3.2.tar.gz")
    version("3.3.1", sha256="7e177e4bea2de937a584b13645cab32f25e3d96fc0bc4a4cf99c27dc77682be6", url="https://pypi.org/packages/b7/82/f7a4ddc1af185936c1e4fa000942ffa8fb2d98cff26b75afa7b3c63391c4/cryptography-3.3.1.tar.gz")
    version("3.2.1", sha256="d3d5e10be0cf2a12214ddee45c6bd203dab435e3d83b4560c03066eda600bfe3", url="https://pypi.org/packages/94/5c/42de91c7fbdb817b2d9a4e64b067946eb38a4eb36c1a09c96c87a0f86a82/cryptography-3.2.1.tar.gz")
    version("3.2", sha256="e4789b84f8dedf190148441f7c5bfe7244782d9cbb194a36e17b91e7d3e1cca9", url="https://pypi.org/packages/1c/15/aceb9a2535c9fa805316b49e42fde0a83d1a0492b4e3608a4a5dc9b04b46/cryptography-3.2.tar.gz")
    version("3.1.1", sha256="9d9fc6a16357965d282dd4ab6531013935425d0dc4950df2e0cf2a1b1ac1017d", url="https://pypi.org/packages/5d/4b/7bb135c5787c003cdbc44990c5f41908f0f37135e0bb554e880d90fd5f6f/cryptography-3.1.1.tar.gz")
    version("3.1", sha256="26409a473cc6278e4c90f782cd5968ebad04d3911ed1c402fc86908c17633e08", url="https://pypi.org/packages/12/be/c9cc7d7ab71dbcc9e4e517ead0cdd48e8c9a48d7b8bdddb738e90d08279a/cryptography-3.1.tar.gz")
    version("3.0", sha256="8e924dbc025206e97756e8903039662aa58aa9ba357d8e1d8fc29e3092322053", url="https://pypi.org/packages/bf/ac/552fc8729d90393845cc3a2062facf4a89dcbe206fa78771d60ddaae7554/cryptography-3.0.tar.gz")
    version("2.9.2", sha256="a0c30272fb4ddda5f5ffc1089d7405b7a71b0b0f51993cb4e5dbb4590b2fc229", url="https://pypi.org/packages/56/3b/78c6816918fdf2405d62c98e48589112669f36711e50158a0c15d804c30d/cryptography-2.9.2.tar.gz")
    version("2.9.1", sha256="ce0bd68b4b946bd4bcebc3d4d1325bf0e938e445ae18cedddd60e33dd85a368e", url="https://pypi.org/packages/f7/0b/dc724c3e1025b7b61aed8071b551286415dade6861170695293899263d68/cryptography-2.9.1.tar.gz")
    version("2.9", sha256="0cacd3ef5c604b8e5f59bf2582c076c98a37fe206b31430d0cd08138aff0986e", url="https://pypi.org/packages/9d/0a/d7060601834b1a0a84845d6ae2cd59be077aafa2133455062e47c9733024/cryptography-2.9.tar.gz")
    version("2.8", sha256="3cda1f0ed8747339bbdf71b9f38ca74c7b592f24f65cdb3ab3765e4b02871651", url="https://pypi.org/packages/be/60/da377e1bed002716fb2d5d1d1cab720f298cb33ecff7bf7adea72788e4e4/cryptography-2.8.tar.gz")
    version("2.7", sha256="e6347742ac8f35ded4a46ff835c60e68c22a536a8ae5c4422966d06946b6d4c6", url="https://pypi.org/packages/c2/95/f43d02315f4ec074219c6e3124a87eba1d2d12196c2767fadfdc07a83884/cryptography-2.7.tar.gz")
    version("2.6.1", sha256="26c821cbeb683facb966045e2064303029d572a87ee69ca5a1bf54bf55f93ca6", url="https://pypi.org/packages/07/ca/bc827c5e55918ad223d59d299fff92f3563476c3b00d0a9157d9c0217449/cryptography-2.6.1.tar.gz")
    version("2.6", sha256="41d3d15be7f297275e8b476cbd132c9d6701c5206e6c48c5946ec40ff2abb1bc", url="https://pypi.org/packages/a3/5f/d5b7d21006e3c1a3919a3cc14e2a5ce1cee1c7ff635f09b31d91bdaff377/cryptography-2.6.tar.gz")
    version("2.5", sha256="4946b67235b9d2ea7d31307be9d5ad5959d6c4a8f98f900157b47abddf698401", url="https://pypi.org/packages/69/ed/5e97b7f54237a9e4e6291b6e52173372b7fa45ca730d36ea90b790c0059a/cryptography-2.5.tar.gz")
    version("2.4.2", sha256="05a6052c6a9f17ff78ba78f8e6eb1d777d25db3b763343a1ae89a7a8670386dd", url="https://pypi.org/packages/f3/39/d3904df7c56f8654691c4ae1bdb270c1c9220d6da79bd3b1fbad91afd0e1/cryptography-2.4.2.tar.gz")
    version("2.4.1", sha256="e85b410885addaeb31a867eabcefc9ef4a7e904ad45eac9e60a763a54b244626", url="https://pypi.org/packages/d2/5f/6ed3135eb1e775187f7ecd4e7713f1415516725365e51f9786143f36e024/cryptography-2.4.1.tar.gz")
    version("2.3.1", sha256="8d10113ca826a4c29d5b85b2c4e045ffa8bad74fb525ee0eceb1d38d4c70dfd6", url="https://pypi.org/packages/22/21/233e38f74188db94e8451ef6385754a98f3cad9b59bedf3a8e8b14988be4/cryptography-2.3.1.tar.gz")
    version("1.8.1", sha256="323524312bb467565ebca7e50c8ae5e9674e544951d28a2904a50012a8828190", url="https://pypi.org/packages/ec/5f/d5bc241d06665eed93cd8d3aa7198024ce7833af7a67f6dc92df94e00588/cryptography-1.8.1.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    variant("idna", default=False)
    # END VARIANTS

    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-cffi@1.12:", when="@41.0.4:")
    # END DEPENDENCIES

