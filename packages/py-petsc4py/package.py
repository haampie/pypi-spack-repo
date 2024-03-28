# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPetsc4py(PythonPackage):
    # BEGIN VERSIONS
    version("3.20.2", sha256="d3f24aa6612ded3e9b9ae11d5533f319d1df1705bea6d81385fea023d01175c9", url="https://pypi.org/packages/e0/8e/ada0ae6078531c72ff440ee20a6282df21b09d3cbbfecb7e51e357108398/petsc4py-3.20.2.tar.gz")
    version("3.20.1", sha256="dcc9092040d13130496f1961b79c36468f383b6ede398080e004f1966c06ad38", url="https://pypi.org/packages/83/88/ea3e1f6d5c29b54d7a521183c78d025c7f417887e33cfab0fd2d4b1ce3ce/petsc4py-3.20.1.tar.gz")
    version("3.20.0", sha256="c2461eef3977ae5c214ad252520adbb92ec3a31d00e79391dd92535077bbf03e", url="https://pypi.org/packages/ba/03/65402ad69b02e455952745672f92b35ae33ca5d248adfe12c529c7c07ae9/petsc4py-3.20.0.tar.gz")
    version("3.19.6", sha256="bd7891b651eb83504c744e70706818cf63ecbabee3206c1fed7c3013873802b9", url="https://pypi.org/packages/ff/a4/f4c1f1334bef4a045b1e49c168494b542b228d4b954726f7e42508de6bef/petsc4py-3.19.6.tar.gz")
    version("3.19.5", sha256="e059fdb8b23936c3182c9226924029dbdc8f1f72a623be0fe8c2caf8646c7a45", url="https://pypi.org/packages/a3/a1/0b99bc3d5523768b777dbd0c82501cc213558243ffbbb95f847890f143ae/petsc4py-3.19.5.tar.gz")
    version("3.19.4", sha256="5621ddee63d0c631d2e8fed2d5d9763b183ad164c227dde8d3abcdb6c35c5ffb", url="https://pypi.org/packages/e7/5b/5a04d41b26f46d97dfe0086bb3c3fd0085ede08db2db9821152d49c8a969/petsc4py-3.19.4.tar.gz")
    version("3.19.2", sha256="5f207eb95f87ddafa32229681a95af61912871cd7fbd38780bc63019dad3e7b8", url="https://pypi.org/packages/69/50/b3c32f590b21a9c366fe471cdafd1422854e2ab70ec00e57fd582c85478e/petsc4py-3.19.2.tar.gz")
    version("3.19.1", sha256="d04def9995ed6395e125c605da169438d77d410d5019dc57be42e428ade30190", url="https://pypi.org/packages/ed/b7/2d84edf0192cb33dded2f56b80cca73ec2a0f615bf38699b8ea43bf73992/petsc4py-3.19.1.tar.gz")
    version("3.19.0", sha256="2d0939686e81164bc3047de6d67785ce9a2a695040e5c4bb8978b834ba9a8a5d", url="https://pypi.org/packages/ed/70/ff5d45cf4cac02eacf07b8164a68261e8ec9c9554c97c4ed2d1caeca03bc/petsc4py-3.19.0.tar.gz")
    version("3.18.5", sha256="625cbb99d7d3000ad05afe60585c6aa24ca650894b09a1989127febb64b65470", url="https://pypi.org/packages/3d/af/8037865ac5b20e84c736399abd7b38bef871ed9f0782c01ec1c1a24a471b/petsc4py-3.18.5.tar.gz")
    version("3.18.4", sha256="84a055b7f38d1200a8c486c89db05ce0724fe28da56afb656660cef054384e24", url="https://pypi.org/packages/d6/23/7cca5dcc51c1bbacc827f94b5122a4eda6d13e9297693d8fa9f6af8109d2/petsc4py-3.18.4.tar.gz")
    version("3.18.3", sha256="853ab9620c4832cbfe1f490edde827a505c8a376cc1a7b4fa6406faac9059433", url="https://pypi.org/packages/ff/77/484749f16b1d2cdbf18399f2da9fc81903bcac9804be689860a3d3623878/petsc4py-3.18.3.tar.gz")
    version("3.18.2", sha256="1b6761b02ec6ef9099e2a048e234065c1c4096ace01e52e353624b80417cceec", url="https://pypi.org/packages/98/f9/c4cdd4aa974dbfee4a526eefb4d79394cd2ded2e6522723066dcccc6d933/petsc4py-3.18.2.tar.gz")
    version("3.18.1", sha256="6d9d9632e2da0920c4e3905b7bac919837bdd85ecfaf1b9e461ba7e05ec4a5ce", url="https://pypi.org/packages/3c/23/ed5833b11e2b228b3d3764f98b18005a36b756aa210bb54c7f6f67c6216e/petsc4py-3.18.1.tar.gz")
    version("3.18.0", sha256="76bad2d35f380f698f5649c3f38eabd153b9b19b1fe3ce3a1d3de9aa5824a4d2", url="https://pypi.org/packages/cc/b7/ca9e4864370744eda1100ab828670eabf4cb95b72da8ea57ff67ae73dd69/petsc4py-3.18.0.tar.gz")
    version("3.17.4", sha256="216c3da074557946615d37d0826bc89f1f2e599323e2dacbdc45326d78bd50c6", url="https://pypi.org/packages/95/04/e58f2c8f8a6f5ed86e0d9d1938d8e4aa7f8edd90d568ea7d282933e22d9c/petsc4py-3.17.4.tar.gz")
    version("3.17.3", sha256="c588ab4a17deebe7f0a57f966b3368d88f01d1a1c09f220f63fe8e3b37a32899", url="https://pypi.org/packages/9c/87/4826ee08b3ec32abf87c7ea79a313212557749c4b9e2093aa8cb8362db17/petsc4py-3.17.3.tar.gz")
    version("3.17.2", sha256="7e256e13013ce12c8e52edee35920e3d2c1deaae1b71597a3064201eba7abc1c", url="https://pypi.org/packages/d5/c9/af19b8e466e7641ecf3d12ac5dc3198d32de570ecf46ab811655695d0f56/petsc4py-3.17.2.tar.gz")
    version("3.17.1", sha256="f73a6eb0b453ec2500c9b353dc8427f205bcc12910b263bc4351fea3c6e0af71", url="https://pypi.org/packages/6c/17/1184221edc099322a9450dfb8474cade79d171c5f4b11108c279a90e392d/petsc4py-3.17.1.tar.gz")
    version("3.17.0", sha256="a3543ebb87dc2b47046e1950b3a356e249d365526515b5e6b328aa7bfae94d29", url="https://pypi.org/packages/4b/05/dd0c21e2dd50cc15d57e0f20c582c57782c5f79df1b5938f522d702cf969/petsc4py-3.17.0.tar.gz")
    version("3.16.6", sha256="a9b4ed19ca2e62b38da51ac3a70539d9581a1354cc4464c93963d7e95bd8ef66", url="https://pypi.org/packages/bc/80/f05e649826def50c42ae5035e94da4de8f1e30e79b46602b023622a35eb0/petsc4py-3.16.6.tar.gz")
    version("3.16.5", sha256="f0ab5c5947ee0b58e51f741f46fab0d32e6458245e8f8b81fcf3da77bad50d25", url="https://pypi.org/packages/d3/49/7887b1c2782025499265ac22381670d5582ca2cd729c179ba7a5b794a02f/petsc4py-3.16.5.tar.gz")
    version("3.16.4", sha256="51ac59be9d741ede95c8e0e13b6062b6fb1bd1c975da26732ba059ee8c5bb7eb", url="https://pypi.org/packages/34/30/fe297ab08725b278b68d3664241150ae9f0deeff9dbac6da66416122b353/petsc4py-3.16.4.tar.gz")
    version("3.16.3", sha256="10e730d50716e40de55b200ff53b461bc4f3fcc798ba89b74dfe6bdf63fa7b6e", url="https://pypi.org/packages/b5/1e/21bd550db29b92f58d2de714e262b035c5a1de9e627d9a218df69e14f520/petsc4py-3.16.3.tar.gz")
    version("3.16.2", sha256="906634497ae9c59f2c97e12b935954e5ba95df2e764290c24fff6751b7510b04", url="https://pypi.org/packages/79/f3/db0edf8ee1181efdfaa62a003ba0b73bd1f55050be1ad2d0d4fe6a6997c5/petsc4py-3.16.2.tar.gz")
    version("3.16.1", sha256="c218358217c436947f8fd61f247f73ac65fa29ea3489ad00bef5827b1436b95f", url="https://pypi.org/packages/11/07/555668abf04f88b595c2838a18db567ed02f5f8b2eda65cd62b05c5ace87/petsc4py-3.16.1.tar.gz")
    version("3.16.0", sha256="4044accfdc2c80994e80e4e286478d1ba9ac358512d1b74c42e1327eadb0d802", url="https://pypi.org/packages/e0/97/c14e3614e19be2e5c09c0150a288e54bcaa71291b75e7e86947b34677ad0/petsc4py-3.16.0.tar.gz")
    version("3.15.1", sha256="4ec8f42081e4d6a61157b32869b352dcb18c69077f2d1e4160f3837efd9e150f", url="https://pypi.org/packages/78/80/b28275d91ca4fd44a25c099b56f8b994526b5172aaa20a32381ee920ffa2/petsc4py-3.15.1.tar.gz")
    version("3.15.0", sha256="fe744bd9c92557f0a38027f19a419b6e6765a982f531d02e620c79eb1a97bae7", url="https://pypi.org/packages/12/c0/8e42e40d346d7f5efc8d7b7aa570f56b0aeba544e07e12dd889b5addf722/petsc4py-3.15.0.tar.gz")
    version("3.14.1", sha256="f5f8daf3a4cd1dfc945876b0d83a05b25f3c54e08046312eaa3e3036b24139c0", url="https://pypi.org/packages/c1/73/604fe37a9305586ad13807ffc81f2a0535f5c0a2cd2c615f248f769374c0/petsc4py-3.14.1.tar.gz")
    version("3.14.0", sha256="33ac9fb55a541e4c1deabd6e2144da96d5ae70e70c830a55de558000cf3f0ec5", url="https://pypi.org/packages/59/65/94c85bdacebc4b3b18527538ed010334a13cecdbe8bdbdc8b794307aae9f/petsc4py-3.14.0.tar.gz")
    version("3.13.0", sha256="ace21f71102e752fefac6c81b65207edba89a6974b3c58c71599c6c358640f39", url="https://pypi.org/packages/7c/e7/5b089013c5188ee5f619ad64749fc3e6355943950dfcf421c327d66ee2ac/petsc4py-3.13.0.tar.gz")
    version("3.12.0", sha256="1a02fa0336c27583aabf399124ac0610ef20452cf6b837a1082f7788f17fadad", url="https://pypi.org/packages/e4/51/7eaa24a5797f0728007acfbfafed026ff2b0602f9ddd07564829423663df/petsc4py-3.12.0.tar.gz")
    version("3.11.0", sha256="58f4f57ac96ec39273906859cdc388b1ae372045c726bfd2a01d4eca8bc4a1e6", url="https://pypi.org/packages/71/5e/8494910160bc5d97132994c9699a3678ab08e8b484ed3950fe88044b8838/petsc4py-3.11.0.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    variant("mpi", default=False)
    # END VARIANTS

    # BEGIN DEPENDENCIES
    # END DEPENDENCIES

