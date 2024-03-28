# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyDeepdiff(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("6.7.1", sha256="58396bb7a863cbb4ed5193f548c56f18218060362311aa1dc36397b2f25108bd", url="https://pypi.org/packages/5a/8f/a9d39ec15f40e8169cb134317824ee4618b864b2e4b91a9b310d3ef94729/deepdiff-6.7.1-py3-none-any.whl")
    version("6.7.0", sha256="d64dd64be5b2e3917c7cc557d69e68d008d798a5cd4981d1508707037504d50a", url="https://pypi.org/packages/11/a5/fb28e5b442af0db9e293932ce35f20805493116bec2eee38acfea9c48716/deepdiff-6.7.0-py3-none-any.whl")
    version("6.6.1", sha256="891b3cb12837e5d376ac0b58f4c8a2764e3a8bbceabb7108ff82235f1f2c4460", url="https://pypi.org/packages/d7/4f/e39f73757101ae9c191dbc911ffb2e97e4898e4feda6f78546238d44a59d/deepdiff-6.6.1-py3-none-any.whl")
    version("6.6.0", sha256="e96424a57befa3f85238d10d9fb73d7a8cfd2228f1c2ab3cedd58b97d2acd80e", url="https://pypi.org/packages/cd/ac/bc7c9b491b9f8ab95b4a0db362af5f149fa7cf575d422dbc62e0fb076d95/deepdiff-6.6.0-py3-none-any.whl")
    version("6.5.0", sha256="acdc1651a3e802415e0337b7e1192df5cd7c17b72fbab480466fdd799b9a72e7", url="https://pypi.org/packages/0a/aa/ad75c66354a1b3619e73879a48219488e5ea91f26569d2f1fd4ba616cacd/deepdiff-6.5.0-py3-none-any.whl")
    version("6.4.1", sha256="065cdbbe62f66447cf507b32351579ffcc4a80bb28f567ac27e92a21ddca99f9", url="https://pypi.org/packages/c6/a9/c846cb3a6965002f42fb073fff6d30a2efcfa825cc3f4a1ac9ca7a0335d2/deepdiff-6.4.1-py3-none-any.whl")
    version("6.4.0", sha256="a3118ae1b2072aa87b7ec080d24a71b2d855609c209794e018c01299e4c96277", url="https://pypi.org/packages/98/2f/d62b174a0ea1c7901de9971c60cb376b1d8594f509a1e0c533cef44515a6/deepdiff-6.4.0-py3-none-any.whl")
    version("6.3.1", sha256="eae2825b2e1ea83df5fc32683d9aec5a56e38b756eb2b280e00863ce4def9d33", url="https://pypi.org/packages/fe/b3/81bb598d24f1a48eaceb32243a91016385c0599196a59eaff6cd29299334/deepdiff-6.3.1-py3-none-any.whl")
    version("6.3.0", sha256="15838bd1cbd046ce15ed0c41e837cd04aff6b3e169c5e06fca69d7aa11615ceb", url="https://pypi.org/packages/33/4f/8feec2f9ef4515fc63566ec95a4775afd3ab1f08b563240469aa6afabd41/deepdiff-6.3.0-py3-none-any.whl")
    version("6.2.3", sha256="d83b06e043447d6770860a635abecb46e849b0494c43ced2ecafda7628c7ce72", url="https://pypi.org/packages/a7/dd/85c0fa878b5cd8e5c128500729874c8622337490130d86e1d40e0ad04187/deepdiff-6.2.3-py3-none-any.whl")
    version("5.6.0", sha256="ef3410ca31e059a9d10edfdff552245829835b3ecd03212dc5b533d45a6c3f57", url="https://pypi.org/packages/18/d1/25134e24783076814071e51b5417407947398dd4c99e607ec3c9feca5c90/deepdiff-5.6.0-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-ordered-set@4.0.2:", when="@6:")
        depends_on("py-ordered-set@4.0.2:4.0", when="@5.2:5.7")
        depends_on("py-orjson", when="@6.2.3:6.2")
    # END DEPENDENCIES

