# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyKerasPreprocessing(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("1.1.2", sha256="7b82029b130ff61cc99b55f3bd27427df4838576838c5b2f65940e4fcec99a7b", url="https://pypi.org/packages/79/4c/7c3275a01e12ef9368a892926ab932b33bb13d55794881e3573482b378a7/Keras_Preprocessing-1.1.2-py2.py3-none-any.whl")
    version("1.1.1", sha256="138012da7bbc5508d59681515636c01618644322db08c1f4c6d66e63de8ddb73", url="https://pypi.org/packages/5e/ac/d66d66e98b572559028ddbcd47df341a467ee438b185fa18f47f0eec8890/Keras_Preprocessing-1.1.1-py2.py3-none-any.whl")
    version("1.1.0", sha256="44aee5f2c4d80c3b29f208359fcb336df80f293a0bb6b1c738da43ca206656fb", url="https://pypi.org/packages/28/6a/8c1f62c37212d9fc441a7e26736df51ce6f0e38455816445471f10da4f0a/Keras_Preprocessing-1.1.0-py2.py3-none-any.whl")
    version("1.0.9", sha256="0170b799a7562f80ad7931d22d56de22cf4bdd502e11c48f31a46380137a70a8", url="https://pypi.org/packages/c0/bf/0315ef6a9fd3fc2346e85b0ff1f5f83ca17073f2c31ac719ab2e4da0d4a3/Keras_Preprocessing-1.0.9-py2.py3-none-any.whl")
    version("1.0.8", sha256="c0cbc80c0cd2d9052afd4977a29ed3a8d12e8d131adfde9db62134c0d48c48c0", url="https://pypi.org/packages/14/8d/443591dd9f42cdde966a14ea2d59e7a781b77a8f09652288af61bec93b81/Keras_Preprocessing-1.0.8-py2.py3-none-any.whl")
    version("1.0.6", sha256="68960bde2b73514252e88601139ffeedaeeea42cd6f2236cb75c92ac75cc1b6f", url="https://pypi.org/packages/e5/ee/93c40d5166e28b6c41f28ee9c0b0fba21ded4142ba809cd579af3231da66/Keras_Preprocessing-1.0.6-py2.py3-none-any.whl")
    version("1.0.5", sha256="90d04c1750bccceef88ac09475c291b4b5f6aa1eaf0603167061b1aa8b043c61", url="https://pypi.org/packages/fc/94/74e0fa783d3fc07e41715973435dd051ca89c550881b3454233c39c73e69/Keras_Preprocessing-1.0.5-py2.py3-none-any.whl")
    version("1.0.4", sha256="f00762c4eeddf2a3cd3e39303406f4d7eaf04fea845a6f77e763f7861a426ee4", url="https://pypi.org/packages/02/f7/38301bccba4b4cc3ca1b607b33d07aad68ab2efcd53d92e1c0a39338e08c/Keras_Preprocessing-1.0.4-py2.py3-none-any.whl")
    version("1.0.3", sha256="ecfdc0d0a396aa0065bd35c8c43f702579901e1569488a024383987ac5d71b0e", url="https://pypi.org/packages/b3/bd/796f986980da4d6adc77ffd8b2b11074e7b17a7b74b03789aefac5709c4b/Keras_Preprocessing-1.0.3-py2.py3-none-any.whl")
    version("1.0.2", sha256="f44ab7bac195ae77ace2ce082413de2d6794e89d09a71a822a6bafd2aa32276b", url="https://pypi.org/packages/71/26/1e778ebd737032749824d5cba7dbd3b0cf9234b87ab5ec79f5f0403ca7e9/Keras_Preprocessing-1.0.2-py2.py3-none-any.whl")
    version("1.0.1", sha256="5283236f0b22a57b30bda766fc819b2ed2483c52f3e1f8b39fcc528f51f772e7", url="https://pypi.org/packages/f8/33/275506afe1d96b221f66f95adba94d1b73f6b6087cfb6132a5655b6fe338/Keras_Preprocessing-1.0.1-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-keras@2.1.6:", when="@:1.0.3")
        depends_on("py-numpy@1.9.1:")
        depends_on("py-scipy@0.14:", when="@:1.0.3")
        depends_on("py-six@1.9:")
    # END DEPENDENCIES

