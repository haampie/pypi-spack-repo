# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyJupytext(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("1.16.1", sha256="796ec4f68ada663569e5d38d4ef03738a01284bfe21c943c485bc36433898bd0", url="https://pypi.org/packages/19/d0/8cc6fb49c36794f15f8ce50f54b9327029a0d738097c085df95b0d1d108f/jupytext-1.16.1-py3-none-any.whl")
    version("1.16.0", sha256="c2b951ac72871f39cd6cd242b56bc43219b7ed8169598bae5359811fb1f54d28", url="https://pypi.org/packages/b4/35/1f396e6745cbaa1aec3624fb6656a77f2e001b324cb4a056aa6a4a436e46/jupytext-1.16.0-py3-none-any.whl")
    version("1.15.2", sha256="ef2a1a3eb8f63d84a3b3772014bdfbe238e4e12a30c4309b8c89e0a54adeb7d1", url="https://pypi.org/packages/9e/e3/3c5b6cce216d090ed6cf6cc258602f836d050738ac02f97cb71675f9cfe3/jupytext-1.15.2-py3-none-any.whl")
    version("1.15.1", sha256="1df0724f97e5c0db9bb5b71ff9ecf4225e2bccbfb49131834424b043edbe8af8", url="https://pypi.org/packages/d2/f5/d5f481cc9edb67c8d017a6eace529152ec496def175a87ce0aa158efc50e/jupytext-1.15.1-py3-none-any.whl")
    version("1.15.0", sha256="7bb7cf4c0a91f5b1591f7558fa3a6494ac6ccf9810d1aa58565d4d9a2675a4a1", url="https://pypi.org/packages/31/a6/7dd0d2da784ce724bd7410f45259279ebc43f34828c423f46028c3cf3ed1/jupytext-1.15.0-py3-none-any.whl")
    version("1.14.7", sha256="ab2fd066dce8112ac95a7c4f9218c1a40d6cefa76b09352c8d08acf21dad5349", url="https://pypi.org/packages/29/bc/fb6ed512e98c426071e5c018822c737c701d31fe72955ad43f9ae4e56cdb/jupytext-1.14.7-py3-none-any.whl")
    version("1.14.6", sha256="6a0f9b1d850b4173115065853b8a81956bbbe6ee7d4a7906e9817cd6f6892414", url="https://pypi.org/packages/d7/51/638c8a4ac54ec8aa89d46d796a816c99c465890e83fb3274e4a6f1b7e680/jupytext-1.14.6-py3-none-any.whl")
    version("1.14.5", sha256="a5dbe60d0ea158bbf82c2bce74aba8d0c220ad7edcda09e017c5eba229b34dc8", url="https://pypi.org/packages/c8/e6/1acb564671a00d7af3448536203bc01a6da7b39064a7a3e8a4de59d8bdfa/jupytext-1.14.5-py3-none-any.whl")
    version("1.14.4", sha256="c5f5647112aa4ea4c61c31e48a216a4c49d315a0fc43d4f483529ed3b0b1a0d9", url="https://pypi.org/packages/fe/1e/5c1bc4b07be7fb84e3e860b46c663c3cb07edc0f45bedeb97b9096c64269/jupytext-1.14.4-py3-none-any.whl")
    version("1.14.3", sha256="baca47bda520937127d1ad46d627b6f3b82089acabdc63e5f36bf1930519e20d", url="https://pypi.org/packages/55/4e/190eb35aa2ec5cdc474f44e26cf21f10c0026b2d059332ab128c9a2abf54/jupytext-1.14.3-py3-none-any.whl")
    version("1.14.1", sha256="216bddba8bbb9355831ba17fd8d45cfe5d1355e7152bc8980f39175fc2584875", url="https://pypi.org/packages/1e/b6/53edfeda6e8ac67a9fd31b510fe8c8e46c1b505805ae958d6fff82f9b2df/jupytext-1.14.1-py3-none-any.whl")
    version("1.13.6", sha256="2160774e30587fb427213231f0267ed070ba4ede41cf6121dbb2b14225eb83ba", url="https://pypi.org/packages/07/3f/18d7d371bd1d74b9ef8a7d14b91f28a609277d849c036d930436ed243b92/jupytext-1.13.6-py3-none-any.whl")
    version("1.13.0", sha256="c31f016c6fc000d88c5aed2cfc58f1acbfb3d9c58898aa0e4bdc3716f3860b09", url="https://pypi.org/packages/f9/c9/24d58379d6c6600aec4dc1ed5c893b6c963a73598bfcb9270d494c3c3896/jupytext-1.13.0-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-markdown-it-py@1.0.0:", when="@1.14.7:")
        depends_on("py-markdown-it-py@1.0.0:2", when="@1.13.8:1.14.6")
        depends_on("py-markdown-it-py@1.0.0:1", when="@1.11.4:1.13.7")
        depends_on("py-mdit-py-plugins", when="@1.11.4:")
        depends_on("py-nbformat", when="@1.10.1-rc0:")
        depends_on("py-packaging", when="@1.16:")
        depends_on("py-pyyaml", when="@1.7.0-rc1:")
        depends_on("py-toml", when="@1.7.0-rc1:")
    # END DEPENDENCIES

