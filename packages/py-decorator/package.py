# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyDecorator(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("5.1.1", sha256="b8c3f85900b9dc423225913c5aace94729fe1fa9763b38939a95226f02d37186", url="https://pypi.org/packages/d5/50/83c593b07763e1161326b3b8c6686f0f4b0f24d5526546bee538c89837d6/decorator-5.1.1-py3-none-any.whl")
    version("5.1.0", sha256="7b12e7c3c6ab203a29e157335e9122cb03de9ab7264b137594103fd4a683b374", url="https://pypi.org/packages/3d/cc/d7b758e54779f7e465179427de7e78c601d3330d6c411ea7ba9ae2f38102/decorator-5.1.0-py3-none-any.whl")
    version("5.0.9", sha256="6e5c199c16f7a9f0e3a61a4a54b3d27e7dad0dbdde92b944426cb20914376323", url="https://pypi.org/packages/6a/36/b1b9bfdf28690ae01d9ca0aa5b0d07cb4448ac65fb91dc7e2d094e3d992f/decorator-5.0.9-py3-none-any.whl")
    version("5.0.8", sha256="77a3141f7f5837b5de43569c35508ca4570022ba501db8c8a2a8b292bd35772a", url="https://pypi.org/packages/85/1d/93f17297fc380fb7591863cc29613cf6cf9c7c5c386a4417d311e32c5ba9/decorator-5.0.8-py3-none-any.whl")
    version("5.0.7", sha256="945d84890bb20cc4a2f4a31fc4311c0c473af65ea318617f13a7257c9a58bc98", url="https://pypi.org/packages/bc/b4/c208a551033a7abb67703be73dea3d917dbce528bd87bcd6f7dfceec7097/decorator-5.0.7-py3-none-any.whl")
    version("5.0.6", sha256="d9f2d2863183a3c0df05f4b786f2e6b8752c093b3547a558f287bf3022fd2bf4", url="https://pypi.org/packages/d8/12/5d214c8f64723366e555b4800d9a9eacd083e99cc782d86fc0b9b1635702/decorator-5.0.6-py3-none-any.whl")
    version("5.0.5", sha256="b7157d62ea3c2c0c57b81a05e4569853e976a3dda5dd7a1cb86be78978c3c5f8", url="https://pypi.org/packages/3e/c4/80311bb66f2a772e9e9d76c54933d0fdbf3202ad194c6282b4c8687ddb32/decorator-5.0.5-py3-none-any.whl")
    version("5.0.4", sha256="7280eff5351d7004144b1f302347328c3d06e84271dbe690a5dc4b17eb586994", url="https://pypi.org/packages/d6/b5/6842d49850e60bf902fb8683019da7a675ea7477839f8127033cd974f5bc/decorator-5.0.4-py3-none-any.whl")
    version("5.0.3", sha256="e3f6d0eb6f1bf4580f872cb4313cb9a2067183e92bb1fbc4e5309285342d3420", url="https://pypi.org/packages/5a/af/44ad6e71be183bf14693572312c5205cab92eb71e6c571a5379c63d381ba/decorator-5.0.3-py3-none-any.whl")
    version("5.0.2", sha256="107200b813feec199120fb042ac03a0b89b18c827a74c0dbb931d1abb856f047", url="https://pypi.org/packages/e7/a2/512ae6eb4a95ecc3216dbd00cc39495c1d284efb8af04bc7d88afc8ca952/decorator-5.0.2-py3-none-any.whl")
    version("4.4.2", sha256="41fa54c2a0cc4ba648be4fd43cff00aedf5b9465c9bf18d64325bc225f08f760", url="https://pypi.org/packages/ed/1b/72a1821152d07cf1d8b6fce298aeb06a7eb90f4d6d41acec9861e7cc6df0/decorator-4.4.2-py2.py3-none-any.whl")
    version("4.4.1", sha256="5d19b92a3c8f7f101c8dd86afd86b0f061a8ce4540ab8cd401fa2542756bce6d", url="https://pypi.org/packages/8f/b7/f329cfdc75f3d28d12c65980e4469e2fa373f1953f5df6e370e84ea2e875/decorator-4.4.1-py2.py3-none-any.whl")
    version("4.4.0", sha256="f069f3a01830ca754ba5258fde2278454a0b5b79e0d7f5c13b3b97e57d4acff6", url="https://pypi.org/packages/5f/88/0075e461560a1e750a0dcbf77f1d9de775028c37a19a346a6c565a257399/decorator-4.4.0-py2.py3-none-any.whl")
    version("4.3.2", sha256="cabb249f4710888a2fc0e13e9a16c343d932033718ff62e1e9bc93a9d3a9122b", url="https://pypi.org/packages/f1/cd/7c8240007e9716b14679bc217a1baefa4432aa30394f7e2ec40a52b1a708/decorator-4.3.2-py2.py3-none-any.whl")
    version("4.3.1", sha256="584a8133ce3d1a63bc31f9ca1719557a2378de418569dd81b3ab46d17bfccf0e", url="https://pypi.org/packages/db/63/7423ff6be74fe33a3021a74521fa2281efcf45ba1cda5be453421387876e/decorator-4.3.1-py2.py3-none-any.whl")
    version("4.3.0", sha256="2c51dff8ef3c447388fe5e4453d24a2bf128d3a4c32af3fabef1f01c6851ab82", url="https://pypi.org/packages/bc/bb/a24838832ba35baf52f32ab1a49b906b5f82fb7c76b2f6a7e35e140bac30/decorator-4.3.0-py2.py3-none-any.whl")
    version("4.0.9", sha256="f4718552326c99544a6ec602d96b7d03ef61180cf4a492c515ecb2438dd14ccc", url="https://pypi.org/packages/7d/ca/493b2377bf42d57bdd985c31975be3d2b500ad9079199cecb7633e8e2cde/decorator-4.0.9-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    # END DEPENDENCIES

