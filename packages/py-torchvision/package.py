# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyTorchvision(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.2.2.post3", sha256="4911188843c10a2c66e8f3d0c3989647e626a7a75b8387e2dbbb3e5aa96887ad", url="https://pypi.org/packages/fb/01/03fd7e503c16b3dc262483e5555ad40974ab5da8b9879e164b56c1f4ef6f/torchvision-0.2.2.post3-py2.py3-none-any.whl")
    version("0.2.2.post2", sha256="4c39bd9e60b4a701807987b5450c70c74bc734f458c67b2aa9ae249f9985034a", url="https://pypi.org/packages/21/9e/3d41372cf9e0f009172a7ad351070657d02e8b424f7efd38433086c82681/torchvision-0.2.2.post2-py2.py3-none-any.whl")
    version("0.2.2", sha256="686cda0037bc904a35593a1394eaf7337edd141b78dc2eadc4667abb6fd569b5", url="https://pypi.org/packages/ce/a1/66d72a2fe580a9f0fcbaaa5b976911fbbde9dce9b330ba12791997b856e9/torchvision-0.2.2-py2.py3-none-any.whl")
    version("0.2.1", sha256="ba0a5e7fa1646d4e7f2e5ad5802d123e17e42a1a9c026d0f79d2fd3a976afba1", url="https://pypi.org/packages/ca/0d/f00b2885711e08bd71242ebe7b96561e6f6d01fdb4b9dcf4d37e2e13c5e1/torchvision-0.2.1-py2.py3-none-any.whl")
    version("0.2.0", sha256="b4aadc07407c37542b94e38f710cfee6e53bb8e8633418094d476c5e417cbc80", url="https://pypi.org/packages/e9/c9/f4eb36734bffd36eb8095247d816cbe6aeca0a2b9218b78678288edfdb92/torchvision-0.2.0-py2.py3-none-any.whl")
    version("0.1.9", sha256="8eb3b60d838188e12cd5f8a8d1ec09910a39f0d6dde712f8eda4079ea093d904", url="https://pypi.org/packages/e2/56/34a58783d2fefe2da5c4558c213386c810e7b2ab04dd8d6fe474a91b695a/torchvision-0.1.9-py2.py3-none-any.whl")
    version("0.1.8", sha256="2885d02c90541a9888b8881a722862ff53bbf73a2d7617d7c670ccd33121029f", url="https://pypi.org/packages/8c/52/33d739bcc547f22c522def535a8da7e6e5a0f6b98594717f519b5cb1a4e1/torchvision-0.1.8-py2.py3-none-any.whl")
    version("0.1.7", sha256="ee509d6b1cb10be6daad4b7e72712d914cae5f7edca61737795e0d7d41c17826", url="https://pypi.org/packages/0f/c0/262ab7e4ff08c3c1c74e02285bc225e8135b25ea527b762f3d690417a657/torchvision-0.1.7-py2.py3-none-any.whl")
    version("0.1.6", sha256="734f95a39d6be2355479b6809278e249cebaa7b6644e57f81c10e8b449e18b5f", url="https://pypi.org/packages/fc/1f/657b9e8c0b2abf3808727543cd00fa62c417efd201a0b2c3703004046204/torchvision-0.1.6-py2-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    variant("ffmpeg", default=False)
    variant("jpeg", default=False)
    variant("nvjpeg", default=False)
    variant("png", default=False)
    variant("video_codec", default=False)
    # END VARIANTS

    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-numpy", when="@0.1.7:")
        depends_on("py-pillow@4.1.1:", when="@0.2:")
        depends_on("py-pillow", when="@0.1.7:0.1")
        depends_on("py-six", when="@0.1.7:")
        depends_on("py-torch", when="@0.1.7:")
        depends_on("py-tqdm@4.19.9:4.19", when="@0.2.2:0.2.2.0")
    # END DEPENDENCIES

