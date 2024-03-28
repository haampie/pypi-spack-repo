# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PySetuptoolsScm(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("8.0.4", sha256="b47844cd2a84b83b3187a5782c71128c28b4c94cad8bfb871da2784a5cb54c4f", url="https://pypi.org/packages/0e/a3/b9a8b0adfe672bf0df5901707aa929d30a97ee390ba651910186776746d2/setuptools_scm-8.0.4-py3-none-any.whl")
    version("8.0.3", sha256="813822234453438a13c78d05c8af29918fbc06f88efb33d38f065340bbb48c39", url="https://pypi.org/packages/ca/04/4ea91c627355ae6d976bf7f1fc2815372a96b1b87bf290c8d726d10a08a1/setuptools_scm-8.0.3-py3-none-any.whl")
    version("8.0.2", sha256="b737bb0f195ae024759188e7080fe15fe6d9353e1b3f6e40b41e4d298f76c147", url="https://pypi.org/packages/cd/ce/7d8579e32a6cf28bf4a71fb0ea49344cf5508bd5edd8ebd19ccfcb5d8640/setuptools_scm-8.0.2-py3-none-any.whl")
    version("8.0.1", sha256="c132f5a8dc508c8113f865c709041d1b15f7d500442220174c38397607797a91", url="https://pypi.org/packages/d4/73/ccf02298d1982cd27c30b3ada350d9952800a38b45bb0cbdb7c7b0110edc/setuptools_scm-8.0.1-py3-none-any.whl")
    version("8.0.0", sha256="f6b9d6deb0f006681d4454bf20c950d333362ade49f7219e75ee75510ac35cf1", url="https://pypi.org/packages/ef/15/a368b4bb2e00531129c942620bef95ed8f9642902669c1d181dfbfbb155b/setuptools_scm-8.0.0-py3-none-any.whl")
    version("7.1.0", sha256="73988b6d848709e2af142aa48c986ea29592bbcfca5375678064708205253d8e", url="https://pypi.org/packages/1d/66/8f42c941be949ef2b22fe905d850c794e7c170a526023612aad5f3a121ad/setuptools_scm-7.1.0-py3-none-any.whl")
    version("7.0.5", sha256="7930f720905e03ccd1e1d821db521bff7ec2ac9cf0ceb6552dd73d24a45d3b02", url="https://pypi.org/packages/01/ed/75a20e7b075e8ecb1f84e8debf833917905d8790b78008915bd68dddd5c4/setuptools_scm-7.0.5-py3-none-any.whl")
    version("7.0.4", sha256="53a6f51451a84d891ca485cec700a802413bbc5e76ee65da134e54c733a6e44d", url="https://pypi.org/packages/1e/6a/2f64fde612daa7c0cdc22e30da5b609a0f67640e5f2f4d08215677090a58/setuptools_scm-7.0.4-py3-none-any.whl")
    version("7.0.3", sha256="7934c856b042199eb44e1523b46abb881726b7d61b3c9b41a756e4ffb4adf73b", url="https://pypi.org/packages/cb/50/a88ad10c10caba0a375123db0dc9ff31c075655eb844135f57691925298f/setuptools_scm-7.0.3-py3-none-any.whl")
    version("7.0.2", sha256="ec120c99027a785c7a349667480a5b2100dfc7d5063e545c93f3735508945aef", url="https://pypi.org/packages/1a/dd/b83708410d912a56e6aa1f78ac1135465eb6a5cfe494628ae24e7dc5922f/setuptools_scm-7.0.2-py3-none-any.whl")
    version("6.3.2", sha256="4c64444b1d49c4063ae60bfe1680f611c8b13833d556fd1d6050c0023162a119", url="https://pypi.org/packages/bc/bf/353180314d0e27929703faf240c244f25ae765e01f595a010cafb209ab51/setuptools_scm-6.3.2-py3-none-any.whl")
    version("6.0.1", sha256="c3bd5f701c8def44a5c0bfe8d407bef3f80342217ef3492b951f3777bd2d915c", url="https://pypi.org/packages/c4/d5/e50358c82026f44cd8810c8165002746cd3f8b78865f6bcf5d7f0fe4f652/setuptools_scm-6.0.1-py3-none-any.whl")
    version("5.0.2", sha256="bd5c4e37f74c103e117549f89aeb3c244488c4a6422df786d1a7d03257f16b34", url="https://pypi.org/packages/6a/18/23ad8654c5c8d91d1238b2d52882e50152473f2bd2db0da60215b51f401b/setuptools_scm-5.0.2-py2.py3-none-any.whl")
    version("5.0.1", sha256="62fa535edb31ece9fa65dc9dcb3056145b8020c8c26c0ef1018aef33db95c40d", url="https://pypi.org/packages/db/6e/2815f7c8561b088ccedc128681e64daac3d6b2e81a9918b007e244dad8b1/setuptools_scm-5.0.1-py2.py3-none-any.whl")
    version("5.0.0", sha256="9fa59c6285aeb804420b660be5513899d947598a854003e351db3ab6c9707bbd", url="https://pypi.org/packages/c0/28/76e9ceb3fba33cd00728663d6df842a31482d4a764d51ead2faecc7b36ec/setuptools_scm-5.0.0-py2.py3-none-any.whl")
    version("4.1.2", sha256="69258e2eeba5f7ce1ed7a5f109519580fa3578250f8e4d6684859f86d1b15826", url="https://pypi.org/packages/ad/d3/e54f8b4cde0f6fb4f231629f570c1a33ded18515411dee6df6fe363d976f/setuptools_scm-4.1.2-py2.py3-none-any.whl")
    version("4.1.1", sha256="a2c0f4e51b3d7fe18303375fff582ca4d8450d4e153e22ef01c71ee3403d93d8", url="https://pypi.org/packages/17/e7/453068431e84588c8931f130022f3cda3759facc38bde69926140b3187f0/setuptools_scm-4.1.1-py2.py3-none-any.whl")
    version("4.1.0", sha256="f6389299354aa41af21358c7e6cb709eb8d31fb2aad83d16b28d36f555c36f54", url="https://pypi.org/packages/de/fb/34de19c07068ef38847f198eec5a362486a5fe2a4d7124e14b47365b605b/setuptools_scm-4.1.0-py2.py3-none-any.whl")
    version("4.0.0", sha256="128944e912ccd63272ba8a3180d5f7366d737d589043eb277735b150da1dbfd4", url="https://pypi.org/packages/e1/57/504a0e46d65fd60614809dbbc9cd07f790aeb555c7f300d92fef94ee1ecb/setuptools_scm-4.0.0-py2.py3-none-any.whl")
    version("3.5.0", sha256="0d23db3d43e0a43eb7196bcf0eb8a4a2eb0561f621ed7ec44b2fdccfd907e38f", url="https://pypi.org/packages/4b/c1/118ec08816737cc46b4dd93b22f7a138fbfb14b53f4b4718fd9983e70a50/setuptools_scm-3.5.0-py2.py3-none-any.whl")
    version("3.4.3", sha256="f7a5091d8de1b1491068623e9acbe7e881d62986e4c0af7f361424622902ff08", url="https://pypi.org/packages/8d/93/d380ad3ee3acdec01ef5fc1096214b57a8cbeab1e5e95eebf5e78b480d94/setuptools_scm-3.4.3-py2.py3-none-any.whl")
    version("3.4.2", sha256="f1036befb98fdb974218095ea6c478367a7a3f812597a525d4576b10659c5980", url="https://pypi.org/packages/b4/23/17dbdfa1202cdb33d7df245b55d4c7b3bce9109d297cccca21c22500aebb/setuptools_scm-3.4.2-py2.py3-none-any.whl")
    version("3.3.3", sha256="1f11cb2eea431346d46589c2dafcafe2e7dc1c7b2c70bc4c3752d2048ad5c148", url="https://pypi.org/packages/1d/70/97966deebaeeda0b81d3cd63ba9f8ec929b838871ed17476de9d8159db3e/setuptools_scm-3.3.3-py2.py3-none-any.whl")
    version("3.1.0", sha256="cc6953d224a22f10e933fa2f55c95979317c55259016adcf93310ba2997febfa", url="https://pypi.org/packages/b2/d5/970632917c53a1fb2751f7da8b288d26546f2b113e4321674051fc9f81e4/setuptools_scm-3.1.0-py2.py3-none-any.whl")
    version("1.15.6", sha256="dac89650c7909d238965e163e10b736cbd3a72f28e2dd5c0fea6cf5e49e8562e", url="https://pypi.org/packages/54/66/00a0e93b02409454af83cfbd782887b5b131dd915af23d53c6651d7cc039/setuptools_scm-1.15.6-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    variant("toml", default=False)
    # END VARIANTS

    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-importlib-metadata@4.6:", when="@8:8.0.2 ^python@:3.9")
        depends_on("py-packaging@20:", when="@6.3:")
        depends_on("py-setuptools@42:", when="@6.3:7+toml")
        depends_on("py-setuptools@45:", when="@6:6.2")
        depends_on("py-setuptools", when="@4:5,6.3:")
        depends_on("py-toml", when="@4:6.0,6.1.0.dev:6.1.0+toml")
        depends_on("py-tomli@1:", when="@7.1: ^python@:3.10")
        depends_on("py-tomli@1:", when="@6.3+toml")
        depends_on("py-tomli@1:", when="@6.2,6.3.1:7.0")
        depends_on("py-typing-extensions", when="@8:8.0.3 ^python@:3.10")
        depends_on("py-typing-extensions", when="@7,8.0.4:")
    # END DEPENDENCIES

