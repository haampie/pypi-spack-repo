##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PySacremoses(PythonPackage):
    version("0.1.1", sha256="31e04c98b169bfd902144824d191825cd69220cdb4ae4bcf1ec58a7db5587b1a", url="https://pypi.org/packages/0b/f0/89ee2bc9da434bd78464f288fdb346bc2932f2ee80a90b2a4bbbac262c74/sacremoses-0.1.1-py3-none-any.whl")
    version("0.1.0", sha256="85354ae5cab89db73f748230c48f514a4feac8cc893654045be9247653135e70", url="https://pypi.org/packages/2e/18/7b4fedbc4e8fa02111b232d9728788e2e817a64b14760530df746514e25f/sacremoses-0.1.0-py3-none-any.whl")
    version("0.0.53", sha256="43715868766c643b35de4b8046cce236bfe59a7fa88b25eaf6ddf02bacf53a7a", url="https://pypi.org/packages/28/78/fef8d089db5b97546fd6d1ff2e813b8544e85670bf3a8c378c9d0250b98d/sacremoses-0.0.53.tar.gz")
    version("0.0.52", sha256="41aa49059ac5ba405bac57307d614275ba4266c0096223d5fa517923dfd10c0a", url="https://pypi.org/packages/bb/b4/e2c0d6eacdec6deb925fd78e2a8f1fd6abbc1c7c06fd65d252c8cea1d3c1/sacremoses-0.0.52.tar.gz")
    version("0.0.51", sha256="54e738e0fc041d485646d6bb4047209c8a5d0896345803a5544a7cc8b7101bed", url="https://pypi.org/packages/9d/68/42bc87b9789eaa48b8787bec466e879f0b139146eb46c807ba4f369eab26/sacremoses-0.0.51.tar.gz")
    version("0.0.50", sha256="2991e69beb2b019abbbe61f946a9a898385fdaa32027119e3a443a95f1c91edc", url="https://pypi.org/packages/40/12/3acb4b28bd6390c8e45dc3583c3b204090e917a18f6c46cafab6fab5047c/sacremoses-0.0.50.tar.gz")
    version("0.0.49", sha256="33ca6d4e125271b9201cc7fdf7f03f3ffdd358ee6dd8079c0432811d82da5377", url="https://pypi.org/packages/db/8b/37b90a3848ff71c0d05ebac5ee6d83f1f81e5f57f26b99a83ebff033303b/sacremoses-0.0.49-py3-none-any.whl")
    version("0.0.48", sha256="32ebd34adc3ea04aae839976687370a9f9f727e6c8730fcb638a32b59f23e283", url="https://pypi.org/packages/3d/0c/49fe18c9466e964ce4b7c9686a1f518afd7ee9725fe168cb2da5d6bfb37f/sacremoses-0.0.48.tar.gz")
    version("0.0.47", sha256="7622c6e9fe12d45b7acf4528451bd054c1557c1f6779398f9cd9f28332d92a0b", url="https://pypi.org/packages/ec/e5/407e634cbd3b96a9ce6960874c5b66829592ead9ac762bd50662244ce20b/sacremoses-0.0.47-py2.py3-none-any.whl")
    version("0.0.46", sha256="f95f80d09d3501fed5c1d3056d9212b40599b08cb27f185d38ff0063be8ddd09", url="https://pypi.org/packages/36/bf/15f8df78bce5eee8223553123173f010d426565980e457c559a71ecbecc3/sacremoses-0.0.46-py3-none-any.whl")
    version("0.0.39", sha256="53fad38b93dd5bf1657a68d52bcca5d681d4246477a764b7791a2abd5c7d1f4c", url="https://pypi.org/packages/e1/e9/fa2e0d101186844bfe35842715a6d9f0a44231838f92fc505c0eb00323fb/sacremoses-0.0.39.tar.gz")

    with default_args(type="run"):
        depends_on("py-click", when="@0.0.45:0.0.47,0.0.49,0.1:")
        depends_on("py-joblib", when="@0.0.45:0.0.47,0.0.49,0.1:")
        depends_on("py-regex", when="@0.0.45:0.0.47,0.0.49,0.1:")
        depends_on("py-six", when="@0.0.45:0.0.47,0.0.49")
        depends_on("py-tqdm", when="@0.0.45:0.0.47,0.0.49,0.1:")

