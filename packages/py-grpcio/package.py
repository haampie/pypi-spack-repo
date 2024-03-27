##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyGrpcio(PythonPackage):
    version("1.62.1", sha256="6c455e008fa86d9e9a9d85bb76da4277c0d7d9668a3bfa70dbe86e9f3c759947", url="https://pypi.org/packages/c7/bb/d01494037edee2d8e024cac8049b169b2723186b01cebb495ccf677bbba9/grpcio-1.62.1.tar.gz")
    version("1.62.0", sha256="748496af9238ac78dcd98cce65421f1adce28c3979393e3609683fcd7f3880d7", url="https://pypi.org/packages/50/4e/7ed8c24c93c8d000b9ea2927f555ae3b03cfabe035d65eda0db848cb20b6/grpcio-1.62.0.tar.gz")
    version("1.62.0-rc1", sha256="6114254bd724749cb2a189eabfcec37c7a975cd9db796e8ce503311a17c24404", url="https://pypi.org/packages/a8/04/28ec8bfc70025692d56eafe0294fda5c88502280f139ad72e43d5a6d96a6/grpcio-1.62.0rc1.tar.gz")
    version("1.60.1", sha256="dd1d3a8d1d2e50ad9b59e10aa7f07c7d1be2b367f3f2d33c5fade96ed5460962", url="https://pypi.org/packages/7d/6d/919fd5886882c066122e69fbd938c1df2dc0aa22ab8de3e047c6aff5ac58/grpcio-1.60.1.tar.gz")
    version("1.60.0", sha256="2199165a1affb666aa24adf0c97436686d0a61bc5fc113c037701fb7c7fceb96", url="https://pypi.org/packages/61/38/c615b5c2be690fb31871f294cc08a96e598b085b8d07c5967a5018e0b90c/grpcio-1.60.0.tar.gz")
    version("1.60.0-rc1", sha256="d378ea7527706f14173dcb3ebaf9ae0f7b1e42d92a6a7af9e73cc6ca809ffdb2", url="https://pypi.org/packages/3d/5c/db87642b0f5388879a1dbfba36f31eff32f2db1e202e199ac2d72d9bc102/grpcio-1.60.0rc1.tar.gz")
    version("1.59.3", sha256="7800f99568a74a06ebdccd419dd1b6e639b477dcaf6da77ea702f8fb14ce5f80", url="https://pypi.org/packages/ab/a1/f838646e25402eb750f037cf84c1ada46084717375e44724c89900ee4c7d/grpcio-1.59.3.tar.gz")
    version("1.59.2", sha256="d8f9cd4ad1be90b0cf350a2f04a38a36e44a026cac1e036ac593dc48efe91d52", url="https://pypi.org/packages/93/95/7c72028fe9fc46748fb769b13a1e0923acbb79095cd5124b8bac0cebd38c/grpcio-1.59.2.tar.gz")
    version("1.59.0", sha256="acf70a63cf09dd494000007b798aff88a436e1c03b394995ce450be437b8e54f", url="https://pypi.org/packages/38/98/ca2cb5a81e0e2f3e3a00ebf91338fd3278ea0673e156a7ff2de30fe17113/grpcio-1.59.0.tar.gz")
    version("1.58.0", sha256="532410c51ccd851b706d1fbc00a87be0f5312bd6f8e5dbf89d4e99c7f79d7499", url="https://pypi.org/packages/5d/a2/781bae6df87dfd31115b24b1fe01213ef29caf9dbd0b8c1688c59aebf617/grpcio-1.58.0.tar.gz")
    version("1.57.0", sha256="4b089f7ad1eb00a104078bab8015b0ed0ebcb3b589e527ab009c53893fd4e613", url="https://pypi.org/packages/18/b5/3ebe1bd133f472640e2d8941d2208b8de63706ebc08b09e1bb988d7f0071/grpcio-1.57.0.tar.gz")
    version("1.56.2", sha256="0ff789ae7d8ddd76d2ac02e7d13bfef6fc4928ac01e1dcaa182be51b6bcc0aaa", url="https://pypi.org/packages/2f/7e/ddf5d42c77418ebf6d57f1503084e2955e8cf1d49671372fbdff7a82cbe5/grpcio-1.56.2.tar.gz")
    version("1.52.0", sha256="a5d4a83d29fc39af429c10b9b326c174fec49b73398e4a966a1f2a4f30aa4fdb", url="https://pypi.org/packages/ed/b7/6c5cf5c73445b28ac25347c78c6f2d76f2ed9a5d5966bd45b6904b3e7a51/grpcio-1.52.0.tar.gz")
    version("1.48.1", sha256="660217eccd2943bf23ea9a36e2a292024305aec04bf747fbcff1f5032b83610e", url="https://pypi.org/packages/e2/13/0f91c6c7eb0d934141743c7663e8808f4dc478dd0a7b0fd2a02a286c0d6d/grpcio-1.48.1.tar.gz")
    version("1.43.0", sha256="735d9a437c262ab039d02defddcb9f8f545d7009ae61c0114e19dda3843febe5", url="https://pypi.org/packages/c6/6b/5f7cd38ff3ac80f47cbe56618fe45502f90b41a56f5d9e248ee574e14687/grpcio-1.43.0.tar.gz")
    version("1.42.0", sha256="4a8f2c7490fe3696e0cdd566e2f099fb91b51bc75446125175c55581c2f7bc11", url="https://pypi.org/packages/34/be/2565634fc96213bd761ad5732459ab5667ac12b249ccd8c4e658c4e70b99/grpcio-1.42.0.tar.gz")
    version("1.39.0", sha256="57974361a459d6fe04c9ae0af1845974606612249f467bbd2062d963cb90f407", url="https://pypi.org/packages/07/ea/398472e896f529d23fb58e33f01298dfc554a341d58f87c1ea5ad817208e/grpcio-1.39.0.tar.gz")
    version("1.38.1", sha256="1f79d8a24261e3c12ec3a6c25945ff799ae09874fd24815bc17c2dc37715ef6c", url="https://pypi.org/packages/cd/80/4b65b06e35599af065076891248b88d16c87cee1121b8886316ad4343f50/grpcio-1.38.1.tar.gz")
    version("1.38.0", sha256="abbf9c8c3df4d5233d5888c6cfa85c1bb68a6923749bd4dd1abc6e1e93986f17", url="https://pypi.org/packages/8c/34/7dafc9052bd9b2b41c5a8912aeeca01e179d16de17e9c275633d4b807330/grpcio-1.38.0.tar.gz")
    version("1.37.1", sha256="df8305806311d3fe913d4f7eb3ef28e2072159ea12f95baab5d447f1380a71e3", url="https://pypi.org/packages/a0/d6/d04c6550debe23e2eaef0d9c4adccbb6e20d8cce6da40ae989fe8836e287/grpcio-1.37.1.tar.gz")
    version("1.37.0", sha256="b3ce16aa91569760fdabd77ca901b2288152eb16941d28edd9a3a75a0c4a8a85", url="https://pypi.org/packages/0c/c5/f38a7ec5966b2d3b38488494213deaeec421aeef0ba6559e15f58286416c/grpcio-1.37.0.tar.gz")
    version("1.36.0", sha256="70b11805bc9385fcd24e15bcdc5bd8bed463026cd2227d9fdd1ebda612ba0cd9", url="https://pypi.org/packages/9d/9e/18e92a4042fdee8613f5613a37cf7162d32b5674f1b12d0f7b042e7e710b/grpcio-1.36.0.tar.gz")
    version("1.35.0", sha256="7bd0ebbb14dde78bf66a1162efd29d3393e4e943952e2f339757aa48a184645c", url="https://pypi.org/packages/20/4b/0b810309628e354f53b3c90af063f268d74e49902a41196db27f1fb52f06/grpcio-1.35.0.tar.gz")
    version("1.34.1", sha256="1c746a3cd8a830d8d916a9d0476a786aaa98c5cc2a096344af2be955e439f8ac", url="https://pypi.org/packages/81/5e/168a7fa23a025beed6b7daa0981ace55e394a136db3082faed7d6cba4556/grpcio-1.34.1.tar.gz")
    version("1.34.0", sha256="f98f746cacbaa681de0bcd90d7aa77b440e3e1327a9988f6a2b580d54e27d4c3", url="https://pypi.org/packages/35/98/74a430566fdd9d4cc0386322e55306c8928a95da95b1da6fba08641526b5/grpcio-1.34.0.tar.gz")
    version("1.33.2", sha256="21265511880056d19ce4f809ce3fbe2a3fa98ec1fc7167dbdf30a80d3276202e", url="https://pypi.org/packages/cc/1e/5d65ae830536fdb67f10f4bcedca6eb59190ad60d20d796ef3ccdfda4797/grpcio-1.33.2.tar.gz")
    version("1.33.1", sha256="f19782ec5104599382a0f73f2dfea465d0e65f6818bb3c49ca672b97034c64c3", url="https://pypi.org/packages/c3/4b/b8a3e1951c90c3e14a657f3682b705840c146c9cad07948f59df4ff1eca3/grpcio-1.33.1.tar.gz")
    version("1.32.0", sha256="01d3046fe980be25796d368f8fc5ff34b7cf5e1444f3789a017a7fe794465639", url="https://pypi.org/packages/0e/5f/eeb402746a65839acdec78b7e757635f5e446138cc1d68589dfa32cba593/grpcio-1.32.0.tar.gz")
    version("1.30.0", sha256="e8f2f5d16e0164c415f1b31a8d9a81f2e4645a43d1b261375d6bab7b0adf511f", url="https://pypi.org/packages/5e/29/1bd649737e427a6bb850174293b4f2b72ab80dd49462142db9b81e1e5c7b/grpcio-1.30.0.tar.gz")
    version("1.29.0", sha256="a97ea91e31863c9a3879684b5fb3c6ab4b17c5431787548fc9f52b9483ea9c25", url="https://pypi.org/packages/f1/23/62d3e82fa4c505f3195315c8a774b2e656b556d174329aa98edb829e48bc/grpcio-1.29.0.tar.gz")
    version("1.28.1", sha256="cbc322c5d5615e67c2a15be631f64e6c2bab8c12505bc7c150948abdaa0bdbac", url="https://pypi.org/packages/cf/7a/9744998129fce7e29c5f2d8b0f545913b7383e65d8366fc0ae98d11936af/grpcio-1.28.1.tar.gz")
    version("1.27.2", sha256="5ae532b93cf9ce5a2a549b74a2c35e3b690b171ece9358519b3039c7b84c887e", url="https://pypi.org/packages/74/52/9204d08bf37ac2505ebab2fa93b808fac87564580d7cc839db2fe11c3bdd/grpcio-1.27.2.tar.gz")
    version("1.25.0", sha256="c948c034d8997526011960db54f512756fb0b4be1b81140a15b4ef094c6594a4", url="https://pypi.org/packages/e4/60/40c4d2b61d9e4349bc89445deb8d04cc000b10a63446c42d311e0d21d127/grpcio-1.25.0.tar.gz")
    version("1.16.0", sha256="0cc5f2d3ee21c642d8982f197c83053fd3a8cbcd6a60240d8c87c6c256b10d57", url="https://pypi.org/packages/be/84/9afa550ae7bfc65a7150f66ecdbf267617a2d584d9f845b4ef7d026a24ad/grpcio-1.16.0.tar.gz")

    with default_args(type="run"):
        depends_on("py-enum34@1.0.4:", when="@0.13:0.14,1.0.0-rc2,1.0.1-rc1:1.0.2-rc0,1.0.3:1.0,1.2:1.19")
        depends_on("py-futures@2.2:", when="@0.13:0.14,1.0.0-rc2,1.0.1-rc1:1.0.2-rc0,1.0.3:1.0,1.2:1.19")
        depends_on("py-six@1.5.2:", when="@1.0.0-rc2,1.0.1-rc1:1.0.2-rc0,1.0.3:1.0,1.2:1.30")

