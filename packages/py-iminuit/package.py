# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyIminuit(PythonPackage):
    # BEGIN VERSIONS
    version("2.8.4", sha256="4b09189f3094896cfc68596adc95b7f1d92772e1de1424e5dc4dd81def56e8b0", url="https://pypi.org/packages/02/93/03a5b0c66b17027400a0e596fec5928e6b895eaf8c46902878ceaecd7902/iminuit-2.8.4.tar.gz")
    version("1.5.2", sha256="0b54f4d4fc3175471398b573d24616ddb8eb7d63808aa370cfc71fc1d636a1fd", url="https://pypi.org/packages/5e/6d/0b61ff0bc43fb12641b3b512b9d9099c826226ce39573f1adf7898157e74/iminuit-1.5.2.tar.gz")
    version("1.3.7", sha256="9173e52cc4a0c0bda13ebfb862f9b074dc5de345b23cb15c1150863aafd8a26c", url="https://pypi.org/packages/47/1a/650dbc6312faa367c47cf393a028c0c65656369f776ae6cbcb44b4a7773d/iminuit-1.3.7.tar.gz")
    version("1.3.6", sha256="d79a197f305d4708a0e3e52b0a6748c1a6997360d2fbdfd09c022995a6963b5e", url="https://pypi.org/packages/01/82/cea3e9db377ba7db6454c1de93c83a39f83e66157dc0d9738c54aaba3d1f/iminuit-1.3.6.tar.gz")
    version("1.2", sha256="7651105fc3f186cfb5742f075ffebcc5088bf7797d8ed124c00977eebe0d1c64", url="https://pypi.org/packages/c9/fd/87931ec898e16557b8f6ae6e576743d00ca085c1cb4eb4673d8f4b02ac20/iminuit-1.2.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-numpy@1.11.3:", when="@1.3.7:1.4")
    # END DEPENDENCIES

