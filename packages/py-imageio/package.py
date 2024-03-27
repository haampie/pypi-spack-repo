##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyImageio(PythonPackage):
    version("2.34.0", sha256="08082bf47ccb54843d9c73fe9fc8f3a88c72452ab676b58aca74f36167e8ccba", url="https://pypi.org/packages/02/25/66533a8390e3763cf8254dee143dbf8a830391ea60d2762512ba7f9ddfbe/imageio-2.34.0-py3-none-any.whl")
    version("2.33.1", sha256="c5094c48ccf6b2e6da8b4061cd95e1209380afafcbeae4a4e280938cce227e1d", url="https://pypi.org/packages/c0/69/3aaa69cb0748e33e644fda114c9abd3186ce369edd4fca11107e9f39c6a7/imageio-2.33.1-py3-none-any.whl")
    version("2.33.0", sha256="d580d6576d0ae39c459a444a23f6f61fe72123a3df2264f5fce8c87784a4be2e", url="https://pypi.org/packages/fa/04/9abe71dfe8c77f5ee58e8c50df3b562884f7494b56c318b867bd2dcb6ec8/imageio-2.33.0-py3-none-any.whl")
    version("2.32.0", sha256="70e63a8955fb08242c9cbc4cdc40728ab892f76955b99cc6a0c5f304b4b84970", url="https://pypi.org/packages/6c/82/681469e10856d28f0367e38dca840c2a5bd768105cef30def31658c136da/imageio-2.32.0-py3-none-any.whl")
    version("2.31.6", sha256="70410af62626a4d725b726ab59138e211e222b80ddf8201c7a6561d694c6238e", url="https://pypi.org/packages/9b/82/473e452d3f21a9cd7e792a827f8df58bdff614fd2fff33d7bf6c4c128da7/imageio-2.31.6-py3-none-any.whl")
    version("2.31.5", sha256="97f68e12ba676f2f4b541684ed81f7f3370dc347e8321bc68ee34d37b2dbac9f", url="https://pypi.org/packages/f6/37/e21e6f38b93878ba80302e95b8ccd4718d80f0c53055ccae343e606b1e2d/imageio-2.31.5-py3-none-any.whl")
    version("2.31.4", sha256="9a39577b482b9c9533b95b436b45540dc32fdf2868ba912d723d3490594fae22", url="https://pypi.org/packages/1a/55/7a7646d7cc42e771d689d39930afcbe57b3d82267544ebabead57ffb86d1/imageio-2.31.4-py3-none-any.whl")
    version("2.31.3", sha256="ea777be55bfa4bd6aee126c7dfa3bf1759bf87be982876c50f1a976d1b65446d", url="https://pypi.org/packages/eb/21/662994d78d8623055f8ffa91838e28f04b2a34bd5d8d6dbc6c7573285ed6/imageio-2.31.3-py3-none-any.whl")
    version("2.31.2", sha256="a78fbcb33432042a4d6993c87f3ea1f136d908318ce7dda857846ccff73294de", url="https://pypi.org/packages/7b/88/59411e1a652ac3338d348901ffa5a73daf1f67fcb3f97d750237d4fa0821/imageio-2.31.2-py3-none-any.whl")
    version("2.31.1", sha256="4106fb395ef7f8dc0262d6aa1bb03daba818445c381ca8b7d5dfc7a2089b04df", url="https://pypi.org/packages/c7/b0/7b6c35b8636ed773325cdb6f5ac3cd36afba63d99e20ed59c521cf5018b4/imageio-2.31.1-py3-none-any.whl")
    version("2.30.0", sha256="e045e9593ed94af41759901d6a51d5313b1e78fc118b6befbbfbf4e9cbe7398a", url="https://pypi.org/packages/26/ae/862bd5b3751d9b7bf8db5fb1595bd06d2875997ca79d85bd5847eb7916af/imageio-2.30.0-py3-none-any.whl")
    version("2.27.0", sha256="24c6ad7d000e64eacc2861c402b6fb128f370cb0a6623cf796d83bca0d0d14d3", url="https://pypi.org/packages/ad/5b/fa636ec082247ffc250c2a16bb262f3405654cbb098a70996d99d59677eb/imageio-2.27.0-py3-none-any.whl")
    version("2.22.0", sha256="aff0e9b5faf4936728f982a1ab63797b1339847a4533c3e4c8343635149dfbfc", url="https://pypi.org/packages/78/7a/3e4e595faea7112785de0a78efd8349a860b2ce6cd4d8fc15afe42c27f5f/imageio-2.22.0-py3-none-any.whl")
    version("2.16.0", sha256="1ee35330318bcb0ce25de778fc1f61555558a159433a568887d7e3d0317ce63c", url="https://pypi.org/packages/58/fc/1547b93534279bbf2de88f7c4a88975a65cecafd32c2bd3c518b2054ef76/imageio-2.16.0-py3-none-any.whl")
    version("2.10.3", sha256="93ee376a8dc96182ead8d773c3ac2becf79c6f2b93d38f31d7ac036c62a6c72e", url="https://pypi.org/packages/17/be/4a836c9262b40454c2834c5ab1a20a35e2f23216b0744f666395fab8a046/imageio-2.10.3-py3-none-any.whl")
    version("2.9.0", sha256="52ddbaeca2dccf53ba2d6dec5676ca7bc3b2403ef8b37f7da78b7654bb3e10f0", url="https://pypi.org/packages/c3/73/f37f428748c4f10a7991ac5bff00f113a34bcc0d0a78957d6e1cdc29a94e/imageio-2.9.0.tar.gz")
    version("2.5.0", sha256="42e65aadfc3d57a1043615c92bdf6319b67589e49a0aae2b985b82144aceacad", url="https://pypi.org/packages/69/4a/0387d708394d5e25d95b1abe427c301614152d1bebea18d9b06fa7199704/imageio-2.5.0.tar.gz")
    version("2.4.1", sha256="16b8077bc8a5fa7a58b3e744f7ecbb156d8c088132df31e0f4f546c98de3514a", url="https://pypi.org/packages/28/b4/cbb592964dfd71a9de6a5b08f882fd334fb99ae09ddc82081dbb2f718c81/imageio-2.4.1.tar.gz")
    version("2.3.0", sha256="c4fd5183c342d47fdc2e98552d14e3f24386021bbc3efedd1e3b579d7d249c07", url="https://pypi.org/packages/99/c5/16b4e3e9078ccb92a8b010455e62bd77585e807aff44028d6c70fc2b62df/imageio-2.3.0.tar.gz")

    with default_args(type="run"):
        depends_on("py-numpy@1.20.0:", when="@2.16")
        depends_on("py-numpy", when="@2.10:2.15,2.17:")
        depends_on("py-pillow@8.3.2:10.0", when="@2.31.6:2.32")
        depends_on("py-pillow@8.3.2:", when="@2.10:2.31.5,2.33:")

