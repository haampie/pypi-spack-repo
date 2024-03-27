##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyXxhash(PythonPackage):
    version("3.4.1", sha256="0379d6cf1ff987cd421609a264ce025e74f346e3e145dd106c0cc2e3ec3f99a9", url="https://pypi.org/packages/04/ef/1a95dc97a71b128a7c5fd531e42574b274629a4ad1354a694087e2305467/xxhash-3.4.1.tar.gz")
    version("3.4.0", sha256="f8b0487f9227ecee8bcd73f1fc4c41b01fa14ad56ad2a5ff677a72995e5bb762", url="https://pypi.org/packages/81/d3/df9d36a63333344b4112ce1ab0d6318bd016bca1d927d91189375020e0ce/xxhash-3.4.0.tar.gz")
    version("3.3.0", sha256="c3f9e322b1ebeebd44e3d9d2d9b124e0c550c1ef41bd552afdcdd719516ee41a", url="https://pypi.org/packages/07/5f/6951f7496b0a452f3e79e39d48e7166b3445d1e064691b7df99d1ee80196/xxhash-3.3.0.tar.gz")
    version("3.2.0", sha256="1afd47af8955c5db730f630ad53ae798cf7fae0acb64cebb3cf94d35c47dd088", url="https://pypi.org/packages/24/90/666a4d4d96a93ddaaaa0142ef8c1bd20f7135a7f1114a894f4d6efac16c5/xxhash-3.2.0.tar.gz")
    version("3.1.0", sha256="ac21b1e21dc6fdfee9a57b53f4777539d53a84f2e1546a3f802f159f9966bdc1", url="https://pypi.org/packages/9b/58/863e9ca03abd547f6fd1a9ffbbfca6c07e6c9a930af4ca06bc85210594f9/xxhash-3.1.0.tar.gz")
    version("3.0.0", sha256="30b2d97aaf11fb122023f6b44ebb97c6955e9e00d7461a96415ca030b5ceb9c7", url="https://pypi.org/packages/20/3e/ca49932bade8b3308e74df951c36cbc84c8230c9b8715bae1e0014831aa7/xxhash-3.0.0.tar.gz")
    version("2.0.2", sha256="b7bead8cf6210eadf9cecf356e17af794f57c0939a3d420a00d87ea652f87b49", url="https://pypi.org/packages/d6/1d/c06f2eeb658d6f6c2b463334c0e7c3feb761d5d9b207de6017945b2e4744/xxhash-2.0.2.tar.gz")
    version("2.0.1", sha256="347eb6e2af58eed76916d71dd9891976a8d5fc49fa796cb060411d1936ebdb6c", url="https://pypi.org/packages/0a/84/6165d7c85094bb81dbe95d9b068dcc91f4ef6371347f2a4f6310210554ba/xxhash-2.0.1.tar.gz")
    version("2.0.0", sha256="58ca818554c1476fa1456f6cd4b87002e2294f09baf0f81e5a2a4968e62c423c", url="https://pypi.org/packages/6b/64/684870b30b21842618bf3b76378fd32eda944aeb164090746b9a8b70232f/xxhash-2.0.0.tar.gz")
    version("1.4.4", sha256="7d6df9d217977d085b8abd74b61efa40405ac416f2d8bdacc40826bd5cb1b746", url="https://pypi.org/packages/e4/bc/336b9f0c1910ca7efd0c77926f108fe4ebf9451764b434067fa2b3c276b1/xxhash-1.4.4.tar.gz")


