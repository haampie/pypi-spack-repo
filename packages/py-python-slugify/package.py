##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPythonSlugify(PythonPackage):
    version("8.0.4", sha256="276540b79961052b66b7d116620b36518847f52d5fd9e3a70164fc8c50faa6b8", url="https://pypi.org/packages/a4/62/02da182e544a51a5c3ccf4b03ab79df279f9c60c5e82d5e8bec7ca26ac11/python_slugify-8.0.4-py2.py3-none-any.whl")
    version("8.0.3", sha256="c71189c161e8c671f1b141034d9a56308a8a5978cd13d40446c879569212fdd1", url="https://pypi.org/packages/f3/00/d1f681edfd12ba85259932ed08840dc672676e99ffdc8ff34911a8a5f477/python_slugify-8.0.3-py2.py3-none-any.whl")
    version("8.0.2", sha256="428ea9b00c977b8f6c097724398f190b2c18e2a6011094d1001285875ccacdbf", url="https://pypi.org/packages/09/49/e05adaaa2d8604b7cfbce81af14c7a48c67d70a6e06cb47473c9673267db/python_slugify-8.0.2-py2.py3-none-any.whl")
    version("8.0.1", sha256="70ca6ea68fe63ecc8fa4fcf00ae651fc8a5d02d93dcd12ae6d4fc7ca46c4d395", url="https://pypi.org/packages/b4/85/6aa722a11307ec572682023b76cad4c52cda708dfc25fcb4b4a6051da7ab/python_slugify-8.0.1-py2.py3-none-any.whl")
    version("8.0.0", sha256="51f217508df20a6c166c7821683384b998560adcf8f19a6c2ca8b460528ccd9c", url="https://pypi.org/packages/3b/0e/95f48766da1472daa32b50eecbd444bfffda6d451669d27d1d8d56392487/python_slugify-8.0.0-py2.py3-none-any.whl")
    version("7.0.0", sha256="003aee64f9fd955d111549f96c4b58a3f40b9319383c70fad6277a4974bbf570", url="https://pypi.org/packages/63/65/d0d7c085964fdf0cb294299663b407c38e2c8e8dd13bafcf5681798c12db/python_slugify-7.0.0-py2.py3-none-any.whl")
    version("6.1.2", sha256="7b2c274c308b62f4269a9ba701aa69a797e9bca41aeee5b3a9e79e36b6656927", url="https://pypi.org/packages/c1/35/74ab800f1108b95ff9b8e7672a01dbf1f357159e6d06c1f16e983674ff0c/python_slugify-6.1.2-py2.py3-none-any.whl")
    version("6.1.1", sha256="8c0016b2d74503eb64761821612d58fcfc729493634b1eb0575d8f5b4aa1fbcf", url="https://pypi.org/packages/c4/17/3de1cac1ecdb745d36fa33c84c4a1de54b163246374e7d25fe7e77acf967/python_slugify-6.1.1-py2.py3-none-any.whl")
    version("6.1.0", sha256="2e3fad0bf38b11514f8de911ea04e7a6c6a08bb1bac18abd96d9566c34404d56", url="https://pypi.org/packages/ac/3b/1d29efed5d3dff7a80323ab5848603969b408df50d6b70a486c95e91b729/python_slugify-6.1.0-py2.py3-none-any.whl")
    version("6.0.1", sha256="89eec682c5180ba64811c9906a28184bbcc0a35792ba1bda3b5c2ab0cb2d0f67", url="https://pypi.org/packages/21/81/cc25cab7e465d3e15bb1653d4a99c6cee0f6fbdf747f9a99458561642db3/python_slugify-6.0.1-py2.py3-none-any.whl")
    version("4.0.0", sha256="a8fc3433821140e8f409a9831d13ae5deccd0b033d4744d94b31fea141bdd84c", url="https://pypi.org/packages/92/5f/7b84a0bba8a0fdd50c046f8b57dcf179dc16237ad33446079b7c484de04c/python-slugify-4.0.0.tar.gz")

    with default_args(type="run"):
        depends_on("py-text-unidecode@1.3:", when="@5:")

