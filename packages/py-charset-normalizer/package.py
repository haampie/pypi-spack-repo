# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyCharsetNormalizer(PythonPackage):
    # BEGIN VERSIONS
    version("3.3.2", sha256="f30c3cb33b24454a82faecaf01b19c18562b1e89558fb6c56de4d9118a032fd5", url="https://pypi.org/packages/63/09/c1bc53dab74b1816a00d8d030de5bf98f724c52c1635e07681d312f20be8/charset-normalizer-3.3.2.tar.gz")
    version("3.3.1", sha256="d9137a876020661972ca6eec0766d81aef8a5627df628b664b234b73396e727e", url="https://pypi.org/packages/6d/b3/aa417b4e3ace24067f243e45cceaffc12dba6b8bd50c229b43b3b163768b/charset-normalizer-3.3.1.tar.gz")
    version("3.3.0", sha256="63563193aec44bce707e0c5ca64ff69fa72ed7cf34ce6e11d5127555756fd2f6", url="https://pypi.org/packages/cf/ac/e89b2f2f75f51e9859979b56d2ec162f7f893221975d244d8d5277aa9489/charset-normalizer-3.3.0.tar.gz")
    version("3.2.0", sha256="3bb3d25a8e6c0aedd251753a79ae98a093c7e7b471faa3aa9a93a81431987ace", url="https://pypi.org/packages/2a/53/cf0a48de1bdcf6ff6e1c9a023f5f523dfe303e4024f216feac64b6eb7f67/charset-normalizer-3.2.0.tar.gz")
    version("3.1.0", sha256="34e0a2f9c370eb95597aae63bf85eb5e96826d81e3dcf88b8886012906f509b5", url="https://pypi.org/packages/ff/d7/8d757f8bd45be079d76309248845a04f09619a7b17d6dfc8c9ff6433cac2/charset-normalizer-3.1.0.tar.gz")
    version("3.0.1", sha256="ebea339af930f8ca5d7a699b921106c6e29c617fe9606fa7baa043c1cdae326f", url="https://pypi.org/packages/96/d7/1675d9089a1f4677df5eb29c3f8b064aa1e70c1251a0a8a127803158942d/charset-normalizer-3.0.1.tar.gz")
    version("3.0.0", sha256="b27d10ad15740b45fd55f76e6901a4391e6dca3917ef48ecdcf17edf6e00d770", url="https://pypi.org/packages/fe/77/6d5d367b7cfee812a88573e80bbe25cea2d015ed2c3490e4464951ff3232/charset-normalizer-3.0.0.tar.gz")
    version("2.1.1", sha256="83e9a75d1911279afd89352c68b45348559d1fc0506b054b346651b5e7fee29f", url="https://pypi.org/packages/db/51/a507c856293ab05cdc1db77ff4bc1268ddd39f29e7dc4919aa497f0adbec/charset_normalizer-2.1.1-py3-none-any.whl")
    version("2.1.0", sha256="5189b6f22b01957427f35b6a08d9a0bc45b46d3788ef5a92e978433c7a35f8a5", url="https://pypi.org/packages/94/69/64b11e8c2fb21f08634468caef885112e682b0ebe2908e74d3616eb1c113/charset_normalizer-2.1.0-py3-none-any.whl")
    version("2.0.12", sha256="6881edbebdb17b39b4eaaa821b438bf6eddffb4468cf344f09f89def34a8b1df", url="https://pypi.org/packages/06/b3/24afc8868eba069a7f03650ac750a778862dc34941a4bebeb58706715726/charset_normalizer-2.0.12-py3-none-any.whl")
    version("2.0.11", sha256="2842d8f5e82a1f6aa437380934d5e1cd4fcf2003b06fed6940769c164a480a45", url="https://pypi.org/packages/0c/8e/73ef5366e5c04c2410dab1c74493ca9617a56a27a50f11e01aa4fac2a16c/charset_normalizer-2.0.11-py3-none-any.whl")
    version("2.0.10", sha256="cb957888737fc0bbcd78e3df769addb41fd1ff8cf950dc9e7ad7793f1bf44455", url="https://pypi.org/packages/84/3e/1037abe6498e65d645ce7a22d3402605d49a3b2c7f20c3abb027760da4f0/charset_normalizer-2.0.10-py3-none-any.whl")
    version("2.0.9", sha256="1eecaa09422db5be9e29d7fc65664e6c33bd06f9ced7838578ba40d58bdf3721", url="https://pypi.org/packages/47/84/b06f6729fac8108c5fa3e13cde19b0b3de66ba5538c325496dbe39f5ff8e/charset_normalizer-2.0.9-py3-none-any.whl")
    version("2.0.8", sha256="83fcdeb225499d6344c8f7f34684c2981270beacc32ede2e669e94f7fa544405", url="https://pypi.org/packages/c8/27/141554fc0f42c05dd318fbb0be0e3e018da686544a3ff452762e49ccac58/charset_normalizer-2.0.8-py3-none-any.whl")
    version("2.0.7", sha256="f7af805c321bfa1ce6714c51f254e0d5bb5e5834039bc17db7ebe3a4cec9492b", url="https://pypi.org/packages/de/c8/820b1546c68efcbbe3c1b10dd925fbd84a0dda7438bc18db0ef1fa567733/charset_normalizer-2.0.7-py3-none-any.whl")
    version("2.0.6", sha256="5d209c0a931f215cee683b6445e2d77677e7e75e159f78def0db09d68fafcaa6", url="https://pypi.org/packages/3f/65/69e6754102dcd018a0f29e4db673372eb323ee504431125ab6c9109cb21c/charset_normalizer-2.0.6-py3-none-any.whl")
    version("2.0.5", sha256="fa471a601dfea0f492e4f4fca035cd82155e65dc45c9b83bf4322dfab63755dd", url="https://pypi.org/packages/48/84/aa70b1e0d9d5a76d3d8a4c3d495f8f0524831571f65efe51bb8db8df0eed/charset_normalizer-2.0.5-py3-none-any.whl")
    version("2.0.4", sha256="0c8911edd15d19223366a194a513099a302055a962bca2cec0f54b8b63175d8b", url="https://pypi.org/packages/33/53/b7f6126a2b9fd878b025fe3c40266cfaad696f312165008ce045bffa3fe7/charset_normalizer-2.0.4-py3-none-any.whl")
    version("2.0.3", sha256="88fce3fa5b1a84fdcb3f603d889f723d1dd89b26059d0123ca435570e848d5e1", url="https://pypi.org/packages/c4/1d/e6ce112f7237fc746e632e1cbdc24890cad95505c6cd4b711f4fd17f4735/charset_normalizer-2.0.3-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    # END DEPENDENCIES

