##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyAiobotocore(PythonPackage):
    version("2.12.1", sha256="6a9a3d646cf422f45fdc1e4256e78563ebffba64733bc9b8ca9123614e8ba9af", url="https://pypi.org/packages/4d/be/52c4181235cad3e462ac163ae714de37d36bed291efdb4e6591fde119219/aiobotocore-2.12.1-py3-none-any.whl")
    version("2.12.0", sha256="e121503dca049cf361dea19730e335aff2e7508f7f8b24db2e6a43a6fb70299e", url="https://pypi.org/packages/5a/76/5f0f0c933e84fdfd7bf9307c04d1bc2b2528214beac567879ee67e11bcc8/aiobotocore-2.12.0-py3-none-any.whl")
    version("2.11.2", sha256="487fede588040bfa3a43df945275c28c1c73ca75bf705295adb9fbadd2e89be7", url="https://pypi.org/packages/25/cf/c695f7f3301117766d778f536082c41ba20fd01b02e14a5c06f92a5ea75e/aiobotocore-2.11.2-py3-none-any.whl")
    version("2.11.1", sha256="904a7ad7cc8671d662cfd596906dafe839118ea2a66332c37908e3dcfdee1e45", url="https://pypi.org/packages/93/31/96b7a65c1d98238718fac08688ad0fb3ae607c4184074f94407a658b3d19/aiobotocore-2.11.1-py3-none-any.whl")
    version("2.11.0", sha256="6eaf48a6ccd3943ce7d26f75dc8fa0292b7a1a069bd5a9557d37fae5adf14d2d", url="https://pypi.org/packages/7c/1d/0c684405e86928cfdf6af680c5873f68562bcf109ee909e6178be441c5e2/aiobotocore-2.11.0-py3-none-any.whl")
    version("2.10.0", sha256="4fba07909d3e125f3460d6b12e3bcdf3a09b378d71fb09992ca3a555c2eb71f9", url="https://pypi.org/packages/3c/20/19b9bf0d75813afcc01bc1bdc3d603d5ac3f48e179ee9acf3893e4ed715d/aiobotocore-2.10.0-py3-none-any.whl")
    version("2.9.1", sha256="4f8f4074069c115c7558edf1c6e4f78c997fcfb805974e3fe1a8a8442cb923b3", url="https://pypi.org/packages/b9/e7/b5774a802265bfc3a8e3c23e2a79c74b0fd3f6e236efe57c9d7b935aca36/aiobotocore-2.9.1-py3-none-any.whl")
    version("2.9.0", sha256="acf5e49644e6e434b9ecc26284ae7e05d557effbdcdd8185e2eb08925f011853", url="https://pypi.org/packages/c2/28/537fc45d02e653067c5a415b6f472fcbcea3a89a3cc38111ebe0999e305c/aiobotocore-2.9.0-py3-none-any.whl")
    version("2.8.0", sha256="32e632fea387acd45416c2bbc03828ee2c2a66a7dc4bd3a9bcb808dea249c469", url="https://pypi.org/packages/f9/5e/ca5fd1c417f6a1c8cde8519611d82faedb368d7e3684e3a6069c95721bdf/aiobotocore-2.8.0-py3-none-any.whl")
    version("2.7.0", sha256="aec605df77ce4635a0479b50fd849aa6b640900f7b295021ecca192e1140e551", url="https://pypi.org/packages/d0/bc/6a96a686845c9f5958fac0ecafa6050ed77d0e71553b3cfe69acbaa70191/aiobotocore-2.7.0-py3-none-any.whl")
    version("2.5.4", sha256="4b32218728ca3d0be83835b604603a0cd6c329066e884bb78149334267f92440", url="https://pypi.org/packages/20/00/01780c5fa93e3feb6d776ac8c7bd05dbe9290165636c13edcbdde6853537/aiobotocore-2.5.4-py3-none-any.whl")
    version("2.5.0", sha256="9a2a022d7b78ec9a2af0de589916d2721cddbf96264401b78d7a73c1a1435f3b", url="https://pypi.org/packages/91/01/d04cc1e4cc29fcafbca4ca746bf33e03dd5eb51c958738596be7d76a2022/aiobotocore-2.5.0-py3-none-any.whl")
    version("2.4.2", sha256="4acd1ebe2e44be4b100aa553910bda899f6dc090b3da2bc1cf3d5de2146ed208", url="https://pypi.org/packages/90/eb/9902c7ea808d1753a4fd0d5e1a4a87e3bbd609277983c20fa7cd2e6084e5/aiobotocore-2.4.2-py3-none-any.whl")
    version("2.4.1", sha256="26e0d55d5901f487c3467616c028abb85036ca33a0f88e279770adae6b865c69", url="https://pypi.org/packages/b2/9e/a7e3b28cf8dddd938be620fcf389b48f717f713129995272ecf778a48e48/aiobotocore-2.4.1-py3-none-any.whl")
    version("2.4.0", sha256="6c25381d31b712652bc2f6008683949351c240c56d24b1d8ae252c1034a50f63", url="https://pypi.org/packages/75/f3/2fccfdd0a6ade32246547404132d980ffb27461d339ab4b1e3802a152d69/aiobotocore-2.4.0-py3-none-any.whl")
    version("2.1.2", sha256="132a7ccae3bbd35d44dce84a0f4bd77cdac8653f676575afba10ce4879605836", url="https://pypi.org/packages/f3/5f/01fd91f6bd24a14f54f9c03b7cabf51824993a6e3453731a78f26ad2df32/aiobotocore-2.1.2-py3-none-any.whl")
    version("2.1.1", sha256="dbe9ab997851c2458b07a85f682be2ccf35d679d5de0f8f571229f740ad7ba71", url="https://pypi.org/packages/0f/78/da223d2af37066a135c823230a1515c6343e046d4fb14964933f926a5337/aiobotocore-2.1.1.tar.gz")
    version("2.1.0", sha256="5fd4d7aefa0896fe4dd32815ead8a52ed5ccb8016c7c5743fe8ff71c3c074120", url="https://pypi.org/packages/af/71/9fae62115f4a2531a6cb3b40d4304a76265bb56fef0444ea0d4e7c8d7761/aiobotocore-2.1.0.tar.gz")
    version("1.2.1", sha256="58cc422e65fc89f7cb78eca740d241ac8e15f39f6b308cc23152711e8a987d45", url="https://pypi.org/packages/f9/a4/6c6687571b79fe792c627b6fbc31f3437eaf255388f384b5c4853b2b781c/aiobotocore-1.2.1.tar.gz")

    with default_args(type="run"):
        depends_on("py-aiohttp@3.7.4.post:3", when="@2.6:")
        depends_on("py-aiohttp@3.3.1:3", when="@2.5.1:2.5")
        depends_on("py-aiohttp@3.3.1:", when="@0.9.2:1.1,2.1.2:2.1,2.3.4:2.5.0")
        depends_on("py-aioitertools@0.5.1:", when="@0.12:1.1,2.1.2:2.1,2.3.4:")
        depends_on("py-botocore@1.34.41:1.34.51", when="@2.12:")
        depends_on("py-botocore@1.33.2:1.34.34", when="@2.11.2:2.11")
        depends_on("py-botocore@1.33.2:1.34.27", when="@2.11.1")
        depends_on("py-botocore@1.33.2:1.34.22", when="@2.10:2.11.0")
        depends_on("py-botocore@1.33.2:1.33", when="@2.9")
        depends_on("py-botocore@1.32.4:1.33.1", when="@2.8")
        depends_on("py-botocore@1.31.16:1.31.64", when="@2.7")
        depends_on("py-botocore@1.31.17", when="@2.5.3:2.6")
        depends_on("py-botocore@1.29.76", when="@2.5:2.5.0")
        depends_on("py-botocore@1.27.59", when="@2.4")
        depends_on("py-botocore@1.23.24", when="@2.1.2:2.1")
        depends_on("py-wrapt@1.10.10:", when="@0.3.2:0.8,0.9.1:1.1,2.1.2:2.1,2.3.4:")

