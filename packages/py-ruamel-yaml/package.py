# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyRuamelYaml(PythonPackage):
    # BEGIN VERSIONS
    version("0.18.6", sha256="57b53ba33def16c4f3d807c0ccbc00f8a6081827e81ba2491691b76882d0c636", url="https://pypi.org/packages/73/67/8ece580cc363331d9a53055130f86b096bf16e38156e33b1d3014fffda6b/ruamel.yaml-0.18.6-py3-none-any.whl")
    version("0.18.5", sha256="a013ac02f99a69cdd6277d9664689eb1acba07069f912823177c5eced21a6ada", url="https://pypi.org/packages/57/db/4b74a29f5fd175aea3ff0d95f8230d9bb8a54e38d963c6f96065b9e2eef3/ruamel.yaml-0.18.5-py3-none-any.whl")
    version("0.18.4", sha256="ca864776af7b0cbcbb223c38707a440bfabea926ba5b4163b2ef4991aae8f8c1", url="https://pypi.org/packages/cc/8b/11eb402856052429aab4e8d4a3866dd9c84dfeedacd8ae6e78bf8307d095/ruamel.yaml-0.18.4-py3-none-any.whl")
    version("0.18.3", sha256="b5d119e1f9678cf90b58f64bbd2a4e78af76860ae39fab3e73323e622b462df9", url="https://pypi.org/packages/4b/5d/678d7d15071816cb9a5e015fcd090ddc59a6a195ce8965363313e2044595/ruamel.yaml-0.18.3-py3-none-any.whl")
    version("0.18.2", sha256="92076ac8a83dbf44ca661dbed3c935229c8cbc2f10b05959dd3bd5292d8353d3", url="https://pypi.org/packages/5f/97/561b9c14816a9b07d08c7c6de7ab72283929870f5e3454f2d8e811054ef2/ruamel.yaml-0.18.2-py3-none-any.whl")
    version("0.18.1", sha256="93907ef6c731ec1bcb41ab7ff99413945f5acfd7eee27785f2cb18b175dd5aae", url="https://pypi.org/packages/05/e8/bb98ff17311e1e8f3e4149a7298274ec2645437bab936775b02c6646b672/ruamel.yaml-0.18.1-py3-none-any.whl")
    version("0.18.0", sha256="d7d31553fa2ce9628d25f02f20d2fe60d02d01e326cd140f735642cd5eebb8c9", url="https://pypi.org/packages/11/58/3863723ae81d9c1d2cc8fdd6917bf3a854106faa0df817f83f70cc6cfbf6/ruamel.yaml-0.18.0-py3-none-any.whl")
    version("0.17.40", sha256="b16b6c3816dff0a93dca12acf5e70afd089fa5acb80604afd1ffa8b465b7722c", url="https://pypi.org/packages/35/79/5e2cffa1c77432f11cd93a5351f30732c997a239d3a3090856a72d6d8ba7/ruamel.yaml-0.17.40-py3-none-any.whl")
    version("0.17.39", sha256="8df81a51384f2e6af73d88bede63ec437df4854a5a74841f40e7622471298457", url="https://pypi.org/packages/77/f1/ac2c96880bd498ff7ea9898b137e784517d11977353a5eee85e59f4e14ac/ruamel.yaml-0.17.39-py3-none-any.whl")
    version("0.17.38", sha256="c29d92cd41897d3a4d74c69e5014955c08f8e7aef49fb35c2215993db057c0e0", url="https://pypi.org/packages/1f/cb/415b5ff8179a342aa87941f651d4571494560e7a67fb286243512f29d644/ruamel.yaml-0.17.38-py3-none-any.whl")
    version("0.17.36", sha256="9d0a8ae7050ce0065bab51d4f0b000aa8afa91e8e04d1364bc304491f4f25943", url="https://pypi.org/packages/c3/06/20feed488ef1551074657d334cafd8aa094f7f1a6ae9d70df13c76bf5491/ruamel.yaml-0.17.36-py3-none-any.whl")
    version("0.17.35", sha256="b105e3e6fc15b41fdb201ba1b95162ae566a4ef792b9f884c46b4ccc5513a87a", url="https://pypi.org/packages/79/a9/ae2f346226fcec5beb172ae3cab6d47ae0baa986f1ed1bdf08d96b469b27/ruamel.yaml-0.17.35-py3-none-any.whl")
    version("0.17.34", sha256="cde36dc1683b4f60f18c27ca94fc60c03e47003bac7910a78e00a639a4f282bd", url="https://pypi.org/packages/c7/b2/014cafac3adc5b7a815e9bd975b440517f3434b18b9898fde11d709b0663/ruamel.yaml-0.17.34-py3-none-any.whl")
    version("0.17.33", sha256="2080c7a02b8a30fb3c06727cdf3e254a64055eedf3aa2d17c2b669639c04971b", url="https://pypi.org/packages/45/29/061265cf2fdcead209b62779be813d2af935e0c47e6339ac9ee53c023312/ruamel.yaml-0.17.33-py3-none-any.whl")
    version("0.17.32", sha256="23cd2ed620231677564646b0c6a89d138b6822a0d78656df7abda5879ec4f447", url="https://pypi.org/packages/d9/0e/2a05efa11ea33513fbdf4a2e2576fe94fd8fa5ad226dbb9c660886390974/ruamel.yaml-0.17.32-py3-none-any.whl")
    version("0.17.31", sha256="3cf153f0047ced526e723097ac615d3009371779432e304dbd5596b6f3a4c777", url="https://pypi.org/packages/9c/9c/e69fc06169ac6e757c66004885e0dfcc6c2b5c1a331a5dc70b890b6b4bf8/ruamel.yaml-0.17.31-py3-none-any.whl")
    version("0.17.30", sha256="b73821c1e0a9daa459e215db7c4d6d23d7159fb61c4c536653a2b4fb5b8d08a7", url="https://pypi.org/packages/61/17/bcad9c68318846d5c8a54b6f02f2b59f97f150f25e3e590616fa7795d360/ruamel.yaml-0.17.30-py3-none-any.whl")
    version("0.17.26", sha256="25d0ee82a0a9a6f44683dcf8c282340def4074a4562f3a24f55695bb254c1693", url="https://pypi.org/packages/23/33/dbc62343de0cf92e0f9c15bc0a287bdaea0953f1cadca0480c78d5ac6641/ruamel.yaml-0.17.26-py3-none-any.whl")
    version("0.17.25", sha256="8c8ea14ac57b7728785861129343f8d797145e4a422d91ef7a3dfc86ae646ff2", url="https://pypi.org/packages/46/e2/22497ec8874435e6b99da2d2a396e4fb8b281e6c15cf79e6f45ab7304c6a/ruamel.yaml-0.17.25-py3-none-any.whl")
    version("0.17.24", sha256="f251bd9096207af604af69d6495c3c650a3338d0493d27b04bc55477d7a884ed", url="https://pypi.org/packages/8d/7b/a7bfb158635d6849244daafc268fe2576c70d0fe6b38d890a8638a968ab7/ruamel.yaml-0.17.24-py3-none-any.whl")
    version("0.17.23", sha256="605510839d5af3ae730f3ed6408b7004c83f97aa2b732f6f366da7c2fc2f0d9c", url="https://pypi.org/packages/62/c6/2489d768c89ec1ec46afa385c6e33e3902ebe3f19c2f10599e22d704b353/ruamel.yaml-0.17.23-py3-none-any.whl")
    version("0.17.22", sha256="b4c6e66d103d8af198aa6139580ab735169be4922eb4c515ac121bdabf6f9361", url="https://pypi.org/packages/ef/06/608d619f65477e8a4e87077bd27f20685fd96d6a6cdf3ad2920e1d7c968c/ruamel.yaml-0.17.22-py3-none-any.whl")
    version("0.17.21", sha256="742b35d3d665023981bd6d16b3d24248ce5df75fdb4e2924e93a05c1f8b61ca7", url="https://pypi.org/packages/9e/cb/938214ac358fbef7058343b3765c79a1b7ed0c366f7f992ce7ff38335652/ruamel.yaml-0.17.21-py3-none-any.whl")
    version("0.17.20", sha256="810eef9c46523a3f77479c66267a4708255ebe806a2d540078408c2227f011af", url="https://pypi.org/packages/cb/30/2d76730ade03303d1c4deb0742a4fbe374e072a4eeb9e1d08f5140f7ddd2/ruamel.yaml-0.17.20-py3-none-any.whl")
    version("0.17.19", sha256="92ac00b312c9a83ff3253a8f7b86dfe6f9996b4082b103af84b8df99175945bc", url="https://pypi.org/packages/a6/d6/2af44d0b3c8b87573403308a8b28ca3645a843c194aa3c68f22ca3b245e9/ruamel.yaml-0.17.19-py3-none-any.whl")
    version("0.17.18", sha256="9c648677803a2e9570c1116d15ba4fd89198c8966171868044bee2181cae8ab3", url="https://pypi.org/packages/16/d2/6cb023c49feded1fed0b0a494424fa328f1f81c14898e0dd5b17d8d67cd7/ruamel.yaml-0.17.18-py3-none-any.whl")
    version("0.17.17", sha256="9af3ec5d7f8065582f3aa841305465025d0afd26c5fb54e15b964e11838fc74f", url="https://pypi.org/packages/c7/75/729b63cd0de2316c8bb789ff2c557d9732a5aeb900c5539ae74db41ba562/ruamel.yaml-0.17.17-py3-none-any.whl")
    version("0.17.16", sha256="ea21da1198c4b41b8e7a259301cc9710d3b972bf8ba52f06218478e6802dd1f1", url="https://pypi.org/packages/d3/cc/248dfb697bb98152c187ced584e505124ed952529d7f8e74b28f6f4d6f31/ruamel.yaml-0.17.16-py3-none-any.whl")
    version("0.17.15", sha256="c61a0d2d01a64094f0843e2721968e5ee2de93fc220ab6eeae2d1bd121e6e2b3", url="https://pypi.org/packages/12/f6/9ed9325e80398219ffda9316f33c7822249f757e655135d61950a3b2f978/ruamel.yaml-0.17.15-py3-none-any.whl")
    version("0.17.14", sha256="b59c548ba6a2a99a97a842db2321c5adf28470d1decb04bdd82ce9535936a2fa", url="https://pypi.org/packages/a8/d2/11bb5a7a3681f3a7530301d5f1224c678be15a6d587e16b0848b2f65552e/ruamel.yaml-0.17.14-py3-none-any.whl")
    version("0.17.13", sha256="aa1a5b8041bab0d0e8c514949fa8e11b02653061dcbc68365c820b263f8c6ec7", url="https://pypi.org/packages/28/17/8d9c99ab24ab7ca4259e3bff3e53a886387fdc11314fdc17bec15bbdeb17/ruamel.yaml-0.17.13-py3-none-any.whl")
    version("0.17.12", sha256="a54b3ec886c69367bcfd0e8c5b20a5821f49f603f76498ab207e416e8afe56eb", url="https://pypi.org/packages/16/50/c4793402da0d17760799a1076c2dd782958d3e768ed561e1e76844009933/ruamel.yaml-0.17.12-py3-none-any.whl")
    version("0.17.11", sha256="505d0c2d7d0ccc2b68eca0e23fb78a86504c2a7e95ec5f2ccb216557c380e152", url="https://pypi.org/packages/98/ae/2644cb875f505b1b35b1963b756201c85f1c75ed363380a156ddd946b5da/ruamel.yaml-0.17.11-py3-none-any.whl")
    version("0.17.10", sha256="ffb9b703853e9e8b7861606dfdab1026cf02505bade0653d1880f4b2db47f815", url="https://pypi.org/packages/0e/57/19361b93542a1bb071fe8b7dd5ae792de6e8ab86c707aa2c44db08c60b99/ruamel.yaml-0.17.10-py3-none-any.whl")
    version("0.17.9", sha256="8873a6f5516e0d848c92418b0b006519c0566b6cd0dcee7deb9bf399e2bd204f", url="https://pypi.org/packages/74/c6/0aa1aaaa56c9d320f19d9ca3f8304bc6ace8fab95932b1602cbe091ae4a3/ruamel.yaml-0.17.9-py3-none-any.whl")
    version("0.17.8", sha256="d0019c37eb4a5faac9573ad913266825cd818e4a8529acef0ad927d1e4c0437c", url="https://pypi.org/packages/f4/0b/3bf98cdeffcc3dd642d21206cc45153addb7658cb4ed830d4b1d90b27e16/ruamel.yaml-0.17.8-py3-none-any.whl")
    version("0.16.10", sha256="0962fd7999e064c4865f96fb1e23079075f4a2a14849bcdc5cdba53a24f9759b", url="https://pypi.org/packages/a6/92/59af3e38227b9cc14520bf1e59516d99ceca53e3b8448094248171e9432b/ruamel.yaml-0.16.10-py2.py3-none-any.whl")
    version("0.16.5", sha256="0db639b1b2742dae666c6fc009b8d1931ef15c9276ef31c0673cc6dcf766cf40", url="https://pypi.org/packages/fa/90/ecff85a2e9c497e2fa7142496e10233556b5137db5bd46f3f3b006935ca8/ruamel.yaml-0.16.5-py2.py3-none-any.whl")
    version("0.11.7", sha256="c89363e16c9eafb9354e55d757723efeff8682d05e56b0881450002ffb00a344", url="https://pypi.org/packages/f0/85/36931437a58010067837946bd31823072c827657e1a3c50ba5f4848163d4/ruamel.yaml-0.11.7.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-ruamel-yaml-clib@0.2.7:", when="@0.17.34: ^python@:3.12")
        depends_on("py-ruamel-yaml-clib@0.2.7:", when="@0.17.23:0.17.33 ^python@:3.11")
        depends_on("py-ruamel-yaml-clib@0.2.6:", when="@0.17.18:0.17.22 ^python@:3.10")
        depends_on("py-ruamel-yaml-clib@0.1.2:", when="@0.16.13:0.17.17 ^python@:3.9")
        depends_on("py-ruamel-yaml-clib@0.1.2:", when="@0.16.11:0.16.12 ^python@:3.8")
    # END DEPENDENCIES

