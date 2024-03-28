# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyKeyring(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("25.0.0", sha256="9a15cd280338920388e8c1787cb8792b9755dabb3e7c61af5ac1f8cd437cefde", url="https://pypi.org/packages/97/d2/6b63129abee0b6f61c9216dfe918eccc5067fcf67a68e3418ff0935f416a/keyring-25.0.0-py3-none-any.whl")
    version("24.3.1", sha256="df38a4d7419a6a60fea5cef1e45a948a3e8430dd12ad88b0f423c5c143906218", url="https://pypi.org/packages/7c/23/d557507915181687e4a613e1c8a01583fd6d7cb7590e1f039e357fe3b304/keyring-24.3.1-py3-none-any.whl")
    version("24.3.0", sha256="4446d35d636e6a10b8bce7caa66913dd9eca5fd222ca03a3d42c38608ac30836", url="https://pypi.org/packages/e3/e9/c51071308adc273ed612cd308a4b4360ffd291da40b7de2f47c9d6e3a978/keyring-24.3.0-py3-none-any.whl")
    version("24.2.0", sha256="4901caaf597bfd3bbd78c9a0c7c4c29fcd8310dab2cffefe749e916b6527acd6", url="https://pypi.org/packages/0e/8f/5772801169cf62e8232721034f91f81e33b0cfa6e51d3bf6ff65c503af2a/keyring-24.2.0-py3-none-any.whl")
    version("24.1.1", sha256="bc402c5e501053098bcbd149c4ddbf8e36c6809e572c2d098d4961e88d4c270d", url="https://pypi.org/packages/c5/9e/9517ad9978abfd2c579c0f7bd6ff3c549b5e0ea8a0e7ad345879c83a5b87/keyring-24.1.1-py3-none-any.whl")
    version("24.1.0", sha256="ade5e1e7710a7579d7c01e64a712926270239aba48055b1cdc6c022dd6d789b5", url="https://pypi.org/packages/e0/77/9bc91934a369df5578fc54a3cd7ef15ad5825cd5389f91259720dcdd8071/keyring-24.1.0-py3-none-any.whl")
    version("24.0.1", sha256="b3eaa3874e2cffeba2d73e3f275c83827156d0616a2160a610a60d63922ad24b", url="https://pypi.org/packages/78/49/20449ff4bc556d6bfb1ad9335c3e5727a0c5ad853b7f9fbb453013f41c11/keyring-24.0.1-py3-none-any.whl")
    version("24.0.0", sha256="770f609eed2a16c65a6349f3ba1545d00c73f9fed4254c13766c674fe6d0d22b", url="https://pypi.org/packages/94/43/00b79520fab4518ab0e6433fd3cca6e45b25d55619e62e8194ceef074dac/keyring-24.0.0-py3-none-any.whl")
    version("23.13.1", sha256="771ed2a91909389ed6148631de678f82ddc73737d85a927f382a8a1b157898cd", url="https://pypi.org/packages/62/db/0e9a09b2b95986dcd73ac78be6ed2bd73ebe8bac65cba7add5b83eb9d899/keyring-23.13.1-py3-none-any.whl")
    version("23.13.0", sha256="4f4d5c4a2a87d5dbcbb4c7eaf4b106ba5b632c17e7187af86f78016d23d3c96c", url="https://pypi.org/packages/68/a0/4894c336f2fd28d22217e8219caff6d2be3731d09f13c9f580da8855faed/keyring-23.13.0-py3-none-any.whl")
    version("23.12.1", sha256="953a18a7fedd813a6008024042f95d95ce168ebc207c77e7c784c67f6b832631", url="https://pypi.org/packages/f3/2e/5db30581e1618ef6a580e463d77f50781de9f70bcb1483488e514cf65ad2/keyring-23.12.1-py3-none-any.whl")
    version("23.11.0", sha256="3dd30011d555f1345dec2c262f0153f2f0ca6bca041fb1dc4588349bb4c0ac1e", url="https://pypi.org/packages/3a/12/3750c13e0301a65f90f29ed3d5c853d80cea0ef5ae387a5d6866c26685b6/keyring-23.11.0-py3-none-any.whl")
    version("23.10.0", sha256="373e29a1bda7f42247c0db0fa13026c770fa8ff995a7475769357e48743761df", url="https://pypi.org/packages/a9/c7/bb54d8455b61fd0e1a93d0d7cf09ffbde33fca096de964e51b2ecf17a5e7/keyring-23.10.0-py3-none-any.whl")
    version("23.9.3", sha256="69732a15cb1433bdfbc3b980a8a36a04878a6cfd7cb99f497b573f31618001c0", url="https://pypi.org/packages/2a/11/b694ede59e7c677daa2b4201ab4af2d7de2edce7b79a5b51600066aea42e/keyring-23.9.3-py3-none-any.whl")
    version("23.9.2", sha256="e126cffb36da963fad93158b1b8fdf9ee2976f926163f550671241ed20d32799", url="https://pypi.org/packages/cb/c6/a140cf33c9938f7f52ed9cd27dd00011088d9327b6bba66e360fb8e4f0b1/keyring-23.9.2-py3-none-any.whl")
    version("23.9.1", sha256="3565b9e4ea004c96e158d2d332a49f466733d565bb24157a60fd2e49f41a0fd1", url="https://pypi.org/packages/fd/4e/eeaa2a3609cb0074a3cdd910f625adeec95aa1c1b6039816b18f5f7ca3fe/keyring-23.9.1-py3-none-any.whl")
    version("23.9.0", sha256="98f060ec95ada2ab910c195a2d4317be6ef87936a766b239c46aa3c7aac4f0db", url="https://pypi.org/packages/41/75/c2a5d0cc2fb0c690e993d88420c3904a6f735fdb05437c61443ec916c325/keyring-23.9.0-py3-none-any.whl")
    version("23.8.2", sha256="10d2a8639663fe2090705a00b8c47c687cacdf97598ea9c11456679fa974473a", url="https://pypi.org/packages/89/35/05acac64d39ef3944770f9c1ddeec15aa64d3dcb09353922731a00ca3dbc/keyring-23.8.2-py3-none-any.whl")
    version("23.5.0", sha256="b0d28928ac3ec8e42ef4cc227822647a19f1d544f21f96457965dc01cf555261", url="https://pypi.org/packages/0d/bb/8e715dbb1886e6d7e4c6a7024c11a7e137559cd85366f25c67c2bdb311c3/keyring-23.5.0-py3-none-any.whl")
    version("23.2.1", sha256="bd2145a237ed70c8ce72978b497619ddfcae640b6dcf494402d5143e37755c6e", url="https://pypi.org/packages/58/b7/cc5a5321a6119e23ee85745ba204a67d646835e8882ba36eece32ee2b4e1/keyring-23.2.1-py3-none-any.whl")
    version("23.2.0", sha256="66a08700421ed0aaf317c6bf6543f7345f9ab9e7bed6e0ee072f7f6fcddbab75", url="https://pypi.org/packages/7a/18/bfa210920b2602114f804d72cd234cfd3f82ae213e0e4bb79b06561792d6/keyring-23.2.0-py3-none-any.whl")
    version("23.1.0", sha256="b32397fd7e7063f8dd74a26db910c9862fc2109285fa16e3b5208bcb42a3e579", url="https://pypi.org/packages/b5/00/d4ee8383decb2d3dd273a7d62027240e888fddf671ac4398adddd28e8717/keyring-23.1.0-py3-none-any.whl")
    version("23.0.1", sha256="8f607d7d1cc502c43a932a275a56fe47db50271904513a379d39df1af277ac48", url="https://pypi.org/packages/26/f9/41230ac47f738f1ba66676dc8d3b30ca5b1f9eb0230fc204bcd9836c4ae9/keyring-23.0.1-py3-none-any.whl")
    version("21.8.0", sha256="4be9cbaaaf83e61d6399f733d113ede7d1c73bc75cb6aeb64eee0f6ac39b30ea", url="https://pypi.org/packages/d0/a0/20e656cd1e2313af619e382782bd47b5f77a3f33d81992554f3aac56e90d/keyring-21.8.0-py3-none-any.whl")
    version("21.7.0", sha256="4c41ce4f6d1ee91d589a346699ef5a94ba3429603ac8f700cc0097644cdd6748", url="https://pypi.org/packages/e2/23/c15f403d1993a003a711a37318bbe66096c0802b265047919d5c14a4d693/keyring-21.7.0-py3-none-any.whl")
    version("21.6.0", sha256="4a49585d40024826b8eae024c10fece150d020751a9007f5ab793b8f288968f5", url="https://pypi.org/packages/f0/ed/cc938fab7331776e99c18eda0ee8c7b349a5fd803dce4373e9cc9fb9e7b7/keyring-21.6.0-py3-none-any.whl")
    version("21.5.0", sha256="12de23258a95f3b13e5b167f7a641a878e91eab8ef16fafc077720a95e6115bb", url="https://pypi.org/packages/53/14/1c952bcd21255f42f9ba0280d3abd8074dca2c27d136eb749b98ab478f72/keyring-21.5.0-py3-none-any.whl")
    version("21.4.0", sha256="4e34ea2fdec90c1c43d6610b5a5fafa1b9097db1802948e90caf5763974b8f8d", url="https://pypi.org/packages/e4/ed/7be20815f248b0d6aae406783c2bee392640924623c4e17b50ca90c7f74d/keyring-21.4.0-py3-none-any.whl")
    version("21.3.1", sha256="cd4d486803d55bdb13e2d453eb61dbbc984773e4f2b98a455aa85b1f4bc421e4", url="https://pypi.org/packages/3a/6c/0f50bc8811cd7ae39c47f986e645636333e20834270ba7be0954816e5a88/keyring-21.3.1-py3-none-any.whl")
    version("21.3.0", sha256="e7a17caf40c40b6bb8c4772224a487e4a63013560ed0c521065aeba7ecd42182", url="https://pypi.org/packages/59/4d/469272124b46456c425a505a8b5f2d42d2fe95d1181de2d888d684506cf7/keyring-21.3.0-py3-none-any.whl")
    version("21.2.1", sha256="3401234209015144a5d75701e71cb47239e552b0882313e9f51e8976f9e27843", url="https://pypi.org/packages/a8/5e/d13b9feb235d042321a239ac8bc85e90cf3bbe49090c6f1383ac3fd53e0e/keyring-21.2.1-py3-none-any.whl")
    version("21.2.0", sha256="8179b1cdcdcbc221456b5b74e6b7cfa06f8dd9f239eb81892166d9223d82c5ba", url="https://pypi.org/packages/04/21/42d92822959a37ccc390742c2706c8b06cc6a29c10a5ef2e8d22cf0e2e33/keyring-21.2.0-py3-none-any.whl")
    version("20.0.1", sha256="c674f032424b4bffc62abeac5523ec49cc84aed07a480c3233e0baf618efc15c", url="https://pypi.org/packages/f1/07/0afb82d449d210a332d126978634470abdd0c754128a9ead8bbe78eb1b43/keyring-20.0.1-py2.py3-none-any.whl")
    version("18.0.1", sha256="7b29ebfcf8678c4da531b2478a912eea01e80007e5ddca9ee0c7038cb3489ec6", url="https://pypi.org/packages/cb/97/351c4839d78c518d8784822ec6f48f601de5cf47ab21242c0a6e5da888cc/keyring-18.0.1-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-entrypoints", when="@11.1:19.2")
        depends_on("py-importlib-metadata@4.11.4:", when="@23.10: ^python@:3.11")
        depends_on("py-importlib-metadata@3.6:", when="@23.6:23.9 ^python@:3.9")
        depends_on("py-importlib-metadata@3.6:", when="@22.4:23.5")
        depends_on("py-importlib-resources", when="@23.13: ^python@:3.8")
        depends_on("py-jaraco-classes", when="@23.9:")
        depends_on("py-jaraco-context", when="@25:")
        depends_on("py-jaraco-functools", when="@25:")
        depends_on("py-jeepney@0.4.2:", when="@21.1: platform=linux")
        depends_on("py-pywin32-ctypes@0.2:", when="@23.12: platform=windows")
        depends_on("py-pywin32-ctypes@:0.0,0.1.2:", when="@10.4:23.11 platform=windows")
        depends_on("py-secretstorage@3.2:", when="@21.5: platform=linux")
        depends_on("py-secretstorage@3:", when="@21.1:21.4 platform=linux")
        depends_on("py-secretstorage", when="@10:12.0.1,12.1:21.0 platform=linux")
    # END DEPENDENCIES

