##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyTypeguard(PythonPackage):
    version("4.2.1", sha256="7da3bd46e61f03e0852f8d251dcbdc2a336aa495d7daff01e092b55327796eb8", url="https://pypi.org/packages/d9/59/e02336eb478ccdfc9bb0d4c27ce04a4260cd8b45aa04f6b00bcfdbb66a2a/typeguard-4.2.1-py3-none-any.whl")
    version("4.2.0", sha256="24bb8f05ccaee423309daf980ba19e978b18766334ee01994503b853fc44efde", url="https://pypi.org/packages/38/51/055758e85029bf0dec2fd80cc314863e997429eedc5d5ff7b65c5c2e7108/typeguard-4.2.0-py3-none-any.whl")
    version("4.1.5", sha256="8923e55f8873caec136c892c3bed1f676eae7be57cdb94819281b3d3bc9c0953", url="https://pypi.org/packages/18/01/5fc45558268ced46d86292763477996a3cdd505567cd590a688e8cdc386e/typeguard-4.1.5-py3-none-any.whl")
    version("4.1.4", sha256="342dff9923020018f3f1503eee9e32cbe97caa5f2f751388418bd458b68ede49", url="https://pypi.org/packages/7a/11/8eb20601628d36a0e86f35e4db622357d5672b9d3b4491a70365394f4369/typeguard-4.1.4-py3-none-any.whl")
    version("4.1.3", sha256="5b7453b1e3b35fcfe2d62fa4ec500d05e6f2f2eb46f4126ae964677fcc384fff", url="https://pypi.org/packages/84/99/bfa960dcc0386e240f823f7f4b1b028a18126a72216febf892f84b872444/typeguard-4.1.3-py3-none-any.whl")
    version("4.1.2", sha256="e00775920d4c91e93a0db0ed473ecda9cfaca578aed3ce0ed3ba7f3cc38eab9c", url="https://pypi.org/packages/bb/bd/dc7da80c95c920ee2b575e64901b5962ca4a1271b5f3cf6c27242aa0aafc/typeguard-4.1.2-py3-none-any.whl")
    version("4.1.1", sha256="8145b40eaac14d2cd9656a40a763e8928c3519a2d39c43b6478ca20e513fad83", url="https://pypi.org/packages/e9/fe/ce8f006cc033bc839d1bc8280ed31eb125fa17655c4b81b734f235136fa2/typeguard-4.1.1-py3-none-any.whl")
    version("4.1.0", sha256="94a8a8974eca6b980c0fd05a032f283914426ad9f2958b342075358e2744226a", url="https://pypi.org/packages/c4/9d/0918045e44d305ffe1e4c474e81049a2f036b7dec4d4d35483d2b72f353e/typeguard-4.1.0-py3-none-any.whl")
    version("4.0.1", sha256="43f55cc9953f26dae362adb973b6c9ad6b97bfffcc6757277912eddd5cfa345b", url="https://pypi.org/packages/52/55/efeb7d309305e33cd149004cc46ddb697ef5eed7b05507fbba63fe554dbd/typeguard-4.0.1-py3-none-any.whl")
    version("4.0.0", sha256="c4a40af0ba8a41077221271b46d0a6d8d46045443e4d887887c69254ca861952", url="https://pypi.org/packages/5b/8f/88569f7e96b79210c0c06aea80b9c11bfc6779afdc552e8ab489b342d246/typeguard-4.0.0-py3-none-any.whl")
    version("3.0.2", sha256="bbe993854385284ab42fd5bd3bee6f6556577ce8b50696d6cb956d704f286c8e", url="https://pypi.org/packages/e2/62/7d206b0ac6fcbb163215ecc622a54eb747f85ad86d14bc513a834442d0f6/typeguard-3.0.2-py3-none-any.whl")
    version("2.13.3", sha256="5e3e3be01e887e7eafae5af63d1f36c849aaa94e3a0112097312aabfa16284f1", url="https://pypi.org/packages/9a/bb/d43e5c75054e53efce310e79d63df0ac3f25e34c926be5dffb7d283fb2a8/typeguard-2.13.3-py3-none-any.whl")
    version("2.13.2", sha256="4f7da3d80dda5e42d6973f11f33da3542b8bf86edc12ba926b2dbad62adf3fcf", url="https://pypi.org/packages/95/23/08b5774e60ad676a898cf27dc18744a5d73a5f93db6e8ce0ea2d908dca59/typeguard-2.13.2-py3-none-any.whl")
    version("2.13.1", sha256="33545edfd616f414690203fe431159b30f971c43b47e0caea8b81fa10e1e943e", url="https://pypi.org/packages/8d/67/5ada22f7784ad1eb689ae36da7b88a211b8684d5cdbf48ff0c29a286412f/typeguard-2.13.1-py3-none-any.whl")
    version("2.13.0", sha256="0bc44d1ff865b522eda969627868b0e001c8329296ce50aededbea03febc79ee", url="https://pypi.org/packages/55/55/5438ba6879e7ea539108027cffff5e0933cc395c60ed3ae8eb3f87ebcad6/typeguard-2.13.0-py3-none-any.whl")
    version("2.12.1", sha256="cc15ef2704c9909ef9c80e19c62fb8468c01f75aad12f651922acf4dbe822e02", url="https://pypi.org/packages/a0/88/2a1613174e7d05540358b2f19881f369bfe6ba737f0a673177e69eb623df/typeguard-2.12.1-py3-none-any.whl")
    version("2.12.0", sha256="7d1cf82b35e9ff3cd083133ebda54ad1d7a40296471397e6c6b229cf07fe5307", url="https://pypi.org/packages/06/1f/c10ad900a10e1421b85d20f1c9d1748469ef5a34296693a02be887af5f95/typeguard-2.12.0-py3-none-any.whl")
    version("2.11.1", sha256="c62706201ec6c14962162fa67d70bd2762753247533d70ff2442e5ac08f94fa2", url="https://pypi.org/packages/50/0f/788beaef5b73aacaae1eea11b1165fd4dec0a4c600fb2cb1611f55caf4ce/typeguard-2.11.1-py3-none-any.whl")
    version("2.11.0", sha256="5d12bbf114a975fd0fe02d9a035ec2b29cf753db8eb62d7288f6fe80f3e1739c", url="https://pypi.org/packages/d6/bf/f00c9b67afaf6ca8d3a26f6158490aba286bb465b9e9fba039dc0c23062d/typeguard-2.11.0-py3-none-any.whl")
    version("2.10.0", sha256="a75c6d86ac9d1faf85c5ae952de473e5d26824dda6d4394ff6bc676849cfb939", url="https://pypi.org/packages/f3/28/cc6df4c26d14c338c9744dc510a8c7f1a9115f8233e7602cca140a61430c/typeguard-2.10.0-py3-none-any.whl")

    with default_args(type="run"):
        depends_on("py-importlib-metadata@3.6:", when="@3: ^python@:3.9")
        depends_on("py-typing-extensions@4.10.0:", when="@4.2.1: ^python@:3.12")
        depends_on("py-typing-extensions@4.7.0:", when="@4.0.1:4.2.0 ^python@:3.11")
        depends_on("py-typing-extensions@4.4:", when="@3.0.0-rc1:4.0.0 ^python@:3.10")

