##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyMizani(PythonPackage):
    version("0.11.0", sha256="eb03df7f598990cc3159fe80c9d564aa46b67648cdeec8b348025ae2b8577e77", url="https://pypi.org/packages/ce/6a/228b679f183111272027a72da5c993466135f0cdcf7e3544053e52351c43/mizani-0.11.0-py3-none-any.whl")
    version("0.10.0", sha256="2fbe6363b4cc71f063b0c35e993a36df80469b06b7fe7b4b722600f183a2ba5c", url="https://pypi.org/packages/24/db/0bf4870bdc44876172ce7b3dc2fe3d1e15523cc90aafe3996efa9e8ab078/mizani-0.10.0-py3-none-any.whl")
    version("0.9.3", sha256="ac5d49b913de88dc2fb28d82141e9777b97407a6971a158f758093ad5bb820a1", url="https://pypi.org/packages/e2/95/d4e33d3f5bc9fee5512637661208b6b595bda58e9b6a66fa867137761dd7/mizani-0.9.3-py3-none-any.whl")
    version("0.9.2", sha256="e8b7c791041dbb5ba832649922070a6224ccfc7b45e5685f22c9b19a92c048c7", url="https://pypi.org/packages/a2/cd/b9a59133236a3a0554a9197c7951e61d78a69e906ae377ece19c0070cf81/mizani-0.9.2-py3-none-any.whl")
    version("0.9.1", sha256="5214f3904d36566a45a4d3605baa81f629f55254854a540c21aab721a3d377ad", url="https://pypi.org/packages/43/5f/9ad62330d43587d2cf3831c2f06b045568391c2d8f1d31f1e474da9988b2/mizani-0.9.1-py3-none-any.whl")
    version("0.9.0", sha256="04bbacb945975d51569e0b98dd14d07410eb3b28a9ead4e66893dec5349b80c7", url="https://pypi.org/packages/65/62/476c45e4f44e4ee90713a1b35d1b5736f50dcf6cb9aa231d5f9bc75fbf16/mizani-0.9.0-py3-none-any.whl")
    version("0.8.1", sha256="a45f16d1bb420bd92361284252fd29c5e52a20662ad96dfe7a15141a4ca4c287", url="https://pypi.org/packages/a5/6a/738cec3b98020b9cf27bdbfe7c1f385a102300a3d06b2a8ad95f31923dfe/mizani-0.8.1-py3-none-any.whl")
    version("0.8.0", sha256="d054a088be3f527b614e66f3fb081f559e17a2f765d0de4f1dbf7d13f6f08435", url="https://pypi.org/packages/57/e2/09a6342d1695d6a4577d975e06ccfb842ea2239f7f42eb034a99698a3ab3/mizani-0.8.0-py3-none-any.whl")
    version("0.7.4", sha256="f8cd18a4e761846d948ee87429cc84730277d128a46861c719eb6997e6c538a1", url="https://pypi.org/packages/6a/10/999db77b9ce38adc22eb51a869b8c29b6b6fbd9c3b71a627bfee15b8f4d5/mizani-0.7.4-py3-none-any.whl")
    version("0.7.3", sha256="7f95d713e2bd28d51919e065d3453d470a654a0a219a7f777f8e9b6ed6e6ed35", url="https://pypi.org/packages/28/ed/d66698fff045087a220561f2bed1ec4cc9cfc58611a914c1f17bbbc27d05/mizani-0.7.3-py3-none-any.whl")
    version("0.6.0", sha256="da896b6c0e8868d411be0e46c72766596714869912359de44df269496ba9e29b", url="https://pypi.org/packages/e3/76/7a2c9094547ee592f9f43f651ab824aa6599af5e1456250c3f4cc162aece/mizani-0.6.0-py2.py3-none-any.whl")

    with default_args(type="run"):
        depends_on("python@3.9:", when="@0.10:")
        depends_on("py-backports-zoneinfo", when="@0.8:0.9 ^python@:3.8")
        depends_on("py-matplotlib@3.5.0:", when="@0.7.4:0.9")
        depends_on("py-matplotlib@3.1.1:", when="@0.6:0.7.3")
        depends_on("py-numpy@1.23.0:", when="@0.11:")
        depends_on("py-numpy@1.19.0:", when="@0.7.4:0.10")
        depends_on("py-numpy", when="@0.2:0.7.3")
        depends_on("py-palettable", when="@0.2:0.8")
        depends_on("py-pandas@2.1.0:", when="@0.11:")
        depends_on("py-pandas@1.3.5:", when="@0.7.4:0.10")
        depends_on("py-pandas@1.1.0:", when="@0.7.2:0.7.3")
        depends_on("py-pandas@0.25.0:", when="@0.6")
        depends_on("py-scipy@1.7.0:", when="@0.11:")
        depends_on("py-scipy@1.5.0:", when="@0.7.4:0.10")
        depends_on("py-tzdata", when="@0.8: platform=windows")

