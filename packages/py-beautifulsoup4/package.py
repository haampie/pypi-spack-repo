##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyBeautifulsoup4(PythonPackage):
    version("4.12.3", sha256="b80878c9f40111313e55da8ba20bdba06d8fa3969fc68304167741bbf9e082ed", url="https://pypi.org/packages/b1/fe/e8c672695b37eecc5cbf43e1d0638d88d66ba3a44c4d321c796f4e59167f/beautifulsoup4-4.12.3-py3-none-any.whl")
    version("4.12.2", sha256="bd2520ca0d9d7d12694a53d44ac482d181b4ec1888909b035a3dbf40d0f57d4a", url="https://pypi.org/packages/57/f4/a69c20ee4f660081a7dedb1ac57f29be9378e04edfcb90c526b923d4bebc/beautifulsoup4-4.12.2-py3-none-any.whl")
    version("4.12.1", sha256="e44795bb4f156d94abb5fbc56efff871c1045bfef72e9efe77558db9f9616ac3", url="https://pypi.org/packages/29/15/236481b1310857378b0d7d00e1a56018fb88e6cab18cc8076d858cdc565b/beautifulsoup4-4.12.1-py3-none-any.whl")
    version("4.12.0", sha256="2130a5ad7f513200fae61a17abb5e338ca980fa28c439c0571014bc0217e9591", url="https://pypi.org/packages/ee/a7/06b189a2e280e351adcef25df532af3c59442123187e228b960ab3238687/beautifulsoup4-4.12.0-py3-none-any.whl")
    version("4.11.2", sha256="0e79446b10b3ecb499c1556f7e228a53e64a2bfcebd455f370d8927cb5b59e39", url="https://pypi.org/packages/c6/ee/16d6f808f5668317d7c23f942091fbc694bcded6aa39678e5167f61b2ba0/beautifulsoup4-4.11.2-py3-none-any.whl")
    version("4.11.1", sha256="58d5c3d29f5a36ffeb94f02f0d786cd53014cf9b3b3951d42e0080d8a9498d30", url="https://pypi.org/packages/9c/d8/909c4089dbe4ade9f9705f143c9f13f065049a9d5e7d34c828aefdd0a97c/beautifulsoup4-4.11.1-py3-none-any.whl")
    version("4.11.0", sha256="577b9e1c36d2ada780d807c5622e889d43172466658c2eb239e97296965cdddb", url="https://pypi.org/packages/85/f6/fcd36aaa9697fa4d84a21c3e9d121fc2cb000ac952d08c606409e671319b/beautifulsoup4-4.11.0-py3-none-any.whl")
    version("4.10.0", sha256="9a315ce70049920ea4572a4055bc4bd700c940521d36fc858205ad4fcde149bf", url="https://pypi.org/packages/69/bf/f0f194d3379d3f3347478bd267f754fc68c11cbf2fe302a6ab69447b1417/beautifulsoup4-4.10.0-py3-none-any.whl")
    version("4.9.3", sha256="84729e322ad1d5b4d25f805bfa05b902dd96450f43842c4e99067d5e1369eb25", url="https://pypi.org/packages/6b/c3/d31704ae558dcca862e4ee8e8388f357af6c9d9acb0cad4ba0fbbd350d9a/beautifulsoup4-4.9.3.tar.gz")
    version("4.9.2", sha256="1edf5e39f3a5bc6e38b235b369128416c7239b34f692acccececb040233032a1", url="https://pypi.org/packages/91/f5/5be6a47f85552586e750b6939b4f21eb4f1b02ef0d0562f1bc3c5fb0ce78/beautifulsoup4-4.9.2.tar.gz")
    version("4.8.0", sha256="25288c9e176f354bf277c0a10aa96c782a6a18a17122dba2e8cec4a97e03343b", url="https://pypi.org/packages/23/7b/37a477bc668068c23cb83e84191ee03709f1fa24d957b7d95083f10dda14/beautifulsoup4-4.8.0.tar.gz")
    version("4.5.3", sha256="b21ca09366fa596043578fd4188b052b46634d22059e68dd0077d9ee77e08a3e", url="https://pypi.org/packages/9b/a5/c6fa2d08e6c671103f9508816588e0fb9cec40444e8e72993f3d4c325936/beautifulsoup4-4.5.3.tar.gz")
    version("4.5.1", sha256="3c9474036afda9136aac6463def733f81017bf9ef3510d25634f335b0c87f5e1", url="https://pypi.org/packages/86/ea/8e9fbce5c8405b9614f1fd304f7109d9169a3516a493ce4f7f77c39435b7/beautifulsoup4-4.5.1.tar.gz")
    version("4.4.1", sha256="87d4013d0625d4789a4f56b8d79a04d5ce6db1152bb65f1d39744f7709a366b4", url="https://pypi.org/packages/26/79/ef9a8bcbec5abc4c618a80737b44b56f1cb393b40238574078c5002b97ce/beautifulsoup4-4.4.1.tar.gz")

    with default_args(type="run"):
        depends_on("py-soupsieve@1.2.1:", when="@4.9:4.9.1,4.10:")
        depends_on("py-soupsieve@1.2:", when="@4.7:4.8")

