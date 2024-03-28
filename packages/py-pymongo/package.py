# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPymongo(PythonPackage):
    # BEGIN VERSIONS
    version("4.6.2", sha256="ab7d01ac832a1663dad592ccbd92bb0f0775bc8f98a1923c5e1a7d7fead495af", url="https://pypi.org/packages/e6/bb/696f6db3a1e8b696f9a1a4859352a065534a6c70d8070c73a9d7ce134485/pymongo-4.6.2.tar.gz")
    version("4.6.1", sha256="31dab1f3e1d0cdd57e8df01b645f52d43cc1b653ed3afd535d2891f4fc4f9712", url="https://pypi.org/packages/1d/f0/b5fcf9aee64ac3650a3df3bd1d7e8870838a82944fa4868768ab9db5416a/pymongo-4.6.1.tar.gz")
    version("4.6.0", sha256="fb1c56d891f9e34303c451998ef62ba52659648bb0d75b03c5e4ac223a3342c2", url="https://pypi.org/packages/b4/5e/11fad226acae56ef8cfee205bf491f4d50f9c12c5bf3294680006d04de54/pymongo-4.6.0.tar.gz")
    version("4.5.0", sha256="681f252e43b3ef054ca9161635f81b730f4d8cadd28b3f2b2004f5a72f853982", url="https://pypi.org/packages/a3/a6/eae874c4b686dd542e9425ba74a3945a0ebe1247e5801f83ab8b13dcfe59/pymongo-4.5.0.tar.gz")
    version("4.4.1", sha256="a4df87dbbd03ac6372d24f2a8054b4dc33de497d5227b50ec649f436ad574284", url="https://pypi.org/packages/bf/1c/38b956d48667745f2f083937dd31b0467fa3f537480e30c692b1fc4fef3d/pymongo-4.4.1.tar.gz")
    version("4.4.0", sha256="a1b5d286fee4b9b5a0312faede02f2ce2f56ac695685af1d25f428abdac9a22c", url="https://pypi.org/packages/ee/49/f2487573da7a2ee0e19ca488a235a23338b076e670368d447095b634c605/pymongo-4.4.0.tar.gz")
    version("4.3.3", sha256="34e95ffb0a68bffbc3b437f2d1f25fc916fef3df5cdeed0992da5f42fae9b807", url="https://pypi.org/packages/9a/31/482f7401e7bbbeb66ab6b4ac263e2b50435f4329cce1e72378972d48f6b5/pymongo-4.3.3.tar.gz")
    version("4.3.2", sha256="95913659d6c5fc714e662533d014836c988cc1561684f07b6a0a8343651afa66", url="https://pypi.org/packages/d3/ad/6f6f80e0da1f7d18f1505c32dbc4a01cd4c5e712b1d4f5637186409b8da7/pymongo-4.3.2.tar.gz")
    version("4.2.0", sha256="72f338f6aabd37d343bd9d1fdd3de921104d395766bcc5cdc4039e4c2dd97766", url="https://pypi.org/packages/16/5c/def5ee5112e834ce41a86feb37d076b586e51f5ff7acce072073fc616147/pymongo-4.2.0.tar.gz")
    version("4.1.1", sha256="d7b8f25c9b0043cbaf77b8b895814e33e7a3c807a097377c07e1bd49946030d5", url="https://pypi.org/packages/19/5c/ef2753159dfb4e5879e2b091412186f66faae01ce8151761617138c28c91/pymongo-4.1.1.tar.gz")
    version("3.13.0", sha256="e22d6cf5802cd09b674c307cc9e03870b8c37c503ebec3d25b86f2ce8c535dc7", url="https://pypi.org/packages/ec/ff/9b08f29b57384e1f55080d15a12ba4908d93d46cd7fe83c5c562fdcd3400/pymongo-3.13.0.tar.gz")
    version("3.12.3", sha256="0a89cadc0062a5e53664dde043f6c097172b8c1c5f0094490095282ff9995a5f", url="https://pypi.org/packages/97/79/9382c00183979e6cedfb82d7c8d9667a121c19bb2ed66334da930b6f4ef2/pymongo-3.12.3.tar.gz")
    version("3.12.2", sha256="64ea5e97fca1a37f83df9f3460bf63640bc0d725e12f3471e6acbf3a6040dd37", url="https://pypi.org/packages/f0/2f/510ac3c37b514af106a132991bad4ae8c63e0661bf07509455be6516a937/pymongo-3.12.2.tar.gz")
    version("3.12.1", sha256="704879b6a54c45ad76cea7c6789c1ae7185050acea7afd15b58318fa1932ed45", url="https://pypi.org/packages/5f/95/de771196bfc9449097e2d03aedc117d0f7a67a93be7e69b34d7b5e3e9bb0/pymongo-3.12.1.tar.gz")
    version("3.12.0", sha256="b88d1742159bc93a078733f9789f563cef26f5e370eba810476a71aa98e5fbc2", url="https://pypi.org/packages/38/f2/f3e8be03c9994354a5e6c542b6cd76550127f202fcc3a328e1324ee68317/pymongo-3.12.0.tar.gz")
    version("3.9.0", sha256="4249c6ba45587b959292a727532826c5032d59171f923f7f823788f413c2a5a3", url="https://pypi.org/packages/c0/69/9388b715d013444ae8e5d497a6825d120f6a7a67ef5aa8ddea62f601cbff/pymongo-3.9.0.tar.gz")
    version("3.6.0", sha256="c6de26d1e171cdc449745b82f1addbc873d105b8e7335097da991c0fc664a4a8", url="https://pypi.org/packages/69/8a/2384c55f4bd494eeb6104a9b35c36714ba1178dcd08ee5a73b92eed3d8c1/pymongo-3.6.0.tar.gz")
    version("3.3.0", sha256="3d45302fc2622fabf34356ba274c69df41285bac71bbd229f1587283b851b91e", url="https://pypi.org/packages/31/63/5a7826bdee88db6d49ef1737a17de63cf6f50f8cb04f2a0339f048cb33b5/pymongo-3.3.0.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    # END DEPENDENCIES

