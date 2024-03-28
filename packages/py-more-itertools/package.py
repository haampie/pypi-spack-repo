# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyMoreItertools(PythonPackage):
    # BEGIN VERSIONS
    version("9.1.0", sha256="d2bc7f02446e86a68911e58ded76d6561eea00cddfb2a91e7019bbb586c799f3", url="https://pypi.org/packages/85/01/e2678ee4e0d7eed4fd6be9e5b043fff9d22d245d06c8c91def8ced664189/more_itertools-9.1.0-py3-none-any.whl")
    version("8.14.0", sha256="1bc4f91ee5b1b31ac7ceacc17c09befe6a40a503907baf9c839c229b5095cfd2", url="https://pypi.org/packages/0b/ff/1ad78678bee731ae5414ea5e97396b3f91de32186028daa614d322ac5a8b/more_itertools-8.14.0-py3-none-any.whl")
    version("8.12.0", sha256="43e6dd9942dffd72661a2c4ef383ad7da1e6a3e968a927ad7a6083ab410a688b", url="https://pypi.org/packages/e5/c3/48e2c81038f57e8caab9a6e6fb6c2fc23536c59b092abefc447e6b5d1903/more_itertools-8.12.0-py3-none-any.whl")
    version("8.11.0", sha256="88afff98d83d08fe5e4049b81e2b54c06ebb6b3871a600040865c7a592061cbb", url="https://pypi.org/packages/ea/bc/907239b4c02309ed286dad9577f884f5fdd7bf7f354b961f3d2e3a359db9/more_itertools-8.11.0-py3-none-any.whl")
    version("8.9.0", sha256="70401259e46e216056367a0a6034ee3d3f95e0bf59d3aa6a4eb77837171ed996", url="https://pypi.org/packages/5d/64/8a2bce13c6a98d3625406ff6b7af9c4891fe3bd9b4bbab8299b387c96276/more_itertools-8.9.0-py3-none-any.whl")
    version("7.2.0", sha256="92b8c4b06dac4f0611c0729b2f2ede52b2e1bac1ab48f089c7ddc12e26bb60c4", url="https://pypi.org/packages/45/dc/3241eef99eb45f1def35cf93af35d1cf9ef4c0991792583b8f33ea41b092/more_itertools-7.2.0-py3-none-any.whl")
    version("7.0.0", sha256="2112d2ca570bb7c3e53ea1a35cd5df42bb0fd10c45f0fb97178679c3c03d64c7", url="https://pypi.org/packages/b3/73/64fb5922b745fc1daee8a2880d907d2a70d9c7bb71eea86fcb9445daab5e/more_itertools-7.0.0-py3-none-any.whl")
    version("5.0.0", sha256="fe7a7cae1ccb57d33952113ff4fa1bc5f879963600ed74918f1236e212ee50b9", url="https://pypi.org/packages/a4/a6/42f17d065bda1fac255db13afc94c93dbfb64393eae37c749b4cb0752fc7/more_itertools-5.0.0-py3-none-any.whl")
    version("4.3.0", sha256="c187a73da93e7a8acc0001572aebc7e3c69daf7bf6881a2cea10650bd4420092", url="https://pypi.org/packages/79/b1/eace304ef66bd7d3d8b2f78cc374b73ca03bc53664d78151e9df3b3996cc/more_itertools-4.3.0-py3-none-any.whl")
    version("4.1.0", sha256="0dd8f72eeab0d2c3bd489025bb2f6a1b8342f9b198f6fc37b52d15cfa4531fea", url="https://pypi.org/packages/7a/46/886917c6a4ce49dd3fff250c01c5abac5390d57992751384fe61befc4877/more_itertools-4.1.0-py3-none-any.whl")
    version("2.2", sha256="93e62e05c7ad3da1a233def6731e8285156701e3419a5fe279017c429ec67ce0", url="https://pypi.org/packages/3d/4d/5900efaab46680e3c6c7a2fd87e4531f87e101ec35f6941621dc7f097e82/more-itertools-2.2.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-six@1.0.0:", when="@2.5:5")
    # END DEPENDENCIES

