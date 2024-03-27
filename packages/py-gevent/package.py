##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyGevent(PythonPackage):
    version("24.2.1", sha256="432fc76f680acf7cf188c2ee0f5d3ab73b63c1f03114c7cd8a34cebbe5aa2056", url="https://pypi.org/packages/27/24/a3a7b713acfcf1177207f49ec25c665123f8972f42bee641bcc9f32961f4/gevent-24.2.1.tar.gz")
    version("23.9.1", sha256="72c002235390d46f94938a96920d8856d4ffd9ddf62a303a0d7c118894097e34", url="https://pypi.org/packages/8e/ce/d2b9a376ee010f6d548bf1b6b6eddc372a175e6e100896e607c57e37f7cf/gevent-23.9.1.tar.gz")
    version("23.9.0.post1", sha256="943f26edada39dfd5f50551157bb9011191c7367be36e341d0f1cdecfe07a229", url="https://pypi.org/packages/a0/06/7727ae8e3a065078327386b1c611995efb1a50a455fbab8af612d3b2d9ce/gevent-23.9.0.post1.tar.gz")
    version("23.7.0", sha256="d0d3630674c1b344b256a298ab1ff43220f840b12af768131b5d74e485924237", url="https://pypi.org/packages/8a/fb/d16e63f0dfce72f49edaa0b22f69218d196601c0c3366e5094ea90a6bbca/gevent-23.7.0.tar.gz")
    version("22.10.2", sha256="1ca01da176ee37b3527a2702f7d40dbc9ffb8cfc7be5a03bfa4f9eec45e55c46", url="https://pypi.org/packages/9f/4a/e9e57cb9495f0c7943b1d5965c4bdd0d78bc4a433a7c96ee034b16c01520/gevent-22.10.2.tar.gz")
    version("22.10.1", sha256="df3042349c9a4460eeaec8d0e56d737cb183eed055e75a6af9dbda94aaddaf4d", url="https://pypi.org/packages/97/5e/be2ac96fe2e6d5ad40c0ed5cf83c07ce6a74b9a5a1f0422e8b5d9225c865/gevent-22.10.1.tar.gz")
    version("22.8.0", sha256="868d500fe2b7f9750eadc07ada8ab32360c0e71976be2bf5919482f14a6477c7", url="https://pypi.org/packages/48/4b/dd44b36dab6a534c2af4aceb829d9977f983ff40a6a0d4217d2533801635/gevent-22.8.0.tar.gz")
    version("21.12.0", sha256="f48b64578c367b91fa793bf8eaaaf4995cb93c8bc45860e473bf868070ad094e", url="https://pypi.org/packages/c8/18/631398e45c109987f2d8e57f3adda161cc5ff2bd8738ca830c3a2dd41a85/gevent-21.12.0.tar.gz")
    version("21.8.0", sha256="43e93e1a4738c922a2416baf33f0afb0a20b22d3dba886720bc037cd02a98575", url="https://pypi.org/packages/33/2e/49317db0bbd846720ce15fd43641b17a208e6466c582ecbe845e35092ea2/gevent-21.8.0.tar.gz")
    version("21.1.2", sha256="520cc2a029a9eef436e4e56b007af7859315cafa21937d43c1d5269f12f2c981", url="https://pypi.org/packages/0b/50/1b1175ea3a269b5fa3f0f7fed11149888180695bef5fbf568adbb196efaf/gevent-21.1.2.tar.gz")
    version("1.5.0", sha256="b2814258e3b3fb32786bb73af271ad31f51e1ac01f33b37426b66cb8491b4c29", url="https://pypi.org/packages/5a/79/2c63d385d017b5dd7d70983a463dfd25befae70c824fedb857df6e72eff2/gevent-1.5.0.tar.gz")
    version("1.4.0", sha256="1eb7fa3b9bd9174dfe9c3b59b7a09b768ecd496debfc4976a9530a3e15c990d1", url="https://pypi.org/packages/ed/27/6c49b70808f569b66ec7fac2e78f076e9b204db9cf5768740cff3d5a07ae/gevent-1.4.0.tar.gz")
    version("1.3.7", sha256="3f06f4802824c577272960df003a304ce95b3e82eea01dad2637cc8609c80e2c", url="https://pypi.org/packages/10/c1/9499b146bfa43aa4f1e0ed1bab1bd3209a4861d25650c11725036c731cf5/gevent-1.3.7.tar.gz")
    version("1.3.6", sha256="7b413c391e8ad6607b7f7540d698a94349abd64e4935184c595f7cdcc69904c6", url="https://pypi.org/packages/49/13/aa4bb3640b5167fe58875d3d7e65390cdb14f9682a41a741a566bb560842/gevent-1.3.6.tar.gz")
    version("1.3.5", sha256="7f15861f3cc92f49663ca88c4774d26d8044783a65fbc28071a2bd1c7bf36ff0", url="https://pypi.org/packages/e6/0a/fc345c6e6161f84484870dbcaa58e427c10bd9bdcd08a69bed3d6b398bf1/gevent-1.3.5.tar.gz")
    version("1.3.4", sha256="53c4dc705886d028f5d81e698b1d1479994a421498cd6529cb9711b5e2a84f74", url="https://pypi.org/packages/f8/85/f92a8f43c9f15ffad49d743d929863a042ce3e8de5746c63bb4d6ce51a02/gevent-1.3.4.tar.gz")
    version("1.3.3", sha256="59465c7bce7671834f58b44ef62cd8626f1557a0e7e3de44a3b596056f8adc73", url="https://pypi.org/packages/48/a3/09d1f3c650ae9ade2965ac71cbb61a7dd6fd0d3bd67ac12aa06bb23d3920/gevent-1.3.3.tar.gz")
    version("1.3.2.post0", sha256="5eeec334778cbad059b54fc468b0690db6794fe12a1dada7b70924d1c9ffbeac", url="https://pypi.org/packages/a4/5b/12d4fb2e48634b34537ae250e958de426811f876fbacb2a2041f2af147d8/gevent-1.3.2.post0.tar.gz")
    version("1.3.2", sha256="390d820f375626cd0406fdf9b2657f796818fa53c7cff34a9af0e34a4d6bc4ea", url="https://pypi.org/packages/62/85/3a75fa15a5375506a6617c1ce706ea800f016ca2be1a87165f1ab5aff3a2/gevent-1.3.2.tar.gz")
    version("1.3.1", sha256="600d02a31c08936fe4a5181756009a4a3663403b41bc122df039dae0aa3e3831", url="https://pypi.org/packages/cf/c6/aa3ac939ec1028b7e0998c4ed88d9cd18782ca458e834f0faaad2823af3a/gevent-1.3.1.tar.gz")

    with default_args(type="run"):
        depends_on("py-cffi@1.12.2:", when="@1.5-alpha1:1.5-alpha3,1.5.0:1,23.9.1: platform=windows")
        depends_on("py-cffi@1.11.5:", when="@1.3-beta2:1.3.5,1.3.7:1.4 platform=windows")
        depends_on("py-greenlet@3.0.0-rc3:", when="@23.9.1: ^python@3.11:")
        depends_on("py-greenlet@2.0.0:", when="@23.9.1: ^python@:3.10")
        depends_on("py-greenlet@0.4.14:", when="@1.3.7:1.5-alpha3,1.5.0:1")
        depends_on("py-greenlet@0.4.13:", when="@1.3-alpha2:1.3.5")
        depends_on("py-zope-event", when="@23.9.1:")
        depends_on("py-zope-interface", when="@23.9.1:")

