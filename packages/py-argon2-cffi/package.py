# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyArgon2Cffi(PythonPackage):
    # BEGIN VERSIONS
    version("23.1.0", sha256="c670642b78ba29641818ab2e68bd4e6a78ba53b7eff7b4c3815ae16abf91c7ea", url="https://pypi.org/packages/a4/6a/e8a041599e78b6b3752da48000b14c8d1e8a04ded09c88c714ba047f34f5/argon2_cffi-23.1.0-py3-none-any.whl")
    version("21.3.0", sha256="8c976986f2c5c0e5000919e6de187906cfd81fb1c72bf9d88c01177e77da7f80", url="https://pypi.org/packages/a8/07/946d5a9431bae05a776a59746ec385fbb79b526738d25e4202d3e0bbf7f4/argon2_cffi-21.3.0-py3-none-any.whl")
    version("21.2.0", sha256="d5d7b9d38963c2769cd0dbfc5901ae00eb9bb98a9cb5a2ea0c9c7c4fec3e6b98", url="https://pypi.org/packages/b8/7d/425d4bd00cd2bcf820e20736a6d9e03a35ce3fea605910cea4a6a4fe674d/argon2_cffi-21.2.0-py3-none-any.whl")
    version("21.1.0", sha256="f710b61103d1a1f692ca3ecbd1373e28aa5e545ac625ba067ff2feca1b2bb870", url="https://pypi.org/packages/7b/39/a26aaef5c3f0c6cfd67c80599b5b40a794fdab46f4ee3be925d71e2f9596/argon2-cffi-21.1.0.tar.gz")
    version("20.1.0", sha256="d8029b2d3e4b4cea770e9e5a0104dd8fa185c1724a0f01528ae4826a6d25f97d", url="https://pypi.org/packages/74/fd/d78e003a79c453e8454197092fce9d1c6099445b7e7da0b04eb4fe1dbab7/argon2-cffi-20.1.0.tar.gz")
    version("19.2.0", sha256="ffaa623eea77b497ffbdd1a51e941b33d3bf552c60f14dbee274c4070677bda3", url="https://pypi.org/packages/e4/96/f1bf2369f29794971f836b8eff5e3bdb653043f1b61d104eae21b1de3ccb/argon2-cffi-19.2.0.tar.gz")
    version("19.1.0", sha256="81548a27b919861040cb928a350733f4f9455dd67c7d1ba92eb5960a1d7f8b26", url="https://pypi.org/packages/aa/bb/d620acb83d6e7d0a1f896557524b85e058500bd858ee814d467428718811/argon2_cffi-19.1.0.tar.gz")
    version("18.3.0", sha256="003f588de43a817af6ecc1c06103fa0801de63849db3cb0f37576bb2da29043d", url="https://pypi.org/packages/31/9b/d52a356fa5a58685868cb6bf812457314780967d9943ce44f07021588edd/argon2_cffi-18.3.0.tar.gz")
    version("18.2.0", sha256="dcb813d41a877820a42dcd3b8450acdef9ce9c8470d1192ae9e1d31f5f4efb22", url="https://pypi.org/packages/d8/76/0e095ad4e3b5bd24c454f147a9e9ffbc291688ebb7e916c26700c026e3de/argon2_cffi-18.2.0.tar.gz")
    version("18.1.0", sha256="7e4b75611b73f53012117ad21cdde7a17b32d1e99ff6799f22d827eb83a2a59b", url="https://pypi.org/packages/e0/b0/89620675b262fc7d5c2cfd87f5b19e612dce5924edd40495520bfa218b8a/argon2_cffi-18.1.0.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-argon2-cffi-bindings", when="@21.2:")
    # END DEPENDENCIES

