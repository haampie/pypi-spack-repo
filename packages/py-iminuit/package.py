##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyIminuit(PythonPackage):
    version("2.25.2", sha256="3bf8a1b96865a60cedf29135f4feae09fa7c66237d29f68ded64e97a823a9b3e", url="https://pypi.org/packages/78/f1/416e559122a3872878853429a87143b4b4f5d33e23c1317be8a270e875aa/iminuit-2.25.2.tar.gz")
    version("2.25.1", sha256="b829ffc1db5ed671dcd1a49e04593776e6575cf3a66cc7ce7477fc66423f863e", url="https://pypi.org/packages/75/d5/3f6fab636a6406bf960477b26d81302bf7414d2ecef87e8b4c5bcfdf99fe/iminuit-2.25.1.tar.gz")
    version("2.25.0", sha256="7bdf59460d390f2d03ce755c0151b2ec3d203300bc51541bf8287b43c1204c66", url="https://pypi.org/packages/a6/e3/9172082f134a68e79339534dcc87fee02397ece8222e2661c6d08a521eb3/iminuit-2.25.0.tar.gz")
    version("2.24.0", sha256="25ab631c3c8e024b1bcc7c96f66338caac54a4a2324d55f1e3ba5617816e44fd", url="https://pypi.org/packages/52/09/fa129a555e36ee059d63b841ac3542685330352261d890548283244f7f2a/iminuit-2.24.0.tar.gz")
    version("2.23.0", sha256="98f1589eb18d4882232ff1556d62e7ca19c91bbab7524ac8b405261a674452a1", url="https://pypi.org/packages/53/ca/fbf6026f8912dff617c28a188dc9ec01fc5dd956f65665211a18165818fc/iminuit-2.23.0.tar.gz")
    version("2.22.0", sha256="e0ccc37bad8bc1bd3b9d3fa07d28d4c0407e25a888faa9b559be2d9afbd2d97c", url="https://pypi.org/packages/11/9c/c472fde7ae390588946ecc1ab44b9d7cd07d05d16b2379c584d017e98df6/iminuit-2.22.0.tar.gz")
    version("2.21.3", sha256="fb313f0cc27e221b9b221bcd779b3a668fb4c77b0f90abfd5336833ecbdac016", url="https://pypi.org/packages/be/95/a2888ba5fdcea6736370ad2aa988d3c471daf6287bca534897c5c72351d3/iminuit-2.21.3.tar.gz")
    version("2.21.2", sha256="449b738f21e3d57510b3c786eefc867ba03a78e94351e0a05450f8db4c034a74", url="https://pypi.org/packages/e5/1b/6975bc5348c86b9f4e67783f5a8c24ebc2e184b755ecf16c3e00cc5a7b97/iminuit-2.21.2.tar.gz")
    version("2.21.1", sha256="b151059621e252b6ca310a16d044b82c329521346b9d5d0668cdb14421cb5e0f", url="https://pypi.org/packages/82/dc/a005ccf61cb7c33998179d4f1054ce804c0fcd31b9509508693bb647cdf0/iminuit-2.21.1.tar.gz")
    version("2.21.0", sha256="8af46cc1e688be488171e4df008e39ef037eb5b9ed277b781d3ca759fdbdbc02", url="https://pypi.org/packages/01/53/40d7ecf0d511c4f76cf831ec60123505351109d864a5d78dcee8bf2e297d/iminuit-2.21.0.tar.gz")
    version("2.8.4", sha256="4b09189f3094896cfc68596adc95b7f1d92772e1de1424e5dc4dd81def56e8b0", url="https://pypi.org/packages/02/93/03a5b0c66b17027400a0e596fec5928e6b895eaf8c46902878ceaecd7902/iminuit-2.8.4.tar.gz")
    version("1.5.2", sha256="0b54f4d4fc3175471398b573d24616ddb8eb7d63808aa370cfc71fc1d636a1fd", url="https://pypi.org/packages/5e/6d/0b61ff0bc43fb12641b3b512b9d9099c826226ce39573f1adf7898157e74/iminuit-1.5.2.tar.gz")
    version("1.3.7", sha256="9173e52cc4a0c0bda13ebfb862f9b074dc5de345b23cb15c1150863aafd8a26c", url="https://pypi.org/packages/47/1a/650dbc6312faa367c47cf393a028c0c65656369f776ae6cbcb44b4a7773d/iminuit-1.3.7.tar.gz")
    version("1.3.6", sha256="d79a197f305d4708a0e3e52b0a6748c1a6997360d2fbdfd09c022995a6963b5e", url="https://pypi.org/packages/01/82/cea3e9db377ba7db6454c1de93c83a39f83e66157dc0d9738c54aaba3d1f/iminuit-1.3.6.tar.gz")
    version("1.2", sha256="7651105fc3f186cfb5742f075ffebcc5088bf7797d8ed124c00977eebe0d1c64", url="https://pypi.org/packages/c9/fd/87931ec898e16557b8f6ae6e576743d00ca085c1cb4eb4673d8f4b02ac20/iminuit-1.2.tar.gz")

    with default_args(type="run"):
        depends_on("py-numpy@1.21.0:", when="@2.22:")
        depends_on("py-numpy@1.11.3:", when="@1.3.7:1.4")
        depends_on("py-typing-extensions", when="@2.22: ^python@:3.8")

