# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyMultidict(PythonPackage):
    # BEGIN VERSIONS
    version("6.0.5", sha256="f7e301075edaf50500f0b341543c41194d8df3ae5caf4702f2095f3ca73dd8da", url="https://pypi.org/packages/f9/79/722ca999a3a09a63b35aac12ec27dfa8e5bb3a38b0f857f7a1a209a88836/multidict-6.0.5.tar.gz")
    version("6.0.4", sha256="3666906492efb76453c0e7b97f2cf459b0682e7402c0489a95484965dbc1da49", url="https://pypi.org/packages/4a/15/bd620f7a6eb9aa5112c4ef93e7031bcd071e0611763d8e17706ef8ba65e0/multidict-6.0.4.tar.gz")
    version("6.0.3", sha256="2523a29006c034687eccd3ee70093a697129a3ffe8732535d3b2df6a4ecc279d", url="https://pypi.org/packages/b5/5b/1dd3b9cf73c474ea1d0f0b1f8b7b712b0f13817493fd93101256ec856b59/multidict-6.0.3.tar.gz")
    version("6.0.2", sha256="5ff3bd75f38e4c43f1f470f2df7a4d430b821c4ce22be384e1459cb57d6bb013", url="https://pypi.org/packages/fa/a7/71c253cdb8a1528802bac7503bf82fe674367e4055b09c28846fdfa4ab90/multidict-6.0.2.tar.gz")
    version("6.0.1", sha256="d40616f3f9326a18e1f2fa7c7e8e0e04a7e5228bfa2bd62c1e0d68fbc259b09b", url="https://pypi.org/packages/78/91/db40f5e6bd2b5d2f3fff0f5edee05035513c11fff09c565368f22129240a/multidict-6.0.1.tar.gz")
    version("6.0.0", sha256="84eae1eb73e64a34925eda18961e09e7441b2864d302fd726fa684d14151b3ae", url="https://pypi.org/packages/9e/4e/10b87ecb16934889d3503f358a572f2f939bcacf0016b77c77bb9a48557b/multidict-6.0.0.tar.gz")
    version("5.2.0", sha256="0dd1c93edb444b33ba2274b66f63def8a327d607c6c790772f448a53b6ea59ce", url="https://pypi.org/packages/8e/7c/e12a69795b7b7d5071614af2c691c97fbf16a2a513c66ec52dd7d0a115bb/multidict-5.2.0.tar.gz")
    version("5.1.0", sha256="25b4e5f22d3a37ddf3effc0710ba692cfc792c2b9edfb9c05aefe823256e84d5", url="https://pypi.org/packages/1c/74/e8b46156f37ca56d10d895d4e8595aa2b344cff3c1fb3629ec97a8656ccb/multidict-5.1.0.tar.gz")
    version("5.0.2", sha256="e5bf89fe57f702a046c7ec718fe330ed50efd4bcf74722940db2eb0919cddb1c", url="https://pypi.org/packages/da/e6/50c7f52781f45c2b37c77e962c30a3944a9e79a46ea92956e826c24d3432/multidict-5.0.2.tar.gz")
    version("5.0.1", sha256="0b4d193cb6749f3d200b699bcce0a71946fb869284eb4e040f49283187105fc3", url="https://pypi.org/packages/51/81/5306a57ded398c88893c279f3ae030234ce7577e5092216ac8faa476ab2d/multidict-5.0.1.tar.gz")
    version("4.7.6", sha256="fbb77a75e529021e7c4a8d4e823d88ef4d23674a202be4f5addffc72cbb91430", url="https://pypi.org/packages/65/d4/fabdcc5ee4451c8a8e177e27ddfd131a53a82ecc5a3b68468b7e9f8d70b4/multidict-4.7.6.tar.gz")
    version("4.7.5", sha256="aee283c49601fa4c13adc64c09c978838a7e812f85377ae130a24d7198c0331e", url="https://pypi.org/packages/61/b4/475114b3f1671da634f89239e61038f8742d9ac13aa34b32a05bf8022d22/multidict-4.7.5.tar.gz")
    version("4.7.4", sha256="d7d428488c67b09b26928950a395e41cc72bb9c3d5abfe9f0521940ee4f796d4", url="https://pypi.org/packages/b6/22/ae21cedaa0e6d35e84e8ab57700dcf3d4609421ebe113e1aaafc468eec42/multidict-4.7.4.tar.gz")
    version("4.7.3", sha256="be813fb9e5ce41a5a99a29cdb857144a1bd6670883586f995b940a4878dc5238", url="https://pypi.org/packages/84/96/5503ba866d8d216e49a6ce3bcb288df8a5fb3ac8a90b8fcff9ddcda32568/multidict-4.7.3.tar.gz")
    version("4.7.2", sha256="d4dafdcfbf0ac80fc5f00603f0ce43e487c654ae34a656e4749f175d9832b1b5", url="https://pypi.org/packages/ec/1b/a117d6cb4403f2b64633606e3767f65fa8897b7db6efe14391c7b96cf2f6/multidict-4.7.2.tar.gz")
    version("4.7.1", sha256="d7b6da08538302c5245cd3103f333655ba7f274915f1f5121c4f4b5fbdb3febe", url="https://pypi.org/packages/34/68/38290d44ea34dae6d52719f0c94bd09951387cec75e36cdce6805b5f27e9/multidict-4.7.1.tar.gz")
    version("4.6.1", sha256="5159c4975931a1a78bf6602bbebaa366747fce0a56cb2111f44789d2c45e379f", url="https://pypi.org/packages/8a/74/61547af55c077b8d2e3648c2af74c08fa1e382665b290468db7ba54db2ea/multidict-4.6.1.tar.gz")
    version("4.6.0", sha256="56fb5c003ef5d7b0d4957fe2d36fc29df16e56667ef78ee2a5bc5379c874fff0", url="https://pypi.org/packages/b7/8f/1ec863af20356921e9eb9b69a2ccb55fbe24550270354f17acbdaa6965cd/multidict-4.6.0.tar.gz")
    version("4.5.2", sha256="024b8129695a952ebd93373e45b5d341dbb87c17ce49637b34000093f243dd4f", url="https://pypi.org/packages/7f/8f/b3c8c5b062309e854ce5b726fc101195fbaa881d306ffa5c2ba19efa3af2/multidict-4.5.2.tar.gz")
    version("4.5.1", sha256="985dbf59e92f475573a04598f9a00f92b4fdb64fc41f1df2ea6f33b689319537", url="https://pypi.org/packages/21/30/f08438389a2540b9b2145f47a1ef9e64687a8b90b374e74829d8acd13c0b/multidict-4.5.1.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    # END DEPENDENCIES

