##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyMoreItertools(PythonPackage):
    version("10.2.0", sha256="686b06abe565edfab151cb8fd385a05651e1fdf8f0a14191e4439283421f8684", url="https://pypi.org/packages/50/e2/8e10e465ee3987bb7c9ab69efb91d867d93959095f4807db102d07995d94/more_itertools-10.2.0-py3-none-any.whl")
    version("10.1.0", sha256="64e0735fcfdc6f3464ea133afe8ea4483b1c5fe3a3d69852e6503b43a0b222e6", url="https://pypi.org/packages/5a/cb/6dce742ea14e47d6f565589e859ad225f2a5de576d7696e0623b784e226b/more_itertools-10.1.0-py3-none-any.whl")
    version("10.0.0", sha256="928d514ffd22b5b0a8fce326d57f423a55d2ff783b093bab217eda71e732330f", url="https://pypi.org/packages/51/6e/7c6688d94e350c006f89f84e1c6af37a857f5d302bc7a3ddf917a4470948/more_itertools-10.0.0-py3-none-any.whl")
    version("9.1.0", sha256="d2bc7f02446e86a68911e58ded76d6561eea00cddfb2a91e7019bbb586c799f3", url="https://pypi.org/packages/85/01/e2678ee4e0d7eed4fd6be9e5b043fff9d22d245d06c8c91def8ced664189/more_itertools-9.1.0-py3-none-any.whl")
    version("9.0.0", sha256="250e83d7e81d0c87ca6bd942e6aeab8cc9daa6096d12c5308f3f92fa5e5c1f41", url="https://pypi.org/packages/5d/87/1ec3fcc09d2c04b977eabf8a1083222f82eaa2f46d5a4f85f403bf8e7b30/more_itertools-9.0.0-py3-none-any.whl")
    version("8.14.0", sha256="1bc4f91ee5b1b31ac7ceacc17c09befe6a40a503907baf9c839c229b5095cfd2", url="https://pypi.org/packages/0b/ff/1ad78678bee731ae5414ea5e97396b3f91de32186028daa614d322ac5a8b/more_itertools-8.14.0-py3-none-any.whl")
    version("8.13.0", sha256="c5122bffc5f104d37c1626b8615b511f3427aa5389b94d61e5ef8236bfbc3ddb", url="https://pypi.org/packages/bd/3f/c4b3dbd315e248f84c388bd4a72b131a29f123ecacc37ffb2b3834546e42/more_itertools-8.13.0-py3-none-any.whl")
    version("8.12.0", sha256="43e6dd9942dffd72661a2c4ef383ad7da1e6a3e968a927ad7a6083ab410a688b", url="https://pypi.org/packages/e5/c3/48e2c81038f57e8caab9a6e6fb6c2fc23536c59b092abefc447e6b5d1903/more_itertools-8.12.0-py3-none-any.whl")
    version("8.11.0", sha256="88afff98d83d08fe5e4049b81e2b54c06ebb6b3871a600040865c7a592061cbb", url="https://pypi.org/packages/ea/bc/907239b4c02309ed286dad9577f884f5fdd7bf7f354b961f3d2e3a359db9/more_itertools-8.11.0-py3-none-any.whl")
    version("8.10.0", sha256="56ddac45541718ba332db05f464bebfb0768110111affd27f66e0051f276fa43", url="https://pypi.org/packages/e0/1f/9cd11889680dc55a3612a277c8310def3f2bfc7159f12fcb647e32350380/more_itertools-8.10.0-py3-none-any.whl")
    version("8.9.0", sha256="70401259e46e216056367a0a6034ee3d3f95e0bf59d3aa6a4eb77837171ed996", url="https://pypi.org/packages/5d/64/8a2bce13c6a98d3625406ff6b7af9c4891fe3bd9b4bbab8299b387c96276/more_itertools-8.9.0-py3-none-any.whl")
    version("7.2.0", sha256="92b8c4b06dac4f0611c0729b2f2ede52b2e1bac1ab48f089c7ddc12e26bb60c4", url="https://pypi.org/packages/45/dc/3241eef99eb45f1def35cf93af35d1cf9ef4c0991792583b8f33ea41b092/more_itertools-7.2.0-py3-none-any.whl")
    version("7.0.0", sha256="2112d2ca570bb7c3e53ea1a35cd5df42bb0fd10c45f0fb97178679c3c03d64c7", url="https://pypi.org/packages/b3/73/64fb5922b745fc1daee8a2880d907d2a70d9c7bb71eea86fcb9445daab5e/more_itertools-7.0.0-py3-none-any.whl")
    version("5.0.0", sha256="38a936c0a6d98a38bcc2d03fdaaedaba9f412879461dd2ceff8d37564d6522e4", url="https://pypi.org/packages/dd/26/30fc0d541d9fdf55faf5ba4b0fd68f81d5bd2447579224820ad525934178/more-itertools-5.0.0.tar.gz")
    version("4.3.0", sha256="c476b5d3a34e12d40130bc2f935028b5f636df8f372dc2c1c01dc19681b2039e", url="https://pypi.org/packages/88/ff/6d485d7362f39880810278bdc906c13300db05485d9c65971dec1142da6a/more-itertools-4.3.0.tar.gz")
    version("4.1.0", sha256="c9ce7eccdcb901a2c75d326ea134e0886abfbea5f93e91cc95de9507c0816c44", url="https://pypi.org/packages/db/0b/f5660bf6299ec5b9f17bd36096fa8148a1c843fa77ddfddf9bebac9301f7/more-itertools-4.1.0.tar.gz")
    version("2.2", sha256="93e62e05c7ad3da1a233def6731e8285156701e3419a5fe279017c429ec67ce0", url="https://pypi.org/packages/3d/4d/5900efaab46680e3c6c7a2fd87e4531f87e101ec35f6941621dc7f097e82/more-itertools-2.2.tar.gz")

    with default_args(type="run"):
        depends_on("py-six@1.0.0:", when="@2.5:5")

