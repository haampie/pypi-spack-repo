# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyBitsandbytes(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.42.0", sha256="63798680912cc63bb77b535a2d0860af024e290a52e157f777ad2a52e2585967", url="https://pypi.org/packages/9b/63/489ef9cd7a33c1f08f1b2be51d1b511883c5e34591aaa9873b30021cd679/bitsandbytes-0.42.0-py3-none-any.whl")
    version("0.41.3.post2", sha256="ceb301a3d4e6bf52bdad8d09f3064ac194bdfdeae535994c0315bd2ef7639cca", url="https://pypi.org/packages/d9/8d/b62d4fb02587e293e5b91b68bbcaa2d88c6a0360b622e9521d4bd07a20cd/bitsandbytes-0.41.3.post2-py3-none-any.whl")
    version("0.41.3.post1", sha256="76634534db482538145a82fab1c7fddf9d14c0f24f28bcfee47dd09cbf977d41", url="https://pypi.org/packages/4c/67/b1b0fe832511d597bbb764761eb6f262a2cf30dab55303bdb5cf464b9695/bitsandbytes-0.41.3.post1-py3-none-any.whl")
    version("0.41.3", sha256="0060b1597236a5d52924fc911eb78d0f1482b7183c1d8a89312fb88c559aab86", url="https://pypi.org/packages/1b/db/1a3c0d3542484806c273e8027a328b12be69c1042bb9e134efe93ddf9b50/bitsandbytes-0.41.3-py3-none-any.whl")
    version("0.41.2.post2", sha256="98e5e1979aea3d481ed06181c689f3a154d7f5dc1af770c5173485bc54cf7b72", url="https://pypi.org/packages/c2/49/557f8f4aa9cfc1e9d7875fd850a44a6d3d881a42c483bc8cf56a6b597dfe/bitsandbytes-0.41.2.post2-py3-none-any.whl")
    version("0.41.2.post1", sha256="613a7c7fd994cbd68027eb9f7c0a12d9f81915c70dda20685c27803c9a9fc47a", url="https://pypi.org/packages/f4/4e/6260c56553b6d2e546e7f39a7d44f4705eac03a117f7f2b2b6c29265f689/bitsandbytes-0.41.2.post1-py3-none-any.whl")
    version("0.41.2", sha256="5a2280761dc11c7a23a1be948cfd6a849c2e718012ee34316b979eb6c5634de2", url="https://pypi.org/packages/eb/7b/741589ad16d4dc843a7c57a705e7640e25e3e75ba58767705314e120e271/bitsandbytes-0.41.2-py3-none-any.whl")
    version("0.41.1", sha256="b25228c27636367f222232ed4d1e1502eedd2064be215633734fb8ea0c1c65f4", url="https://pypi.org/packages/1e/2c/af22cd797fc368a9f098ed03015730e6568b884fe67f9940793d944a4b7b/bitsandbytes-0.41.1-py3-none-any.whl")
    version("0.41.0", sha256="dfaebbdcf48bff6628ca04880877a10b4da61e4fff62cdd3433764b1571ab3d1", url="https://pypi.org/packages/b9/33/1cea2d1c909dd3e2b595f7b73c4417f3786c385a4b269a5c40c7699bb14b/bitsandbytes-0.41.0-py3-none-any.whl")
    version("0.40.2", sha256="f0ae26f40c9230c9add9e7c70a10a5ced36fb6deff39906aec1ce4fd25e6ddc0", url="https://pypi.org/packages/32/ea/75961538b08e4ed568057198717aabdebeaf6f398b7692420532e6861754/bitsandbytes-0.40.2-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-scipy", when="@0.42:")
    # END DEPENDENCIES

