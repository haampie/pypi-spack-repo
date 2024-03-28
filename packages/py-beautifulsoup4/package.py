# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyBeautifulsoup4(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("4.12.3", sha256="b80878c9f40111313e55da8ba20bdba06d8fa3969fc68304167741bbf9e082ed", url="https://pypi.org/packages/b1/fe/e8c672695b37eecc5cbf43e1d0638d88d66ba3a44c4d321c796f4e59167f/beautifulsoup4-4.12.3-py3-none-any.whl")
    version("4.12.2", sha256="bd2520ca0d9d7d12694a53d44ac482d181b4ec1888909b035a3dbf40d0f57d4a", url="https://pypi.org/packages/57/f4/a69c20ee4f660081a7dedb1ac57f29be9378e04edfcb90c526b923d4bebc/beautifulsoup4-4.12.2-py3-none-any.whl")
    version("4.12.1", sha256="e44795bb4f156d94abb5fbc56efff871c1045bfef72e9efe77558db9f9616ac3", url="https://pypi.org/packages/29/15/236481b1310857378b0d7d00e1a56018fb88e6cab18cc8076d858cdc565b/beautifulsoup4-4.12.1-py3-none-any.whl")
    version("4.12.0", sha256="2130a5ad7f513200fae61a17abb5e338ca980fa28c439c0571014bc0217e9591", url="https://pypi.org/packages/ee/a7/06b189a2e280e351adcef25df532af3c59442123187e228b960ab3238687/beautifulsoup4-4.12.0-py3-none-any.whl")
    version("4.11.2", sha256="0e79446b10b3ecb499c1556f7e228a53e64a2bfcebd455f370d8927cb5b59e39", url="https://pypi.org/packages/c6/ee/16d6f808f5668317d7c23f942091fbc694bcded6aa39678e5167f61b2ba0/beautifulsoup4-4.11.2-py3-none-any.whl")
    version("4.11.1", sha256="58d5c3d29f5a36ffeb94f02f0d786cd53014cf9b3b3951d42e0080d8a9498d30", url="https://pypi.org/packages/9c/d8/909c4089dbe4ade9f9705f143c9f13f065049a9d5e7d34c828aefdd0a97c/beautifulsoup4-4.11.1-py3-none-any.whl")
    version("4.11.0", sha256="577b9e1c36d2ada780d807c5622e889d43172466658c2eb239e97296965cdddb", url="https://pypi.org/packages/85/f6/fcd36aaa9697fa4d84a21c3e9d121fc2cb000ac952d08c606409e671319b/beautifulsoup4-4.11.0-py3-none-any.whl")
    version("4.10.0", sha256="9a315ce70049920ea4572a4055bc4bd700c940521d36fc858205ad4fcde149bf", url="https://pypi.org/packages/69/bf/f0f194d3379d3f3347478bd267f754fc68c11cbf2fe302a6ab69447b1417/beautifulsoup4-4.10.0-py3-none-any.whl")
    version("4.9.3", sha256="fff47e031e34ec82bf17e00da8f592fe7de69aeea38be00523c04623c04fb666", url="https://pypi.org/packages/d1/41/e6495bd7d3781cee623ce23ea6ac73282a373088fcd0ddc809a047b18eae/beautifulsoup4-4.9.3-py3-none-any.whl")
    version("4.9.2", sha256="5dfe44f8fddc89ac5453f02659d3ab1668f2c0d9684839f0785037e8c6d9ac8d", url="https://pypi.org/packages/56/f2/6c6c7d0b5483b8c63e837c3f5d941e511979ceb3975ca45fa3ef682df2d6/beautifulsoup4-4.9.2-py3-none-any.whl")
    version("4.8.0", sha256="f040590be10520f2ea4c2ae8c3dae441c7cfff5308ec9d58a0ec0c1b8f81d469", url="https://pypi.org/packages/1a/b7/34eec2fe5a49718944e215fde81288eec1fa04638aa3fb57c1c6cd0f98c3/beautifulsoup4-4.8.0-py3-none-any.whl")
    version("4.5.3", sha256="0a91347d5a4ab2196407ff4d3d758f2e712cae9bdfa3fd1eb0f83edea95e0d8d", url="https://pypi.org/packages/af/a3/9e803f838b3eeb313d45d916d4387cda8572c92e1aafeb53fd43ddb5da2c/beautifulsoup4-4.5.3-py3-none-any.whl")
    version("4.5.1", sha256="35815098d9d0bf5d3a782346a3945b000592d0e93e2538a502d0d6807130d675", url="https://pypi.org/packages/1f/da/4b0d439054fd6b22fa121e0ac672fd8f34f6cce4f375dfd13e955b89306d/beautifulsoup4-4.5.1-py3-none-any.whl")
    version("4.4.1", sha256="2c264254f6cfce64c3bd9d48885208093a73b9095645f600de0a277ce01ea0e5", url="https://pypi.org/packages/cf/69/9abfdab06490af5e0233bcebe3f617ec128486d94ea987ad4f77b9332eef/beautifulsoup4-4.4.1-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    variant("html5lib", default=False)
    variant("lxml", default=False)
    # END VARIANTS

    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-html5lib", when="@4.6.1:+html5lib")
        depends_on("py-lxml", when="@4.6.1:+lxml")
        depends_on("py-soupsieve@1.2.1:", when="@4.9:")
        depends_on("py-soupsieve@1.2:", when="@4.7:4.8")
    # END DEPENDENCIES

