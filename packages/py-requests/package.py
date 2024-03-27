##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyRequests(PythonPackage):
    version("2.31.0", sha256="58cd2187c01e70e6e26505bca751777aa9f2ee0b7f4300988b709f44e013003f", url="https://pypi.org/packages/70/8e/0e2d847013cb52cd35b38c009bb167a1a26b2ce6cd6965bf26b47bc0bf44/requests-2.31.0-py3-none-any.whl")
    version("2.30.0", sha256="10e94cc4f3121ee6da529d358cdaeaff2f1c409cd377dbc72b825852f2f7e294", url="https://pypi.org/packages/96/80/034ffeca15c0f4e01b7b9c6ad0fb704b44e190cde4e757edbd60be404c41/requests-2.30.0-py3-none-any.whl")
    version("2.29.0", sha256="e8f3c9be120d3333921d213eef078af392fba3933ab7ed2d1cba3b56f2568c3b", url="https://pypi.org/packages/cf/e1/2aa539876d9ed0ddc95882451deb57cfd7aa8dbf0b8dbce68e045549ba56/requests-2.29.0-py3-none-any.whl")
    version("2.28.2", sha256="64299f4909223da747622c030b781c0d7811e359c37124b4bd368fb8c6518baa", url="https://pypi.org/packages/d2/f4/274d1dbe96b41cf4e0efb70cbced278ffd61b5c7bb70338b62af94ccb25b/requests-2.28.2-py3-none-any.whl")
    version("2.28.1", sha256="8fefa2a1a1365bf5520aac41836fbee479da67864514bdb821f31ce07ce65349", url="https://pypi.org/packages/ca/91/6d9b8ccacd0412c08820f72cebaa4f0c0441b5cda699c90f618b6f8a1b42/requests-2.28.1-py3-none-any.whl")
    version("2.28.0", sha256="bc7861137fbce630f17b03d3ad02ad0bf978c844f3536d0edda6499dafce2b6f", url="https://pypi.org/packages/41/5b/2209eba8133fc081d3ffff02e1f6376e3117e52bb16f674721a83e67e68e/requests-2.28.0-py3-none-any.whl")
    version("2.27.1", sha256="f22fa1e554c9ddfd16e6e41ac79759e17be9e492b3587efa038054674760e72d", url="https://pypi.org/packages/2d/61/08076519c80041bc0ffa1a8af0cbd3bf3e2b62af10435d269a9d0f40564d/requests-2.27.1-py2.py3-none-any.whl")
    version("2.27.0", sha256="f71a09d7feba4a6b64ffd8e9d9bc60f9bf7d7e19fd0e04362acb1cfc2e3d98df", url="https://pypi.org/packages/47/01/f420e7add78110940639a958e5af0e3f8e07a8a8b62049bac55ee117aa91/requests-2.27.0-py2.py3-none-any.whl")
    version("2.26.0", sha256="6c1246513ecd5ecd4528a0906f910e8f0f9c6b8ec72030dc9fd154dc1a6efd24", url="https://pypi.org/packages/92/96/144f70b972a9c0eabbd4391ef93ccd49d0f2747f4f6a2a2738e99e5adc65/requests-2.26.0-py2.py3-none-any.whl")
    version("2.25.1", sha256="c210084e36a42ae6b9219e00e48287def368a26d03a048ddad7bfee44f75871e", url="https://pypi.org/packages/29/c1/24814557f1d22c56d50280771a17307e6bf87b70727d975fd6b2ce6b014a/requests-2.25.1-py2.py3-none-any.whl")
    version("2.24.0", sha256="fe75cc94a9443b9246fc7049224f75604b113c36acb93f87b80ed42c44cbb898", url="https://pypi.org/packages/45/1e/0c169c6a5381e241ba7404532c16a21d86ab872c9bed8bdcd4c423954103/requests-2.24.0-py2.py3-none-any.whl")
    version("2.23.0", sha256="43999036bfa82904b6af1d99e4882b560e5e2c68e5c4b0aa03b655f3d7d73fee", url="https://pypi.org/packages/1a/70/1935c770cb3be6e3a8b78ced23d7e0f3b187f5cbfab4749523ed65d7c9b1/requests-2.23.0-py2.py3-none-any.whl")
    version("2.22.0", sha256="9cf5292fcd0f598c671cfc1e0d7d1a7f13bb8085e9a590f48c010551dc6c4b31", url="https://pypi.org/packages/51/bd/23c926cd341ea6b7dd0b2a00aba99ae0f828be89d72b2190f27c11d4b7fb/requests-2.22.0-py2.py3-none-any.whl")
    version("2.21.0", sha256="7bf2a778576d825600030a110f3c0e3e8edc51dfaafe1c146e39a2027784957b", url="https://pypi.org/packages/7d/e3/20f3d364d6c8e5d2353c72a67778eb189176f08e873c9900e10c0287b84b/requests-2.21.0-py2.py3-none-any.whl")
    version("2.18.4", sha256="6a1b267aa90cac58ac3a765d067950e7dbbf75b1da07e895d1f594193a40a38b", url="https://pypi.org/packages/49/df/50aa1999ab9bde74656c2919d9c0c085fd2b3775fd3eca826012bef76d8c/requests-2.18.4-py2.py3-none-any.whl")
    version("2.14.2", sha256="3b39cde35be51762885631cf586f4dc2284951b44d479a4454020758d767cc2f", url="https://pypi.org/packages/e4/b0/286e8a936158e5cc5791d5fa3bc4b1d5a7e1ff4e5b3f3766b63d8e97708a/requests-2.14.2-py2.py3-none-any.whl")
    version("2.13.0", sha256="1a720e8862a41aa22e339373b526f508ef0c8988baf48b84d3fc891a8e237efb", url="https://pypi.org/packages/7e/ac/a80ed043485a3764053f59ca92f809cc8a18344692817152b0e8bd3ca891/requests-2.13.0-py2.py3-none-any.whl")
    version("2.11.1", sha256="5acf980358283faba0b897c73959cecf8b841205bb4b2ad3ef545f46eae1a133", url="https://pypi.org/packages/2e/ad/e627446492cc374c284e82381215dcd9a0a87c4f6e90e9789afefe6da0ad/requests-2.11.1.tar.gz")
    version("2.3.0", sha256="1c1473875d846fe563d70868acf05b1953a4472f4695b7b3566d1d978957b8fc", url="https://pypi.org/packages/ab/f9/4425c8410faf7c7d420dbd64e127f2cfb68cfef869a374b332610b6abc09/requests-2.3.0.tar.gz")

    variant("socks", default=False)

    with default_args(type="run"):
        depends_on("py-certifi@2017.4:", when="@2.16:")
        depends_on("py-chardet@3.0.2:4", when="@2.25.1:2.25")
        depends_on("py-chardet@3.0.2:3", when="@2.16:2.25.0")
        depends_on("py-charset-normalizer@2:", when="@2.28.2:")
        depends_on("py-charset-normalizer@2", when="@2.28.1")
        depends_on("py-charset-normalizer@2:2.0", when="@2.26:2.28.0")
        depends_on("py-idna@2.5:", when="@2.26:")
        depends_on("py-idna@2.5:2", when="@2.23:2.25")
        depends_on("py-idna@2.5:2.8", when="@2.21:2.22")
        depends_on("py-idna@2.5:2.6", when="@2.18.4:2.18")
        depends_on("py-pysocks@1.5.6,1.6:", when="@2.12:+socks")
        depends_on("py-urllib3@1.21.1:", when="@2.30:")
        depends_on("py-urllib3@1.21.1:1", when="@2.25:2.29")
        depends_on("py-urllib3@1.21.1:1.24,1.25.2:1.25", when="@2.22:2.24")
        depends_on("py-urllib3@1.21.1:1.24", when="@2.20:2.21")
        depends_on("py-urllib3@1.21.1:1.22", when="@2.18.2:2.18")

