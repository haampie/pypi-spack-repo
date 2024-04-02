# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyProtobuf(PythonPackage):
    # BEGIN VERSIONS
    version("4.24.3", sha256="12e9ad2ec079b833176d2921be2cb24281fa591f0b119b208b788adc48c2561d", url="https://pypi.org/packages/79/30/98dc7297ce8c3f0182800d2879703f0196e76d6a28e53ecaafc3901f8118/protobuf-4.24.3.tar.gz")
    version("4.23.3", sha256="7a92beb30600332a52cdadbedb40d33fd7c8a0d7f549c440347bc606fb3fe34b", url="https://pypi.org/packages/e5/9d/20e9bf4067e85c3074f1f5bac820a3cfb9ce885cddd8a649fe3570659c77/protobuf-4.23.3.tar.gz")
    version("4.21.9", sha256="61f21493d96d2a77f9ca84fefa105872550ab5ef71d21c458eb80edcf4885a99", url="https://pypi.org/packages/0f/cd/165eaac1c43a5ba391a36087dc909e03c3ae3f7dbcab74f287631208ba92/protobuf-4.21.9.tar.gz")
    version("4.21.7", sha256="71d9dba03ed3432c878a801e2ea51e034b0ea01cf3a4344fb60166cb5f6c8757", url="https://pypi.org/packages/56/23/f716074d2ed0af82c0d1da1eaa5e4bb086236568405f13ab0bbaaa6307fb/protobuf-4.21.7.tar.gz")
    version("4.21.5", sha256="eb1106e87e095628e96884a877a51cdb90087106ee693925ec0a300468a9be3a", url="https://pypi.org/packages/51/90/d2bf065b8753951e5fdba822af358edae6dac055b81f018e1ec74d8ba71e/protobuf-4.21.5.tar.gz")
    version("3.20.3", sha256="2e3427429c9cffebf259491be0af70189607f365c2f41c7c3764af6f337105f2", url="https://pypi.org/packages/55/5b/e3d951e34f8356e5feecacd12a8e3b258a1da6d9a03ad1770f28925f29bc/protobuf-3.20.3.tar.gz")
    version("3.20.2", sha256="712dca319eee507a1e7df3591e639a2b112a2f4a62d40fe7832a16fd19151750", url="https://pypi.org/packages/3d/79/34fbcce8666c74ec6729e2844143fd066d9708eecb89ecd2037fc6cfe9a9/protobuf-3.20.2.tar.gz")
    version("3.20.1", sha256="adc31566d027f45efe3f44eeb5b1f329da43891634d61c75a5944e9be6dd42c9", url="https://pypi.org/packages/19/96/1283259c25bc48a6df98fa096f66fc568b40137b93806ef5ff66a2d166b1/protobuf-3.20.1.tar.gz")
    version("3.20.0", sha256="71b2c3d1cd26ed1ec7c8196834143258b2ad7f444efff26fdc366c6f5e752702", url="https://pypi.org/packages/6d/3e/40c56d21154a1f3ababb69f675333d7fb70c8293f9ca42ea3e448327fc50/protobuf-3.20.0.tar.gz")
    version("3.19.4", sha256="9df0c10adf3e83015ced42a9a7bd64e13d06c4cf45c340d2c63020ea04499d0a", url="https://pypi.org/packages/6c/49/f864b9fd6310d9a15ddae5b37d78dff1df0e2e1da476442fee062c6032b2/protobuf-3.19.4.tar.gz")
    version("3.19.3", sha256="d975a6314fbf5c524d4981e24294739216b5fb81ef3c14b86fb4b045d6690907", url="https://pypi.org/packages/d9/d5/bf6c307f58b4c486f6517341d2f2673cd889b7d3a83cae78a9081233c679/protobuf-3.19.3.tar.gz")
    version("3.19.2", sha256="392f928e57054520276fdad412e045910268224b9446c218702e577d26eaf557", url="https://pypi.org/packages/77/93/15f810611aedaa67a9e8804d74a73103e5fa5f911a9966be3883fd1b80cf/protobuf-3.19.2.tar.gz")
    version("3.19.1", sha256="62a8e4baa9cb9e064eb62d1002eca820857ab2138440cb4b3ea4243830f94ca7", url="https://pypi.org/packages/37/52/4e40f7513b44671817a92dc566f4a6e8eba65bfc94f79da23186e6c127ce/protobuf-3.19.1.tar.gz")
    version("3.19.0", sha256="6a1dc6584d24ef86f5b104bcad64fa0fe06ed36e5687f426e0445d363a041d18", url="https://pypi.org/packages/c9/cb/95924cc9ced5ba0b489bb861195234a964dbd83f8c3d12d254ef4c4a5980/protobuf-3.19.0.tar.gz")
    version("3.18.1", sha256="1c9bb40503751087300dd12ce2e90899d68628977905c76effc48e66d089391e", url="https://pypi.org/packages/ff/3e/19b09fd98ca30a9cd53269806602ffe1d32464fe1f662ec8765a215f0495/protobuf-3.18.1.tar.gz")
    version("3.17.3", sha256="72804ea5eaa9c22a090d2803813e280fb273b62d5ae497aaf3553d141c4fdd7b", url="https://pypi.org/packages/3d/64/a3b379cb9c7827ad33c67dcda4c4ad117bdef1b7d68b22a05c963cf4727d/protobuf-3.17.3.tar.gz")
    version("3.17.2", sha256="5a3450acf046716e4a4f02a3f7adfb7b86f1b5b3ae392cec759915e79538d40d", url="https://pypi.org/packages/08/ae/a443513a5b71812791a2748776a4b5dcd575e1a88e36a5e314b743054491/protobuf-3.17.2.tar.gz")
    version("3.17.1", sha256="25bc4f1c23aced9b3a9e70eef7f03e63bcbd6cfbd881a91b5688412dce8992e1", url="https://pypi.org/packages/b3/82/b5720e214bb2977e1857da6a29321cf78233a4233fbcc5c0552d2d415a47/protobuf-3.17.1.tar.gz")
    version("3.17.0", sha256="05dfe9319939a8473c21b469f34f6486646e54fb8542637cf7ed8e2fbfe21538", url="https://pypi.org/packages/9f/98/dd2e0eb3982288a3290849845a037613d91bcd98ea04764425216baf4982/protobuf-3.17.0.tar.gz")
    version("3.16.0", sha256="228eecbedd46d75010f1e0f8ce34dbcd11ae5a40c165a9fc9d330a58aa302818", url="https://pypi.org/packages/b4/7e/30e31f18058ed50a5c6d4b0db4c5e2d573069cbcbd7a5aae45c207d226b3/protobuf-3.16.0.tar.gz")
    version("3.15.8", sha256="0277f62b1e42210cafe79a71628c1d553348da81cbd553402a7f7549c50b11d0", url="https://pypi.org/packages/48/c8/e90238d5c0de6808da7b2529f4b2bd66c59ee73caabdd9d5bc351512f8b6/protobuf-3.15.8.tar.gz")
    version("3.15.7", sha256="2d03fc2591543cd2456d0b72230b50c4519546a8d379ac6fd3ecd84c6df61e5d", url="https://pypi.org/packages/b0/e1/3bf55eb999735a948ea4d8c417458ba2c14615c104fff8976729832efb8f/protobuf-3.15.7.tar.gz")
    version("3.15.6", sha256="2b974519a2ae83aa1e31cff9018c70bbe0e303a46a598f982943c49ae1d4fcd3", url="https://pypi.org/packages/c5/82/cee5dcde1c7a0ffe1336946a117d31b1a394558fcf4d8ca3fba720a47f80/protobuf-3.15.6.tar.gz")
    version("3.15.5", sha256="be8a929c6178bb6cbe9e2c858be62fa08966a39ae758a8493a88f0ed1efb6097", url="https://pypi.org/packages/1c/d1/42c750caec0e6a606d9f323375083e603b4850ef59d3443f55dd5658b687/protobuf-3.15.5.tar.gz")
    version("3.15.1", sha256="824dbae3390fcc3ea1bf96748e6da951a601802894cf7e1465e72b4732538cab", url="https://pypi.org/packages/6f/cc/819835087776f08c3a4b4193174bdd4a2c8b6763a880667d7c30552b0b4c/protobuf-3.15.1.tar.gz")
    version("3.12.2", sha256="49ef8ab4c27812a89a76fa894fe7a08f42f2147078392c0dee51d4a444ef6df5", url="https://pypi.org/packages/ab/e7/8001b5fc971078a15f57cb56e15b699cb0c0f43b1dffaa2fae39961d80da/protobuf-3.12.2.tar.gz")
    version("3.11.2", sha256="3d7a7d8d20b4e7a8f63f62de2d192cfd8b7a53c56caba7ece95367ca2b80c574", url="https://pypi.org/packages/f8/9c/185f11499a438d11348de507e0a9cf3fe7d13ae22c65bc2d55e02bf9dfc7/protobuf-3.11.2.tar.gz")
    version("3.11.1", sha256="aecdf12ef6dc7fd91713a6da93a86c2f2a8fe54840a3b1670853a2b7402e77c9", url="https://pypi.org/packages/c7/dc/850b5cd7f4c96cf8d58f5b3e2913cf8ac2d8661358fa978b314ee668fb10/protobuf-3.11.1.tar.gz")
    version("3.11.0", sha256="97b08853b9bb71512ed52381f05cf2d4179f4234825b505d8f8d2bb9d9429939", url="https://pypi.org/packages/a1/99/9cc943ccc8b004f2df2fa6fc74144f1261944a2164c81f28589b5eb87f1f/protobuf-3.11.0.tar.gz")
    version("3.10.0", sha256="db83b5c12c0cd30150bb568e6feb2435c49ce4e68fe2d7b903113f0e221e58fe", url="https://pypi.org/packages/12/b9/e7c6a58613c9fe724d1ff9f2353fa48901e6b1b99d0ba64c36a8de2cfa45/protobuf-3.10.0.tar.gz")
    version("3.9.2", sha256="843f498e98ad1469ad54ecb4a7ccf48605a1c5d2bd26ae799c7a2cddab4a37ec", url="https://pypi.org/packages/7d/d0/473a91ac2c59639b9fe2f3248d98b4d6084d4be8254a7b83f010feac8de9/protobuf-3.9.2.tar.gz")
    version("3.9.1", sha256="d831b047bd69becaf64019a47179eb22118a50dd008340655266a906c69c6417", url="https://pypi.org/packages/6d/54/12c5c92ffab546538ea5b544c6afbfcce333fd47e99c1198e24a8efdef1f/protobuf-3.9.1.tar.gz")
    version("3.8.0", sha256="8c61cc8a76e9d381c665aecc5105fa0f1878cf7db8b5cd17202603bcb386d0fc", url="https://pypi.org/packages/65/95/8fe278158433a9bc34723f9ecbdee3097fb6baefaca932ec0331a9f80244/protobuf-3.8.0.tar.gz")
    version("3.7.1", sha256="21e395d7959551e759d604940a115c51c6347d90a475c9baf471a1a86b5604a9", url="https://pypi.org/packages/cf/72/8c1ed9148ded82adbb76c30f958c6d456a2abc08f092b62a586bdf973b80/protobuf-3.7.1.tar.gz")
    version("3.6.1", sha256="1489b376b0f364bcc6f89519718c057eb191d7ad6f1b395ffd93d1aa45587811", url="https://pypi.org/packages/1b/90/f531329e628ff34aee79b0b9523196eb7b5b6b398f112bb0c03b24ab1973/protobuf-3.6.1.tar.gz")
    version("3.6.0", sha256="a37836aa47d1b81c2db1a6b7a5e79926062b5d76bd962115a0e615551be2b48d", url="https://pypi.org/packages/7f/51/7429b4009ccd54717d54b3a273d16df1a269845b39bcca3b4b7023a48078/protobuf-3.6.0.tar.gz")
    version("3.5.2", sha256="09879a295fd7234e523b62066223b128c5a8a88f682e3aff62fb115e4a0d8be0", url="https://pypi.org/packages/f2/2f/7c8475f523b6db67506eba48d3beacc3625e0effabfac109848f19e3cffc/protobuf-3.5.2.tar.gz")
    version("3.5.1", sha256="95b78959572de7d7fafa3acb718ed71f482932ddddddbd29ba8319c10639d863", url="https://pypi.org/packages/14/03/ff5279abda7b46e9538bfb1411d42831b7e65c460d73831ed2445649bc02/protobuf-3.5.1.tar.gz")
    version("3.4.0", sha256="ef02609ef445987976a3a26bff77119c518e0915c96661c3a3b17856d0ef6374", url="https://pypi.org/packages/89/45/3214bb758646a1a30459ca0f5b8f8164d6893f24725c58b632e663565f44/protobuf-3.4.0.tar.gz")
    version("3.3.0", sha256="1cbcee2c45773f57cb6de7ee0eceb97f92b9b69c0178305509b162c0160c1f04", url="https://pypi.org/packages/56/28/6263d846f60dad93939fd3a22d712d6bae3bf3484332d22bd5933dec8c99/protobuf-3.3.0.tar.gz")
    version("3.0.0", sha256="ecc40bc30f1183b418fe0ec0c90bc3b53fa1707c4205ee278c6b90479e5b6ff5", url="https://pypi.org/packages/14/3e/56da1ecfa58f6da0053a523444dff9dfb8a18928c186ad529a24b0e82dec/protobuf-3.0.0.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    variant("cpp", default=False, description="cpp")
    # END VARIANTS

    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("python@3.7:", when="@3.20:3,4.21:4.24")
        depends_on("py-setuptools", when="@3.5.2.post:3.6.0,3.8.0:3.12.2,4:4.0.0-rc1")
        depends_on("py-six@1.9:", when="@3.5.2.post:3.6.0,3.8.0:3.12.2,4:4.0.0-rc1")
    # END DEPENDENCIES

