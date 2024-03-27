##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyRustworkx(PythonPackage):
    version("0.14.2", sha256="bd649322c0649b71fa18cc70a9af027b549560415fa860d6894736029c277b13", url="https://pypi.org/packages/89/a7/f5a793621552cf3e844cb27886a66b875adb1c26f8f254b7cee38a22060e/rustworkx-0.14.2.tar.gz")
    version("0.14.1", sha256="62104ecb0b3d4c2cfdb8b45dc38646bd45760c43fabc70ded9112712d01ea1c9", url="https://pypi.org/packages/bb/0e/a8520a25ccd4b86a620190c90a9ffe1e29f675d624309dd02ece7624a267/rustworkx-0.14.1.tar.gz")
    version("0.14.0", sha256="d630e3dd2984bb3dfa1cc9af5d960c3b970a5c0512551d8340996e9e61e2ca44", url="https://pypi.org/packages/83/b8/01fc71e66f3c5fdeff23e739bce9498770c42ab3fd1190145afd347e3b0d/rustworkx-0.14.0.tar.gz")
    version("0.13.2", sha256="0276cf0b989211859e8797b67d4c16ed6ac9eb32edb67e0a47e70d7d71e80574", url="https://pypi.org/packages/23/f3/b0644cf12d82e8fd5536bbf4f8caf11dabea4d541abe822e307568d7dfc9/rustworkx-0.13.2.tar.gz")
    version("0.13.1", sha256="e76c67896030c9edd9823c2937ac6bfa1ce58bae580a8214596b687b6011a487", url="https://pypi.org/packages/c6/00/0339ecc3c85ff37dd972f95690d13b0e10d24f1031bbf6a0d712493fd2d1/rustworkx-0.13.1.tar.gz")
    version("0.13.0", sha256="9d42059f57a9794c9cbe1c9fc3bca3b72ab00f9d8f24a0efb5ac3829c7f7d6b8", url="https://pypi.org/packages/5f/0f/9c2ff997228ed0ccfe3dd04c84ae151dddbb792b6fd97739316521c72035/rustworkx-0.13.0.tar.gz")
    version("0.12.1", sha256="13a19a2f64dff086b3bffffb294c4630100ecbc13634b4995d9d36a481ae130e", url="https://pypi.org/packages/17/e6/924967efd523c0bfed2868b62c334a3339f21fba0ac4b447089731312159/rustworkx-0.12.1.tar.gz")
    version("0.12.0", sha256="0b871e1463a6677d0fd2fc00adfb774283045d38740bd1b7ea5a1a729de06aa1", url="https://pypi.org/packages/b1/f7/60fe459d27de03eb34dfe083ae09cc71248438d56fffd536c6ba2b45b41c/rustworkx-0.12.0.tar.gz")

    with default_args(type="run"):
        depends_on("py-numpy@1.16.0:1", when="@0.14:")

