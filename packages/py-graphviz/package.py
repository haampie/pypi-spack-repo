# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyGraphviz(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("0.20.2", sha256="63d1ae75f1ca60f980e1cd3a61a678eef8de645ef8427736b2bb9bdd035ca44b", url="https://pypi.org/packages/18/79/12d3f468cc67a04d0db640bdd54913e60cd9828e3eada107d330d760d61a/graphviz-0.20.2-py3-none-any.whl")
    version("0.20.1", sha256="587c58a223b51611c0cf461132da386edd896a029524ca61a1462b880bf97977", url="https://pypi.org/packages/de/5e/fcbb22c68208d39edff467809d06c9d81d7d27426460ebc598e55130c1aa/graphviz-0.20.1-py3-none-any.whl")
    version("0.20", sha256="62c5f48bcc534a45b4588c548ff75e419c1f1f3a33d31a91796ae80a7f581e4a", url="https://pypi.org/packages/4d/ea/81a8018c234ad6219c27155fe3dce349f2ba83e6ebed582c9f8aca46091f/graphviz-0.20-py3-none-any.whl")
    version("0.19.2", sha256="c0a6ac9fadaa308c4ab0d526749c6e127425ec5a76644bbb03e2e04b19a9da9f", url="https://pypi.org/packages/f8/5f/b8cf4337122a0ec9478e85ae7190ccaa3f99960136674b68af41e4d80835/graphviz-0.19.2-py3-none-any.whl")
    version("0.19.1", sha256="f34088c08be2ec16279dfa9c3b4ff3d1453c5c67597a33e2819b000e18d4c546", url="https://pypi.org/packages/9d/fb/886e8ec7862989afc0c35d15813b6c665fe134cc6027cdde2fa300abe9a2/graphviz-0.19.1-py3-none-any.whl")
    version("0.19", sha256="60704af002770700b099e5d684b7f2bd59c06bbaec8f575def7fba7a31a1a27a", url="https://pypi.org/packages/5b/4c/3fd6c42cf1ccbc81e2c9fd56494dad4c144db1537bfcbd1d45c6b97e1aa3/graphviz-0.19-py3-none-any.whl")
    version("0.18.2", sha256="b0fda999966e75e974197c2a80946e9345f730837921a1180b4fd8397bea2799", url="https://pypi.org/packages/e1/a3/e4685863f894958ecafb42ebcaa8d3692a83c409275980a3460c3f371b4e/graphviz-0.18.2-py3-none-any.whl")
    version("0.18.1", sha256="6adf01cf64fb9b1c4374b733d91d4bd8bf2e86d5988d9e140c91fa304203cfb2", url="https://pypi.org/packages/10/4c/2eb2ce2be83a0bbbcc21d41e12ba684f53a4c98c66001700e61747ca08ae/graphviz-0.18.1-py3-none-any.whl")
    version("0.18", sha256="f8bab3bf3eda40ab259bb96f786811b5dec6fd6957fa70a5b1977534e1ee2a40", url="https://pypi.org/packages/03/09/4c70ca7cc67820e7f3e9daeca015fd377e92981b8cc944c68ac6c5d91784/graphviz-0.18-py3-none-any.whl")
    version("0.17", sha256="5dadec94046d82adaae6019311a30e0487536d9d5a60d85451f0ba32f9fc6559", url="https://pypi.org/packages/97/14/b5eeeb6d24dbca0ada857ce4a453985df34d9512464bb20cc1a8aca44c54/graphviz-0.17-py3-none-any.whl")
    version("0.13.2", sha256="241fb099e32b8e8c2acca747211c8237e40c0b89f24b1622860075d59f4c4b25", url="https://pypi.org/packages/f5/74/dbed754c0abd63768d3a7a7b472da35b08ac442cf87d73d5850a6f32391e/graphviz-0.13.2-py2.py3-none-any.whl")
    version("0.13", sha256="df54c2e0d2c8df6aee3397eb44de186d94e2a0610f4052649bfbb26d03d56850", url="https://pypi.org/packages/94/cd/7b37f2b658995033879719e1ea4c9f171bf7a14c16b79220bd19f9eda3fe/graphviz-0.13-py2.py3-none-any.whl")
    version("0.12", sha256="8adc6460f9eddca440b826dd89790090d76fb8e693e2206fd4c2a4ed80841999", url="https://pypi.org/packages/17/51/d6de512dbbbab95f0adb53fb2a4396b79722f7c3fbe8ecc2d8c6ab7de00a/graphviz-0.12-py2.py3-none-any.whl")
    version("0.11.1", sha256="6d0f69c107cfdc9bd1df3763fad99569bbcba29d0c52ffcbc6f266621d8bf709", url="https://pypi.org/packages/5c/b1/016e657586843f40b4daa66127ce1ee9e3285ff15baf5d80946644a98aeb/graphviz-0.11.1-py2.py3-none-any.whl")
    version("0.10.1", sha256="0e1744a45b0d707bc44f99c7b8e5f25dc22cf96b6aaf2432ac308ed9822a9cb6", url="https://pypi.org/packages/1f/e2/ef2581b5b86625657afd32030f90cf2717456c1d2b711ba074bf007c0f1a/graphviz-0.10.1-py2.py3-none-any.whl")
    version("0.8.4", sha256="7caa53f0b0be42c5f2eaa3f3d71dcc863b15bacceb5d531c2ad7519e1980ff82", url="https://pypi.org/packages/53/39/4ab213673844e0c004bed8a0781a0721a3f6bb23eb8854ee75c236428892/graphviz-0.8.4-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    variant("dev", default=False)
    variant("docs", default=False)
    # END VARIANTS

    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-flake8", when="@0.8.2:+dev")
        depends_on("py-pep8-naming", when="@0.8.2:+dev")
        depends_on("py-sphinx@5.0.0:6", when="@0.20.2:+docs")
        depends_on("py-sphinx@5.0.0:", when="@0.20.1+docs")
        depends_on("py-sphinx@4.0.0:", when="@0.20:0.20.0+docs")
        depends_on("py-sphinx@1.8.0:", when="@0.14.1:0.19+docs")
        depends_on("py-sphinx@1.7.0:", when="@0.10:0.14.0+docs")
        depends_on("py-sphinx@1.3:", when="@0.8.3:0.9+docs")
        depends_on("py-sphinx-autodoc-typehints", when="@0.17:+docs")
        depends_on("py-sphinx-rtd-theme", when="@0.8.3:+docs")
        depends_on("py-tox@3.0.0:", when="@0.8.3:+dev")
        depends_on("py-twine", when="@0.8.2:+dev")
        depends_on("py-wheel", when="@0.8.2:+dev")
    # END DEPENDENCIES

