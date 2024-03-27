##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyzmq(PythonPackage):
    version("26.0.0-beta2", sha256="89d2ed84e3ee93e11eedc00eb291c787313ed03040c9b6ed9da6efe950cd64f5", url="https://pypi.org/packages/67/10/ab31a95f1733cddda6bbbff5f4a1e339b4390694d5cebe95c627500b1283/pyzmq-26.0.0b2.tar.gz")
    version("26.0.0-beta1", sha256="2ac03c7c6f6cc0237f34c4a78c7cb89d943b0d56bad2d1044879e17af5e01325", url="https://pypi.org/packages/a4/71/a44240bcd3e4d763aeba340358d5e1fbcb0aadbd77f73c1875d503faa1ec/pyzmq-26.0.0b1.tar.gz")
    version("25.1.2", sha256="93f1aa311e8bb912e34f004cf186407a4e90eec4f0ecc0efd26056bf7eda0226", url="https://pypi.org/packages/3a/33/1a3683fc9a4bd64d8ccc0290da75c8f042184a1a49c146d28398414d3341/pyzmq-25.1.2.tar.gz")
    version("25.1.1", sha256="259c22485b71abacdfa8bf79720cd7bcf4b9d128b30ea554f01ae71fdbfdaa23", url="https://pypi.org/packages/3f/7c/69d31a75a3fe9bbab349de7935badac61396f22baf4ab53179a8d940d58e/pyzmq-25.1.1.tar.gz")
    version("25.1.0", sha256="80c41023465d36280e801564a69cbfce8ae85ff79b080e1913f6e90481fb8957", url="https://pypi.org/packages/64/9c/2b2614b0b86ff703b3a33ea5e044923bd7d100adc8c829d579a9b71ea9e7/pyzmq-25.1.0.tar.gz")
    version("25.0.2", sha256="6b8c1bbb70e868dc88801aa532cae6bd4e3b5233784692b786f17ad2962e5149", url="https://pypi.org/packages/bf/7f/24a55c3393d54570f26fa8845e8e42e813bf1b7fb668ed5d3de76b71dbe9/pyzmq-25.0.2.tar.gz")
    version("25.0.1", sha256="44a24f7ce44e70d20e2a4c9ba5af70b4611df7a4b920eed2c8e0bdd5a5af225f", url="https://pypi.org/packages/59/5b/2e1b7498b4a3118bf03b65c16dba9acbe9112f48415a16ae814894033f6a/pyzmq-25.0.1.tar.gz")
    version("25.0.0", sha256="f330a1a2c7f89fd4b0aa4dcb7bf50243bf1c8da9a2f1efc31daf57a2046b31f2", url="https://pypi.org/packages/cf/89/9dbc5bc589a06e94d493b551177a0ebbe70f08b5ebdd49dddf212df869ff/pyzmq-25.0.0.tar.gz")
    version("24.0.1", sha256="216f5d7dbb67166759e59b0479bca82b8acf9bed6015b526b8eb10143fb08e77", url="https://pypi.org/packages/46/0d/b06cf99a64d4187632f4ac9ddf6be99cd35de06fe72d75140496a8e0eef5/pyzmq-24.0.1.tar.gz")
    version("24.0.0", sha256="13b008bd142c9f6079ad75a30504eef2291502e9eac90e722b16fcf9ce856147", url="https://pypi.org/packages/e7/5d/ec9bc6f18d14f9fa6c4aa60e621096f8057c18fc1d2b320e263433abda3f/pyzmq-24.0.0.tar.gz")
    version("23.2.1", sha256="2b381aa867ece7d0a82f30a0c7f3d4387b7cf2e0697e33efaa5bed6c5784abcd", url="https://pypi.org/packages/72/37/d5603f352522e249e44ee767a8a59b3fe7cf7f708a94fd40a637c6890add/pyzmq-23.2.1.tar.gz")
    version("23.2.0", sha256="a51f12a8719aad9dcfb55d456022f16b90abc8dde7d3ca93ce3120b40e3fa169", url="https://pypi.org/packages/36/80/50962c33a3ad813b086fe2bf023bb8b79cb232f8e15b1b54a4d5b05b62ff/pyzmq-23.2.0.tar.gz")
    version("23.1.0", sha256="1df26aa854bdd3a8341bf199064dd6aa6e240f2eaa3c9fa8d217e5d8b868c73e", url="https://pypi.org/packages/cf/9b/166bc53bbe92067ad3771bdc088582c5e54a2fe5118dc417d165bf4fc0aa/pyzmq-23.1.0.tar.gz")
    version("23.0.0", sha256="a45f5c0477d12df05ef2e2922b49b7c0ae9d0f4ff9b6bb0d666558df0ef37122", url="https://pypi.org/packages/5c/35/44e33d61923d603713387c1be6ab10b7b3e1893c0afdcd685915ff7ed058/pyzmq-23.0.0.tar.gz")
    version("22.3.0", sha256="8eddc033e716f8c91c6a2112f0a8ebc5e00532b4a6ae1eb0ccc48e027f9c671c", url="https://pypi.org/packages/6c/95/d37e7db364d7f569e71068882b1848800f221c58026670e93a4c6d50efe7/pyzmq-22.3.0.tar.gz")
    version("22.2.1", sha256="6d18c76676771fd891ca8e0e68da0bbfb88e30129835c0ade748016adb3b6242", url="https://pypi.org/packages/d6/67/98d0d6ac5c784190a0f9728410902471552cffc78cef37830cd86b9cd70d/pyzmq-22.2.1.tar.gz")
    version("22.2.0", sha256="ff6454bd8067463380ea992a7cbe623bd61aeb83a8f19d47eb221eec3f798080", url="https://pypi.org/packages/e6/73/88ff9ae59ee839ad713f1d5d8aa9af7f731114b3ca7eaca06b5772589ac0/pyzmq-22.2.0.tar.gz")
    version("22.1.0", sha256="7040d6dd85ea65703904d023d7f57fab793d7ffee9ba9e14f3b897f34ff2415d", url="https://pypi.org/packages/99/3b/69360102db726741053d1446cbe9f7f06df7e2a6d5b805ee71841abf1cdc/pyzmq-22.1.0.tar.gz")
    version("22.0.3", sha256="f7f63ce127980d40f3e6a5fdb87abf17ce1a7c2bd8bf2c7560e1bbce8ab1f92d", url="https://pypi.org/packages/a3/7a/561526861908d366ddc2764933a6090078654b0f2ff20c3c180dd5851554/pyzmq-22.0.3.tar.gz")
    version("22.0.2", sha256="d7b82a959e5e22d492f4f5a1e650e909a6c8c76ede178f538313ddb9d1e92963", url="https://pypi.org/packages/d7/4f/2e09600112c1e69ea7eefef3db443d966ae670a5b9fa229fe6eb84e945a4/pyzmq-22.0.2.tar.gz")
    version("22.0.1", sha256="f7869dcb80a71ef83f1e1551f0d1ba4831a5c79416a441cb95ac82c9a954ee54", url="https://pypi.org/packages/84/eb/ff6010c207cab902281a6db0ae83b771bf7af5255db088f4d009b1a1fa3d/pyzmq-22.0.1.tar.gz")
    version("22.0.0", sha256="10b86bd04343b1de89ee03ec0bbaac646291de1a6c873228bb9ed22b4d8b32a2", url="https://pypi.org/packages/c0/f6/a5d9550a7938bdd6af54186b784dd20d52e8b2357f632345243e585c58b1/pyzmq-22.0.0.tar.gz")
    version("18.1.0", sha256="93f44739db69234c013a16990e43db1aa0af3cf5a4b8b377d028ff24515fbeb3", url="https://pypi.org/packages/7a/d2/1eb3a994374802b352d4911f3317313a5b4ea786bc830cc5e343dad9b06d/pyzmq-18.1.0.tar.gz")
    version("16.0.2", sha256="0322543fff5ab6f87d11a8a099c4c07dd8a1719040084b6ce9162bcdf5c45c9d", url="https://pypi.org/packages/af/37/8e0bf3800823bc247c36715a52e924e8f8fd5d1432f04b44b8cd7a5d7e55/pyzmq-16.0.2.tar.gz")
    version("14.7.0", sha256="77994f80360488e7153e64e5959dc5471531d1648e3a4bff14a714d074a38cc2", url="https://pypi.org/packages/8c/dd/fa50d34f3698058298e0d3d2817a25b491928e7fedfdf9e1c7e9d47c2d57/pyzmq-14.7.0.tar.gz")


