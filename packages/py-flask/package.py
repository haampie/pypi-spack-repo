##############################################################################
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyFlask(PythonPackage):
    version("3.0.2", sha256="3232e0e9c850d781933cf0207523d1ece087eb8d87b23777ae38456e2fbe7c6e", url="https://pypi.org/packages/93/a6/aa98bfe0eb9b8b15d36cdfd03c8ca86a03968a87f27ce224fb4f766acb23/flask-3.0.2-py3-none-any.whl")
    version("3.0.1", sha256="ca631a507f6dfe6c278ae20112cea3ff54ff2216390bf8880f6b035a5354af13", url="https://pypi.org/packages/bd/0e/63738e88e981ae57c23bad6c499898314a1110a4141f77d7bd929b552fb4/flask-3.0.1-py3-none-any.whl")
    version("3.0.0", sha256="21128f47e4e3b9d597a3e8521a329bf56909b690fcc3fa3e477725aa81367638", url="https://pypi.org/packages/36/42/015c23096649b908c809c69388a805a571a3bea44362fe87e33fc3afa01f/flask-3.0.0-py3-none-any.whl")
    version("2.3.3", sha256="f69fcd559dc907ed196ab9df0e48471709175e696d6e698dd4dbe940f96ce66b", url="https://pypi.org/packages/fd/56/26f0be8adc2b4257df20c1c4260ddd0aa396cf8e75d90ab2f7ff99bc34f9/flask-2.3.3-py3-none-any.whl")
    version("2.3.2", sha256="77fd4e1249d8c9923de34907236b747ced06e5467ecac1a7bb7115ae0e9670b0", url="https://pypi.org/packages/fa/1a/f191d32818e5cd985bdd3f47a6e4f525e2db1ce5e8150045ca0c31813686/Flask-2.3.2-py3-none-any.whl")
    version("2.3.1", sha256="8ba2a854608fdd603b67dccd4514a46450132227fb9df40127a8d0c1de8769ec", url="https://pypi.org/packages/9f/27/fc83394961f97e74c860d05f9bc848af00259b8c84ca021ab31250b9915e/Flask-2.3.1-py3-none-any.whl")
    version("2.3.0", sha256="99a4889167c86fe57c4036825ebc77dc5dc3241bf0d80ea80ca941587d0d6a52", url="https://pypi.org/packages/24/dd/45df0b0b93f449cb217486136071294595b2d6f8840eaf38704773093a37/Flask-2.3.0-py3-none-any.whl")
    version("2.2.5", sha256="58107ed83443e86067e41eff4631b058178191a355886f8e479e347fa1285fdf", url="https://pypi.org/packages/9f/1a/8b6d48162861009d1e017a9740431c78d860809773b66cac220a11aa3310/Flask-2.2.5-py3-none-any.whl")
    version("2.2.4", sha256="13f6329ddbfff11340939cd11919daf150a01358ded4b7e81c03c055dfecb559", url="https://pypi.org/packages/cf/e6/cfd7227e18fc44a56594a7b7df21b7ac63954ea652987e6da7707aba6064/Flask-2.2.4-py3-none-any.whl")
    version("2.2.3", sha256="c0bec9477df1cb867e5a67c9e1ab758de9cb4a3e52dd70681f59fa40a62b3f2d", url="https://pypi.org/packages/95/9c/a3542594ce4973786236a1b7b702b8ca81dbf40ea270f0f96284f0c27348/Flask-2.2.3-py3-none-any.whl")
    version("2.2.2", sha256="b9c46cc36662a7949f34b52d8ec7bb59c0d74ba08ba6cb9ce9adc1d8676d9526", url="https://pypi.org/packages/0f/43/15f4f9ab225b0b25352412e8daa3d0e3d135fcf5e127070c74c3632c8b4c/Flask-2.2.2-py3-none-any.whl")
    version("2.2.1", sha256="3c604c48c3d5b4c63e72134044c0b4fe90ff01ef65280b9fe2d38c8860d99fe5", url="https://pypi.org/packages/3c/96/6c896f80f466b7f5e2cfd6d632fe5b0464dcb412757c595a663e59589a93/Flask-2.2.1-py3-none-any.whl")
    version("2.2.0", sha256="10dc2bae7a9b6ab59111d6dbece2e08fb0015d2e88d296c40323cc0c7aac2c2e", url="https://pypi.org/packages/7b/97/3b7716320e560f937e356773a4ec7846c2617b78f6b7d1334cd1725ba834/Flask-2.2.0-py3-none-any.whl")
    version("2.0.2", sha256="cb90f62f1d8e4dc4621f52106613488b5ba826b2e1e10a33eac92f723093ab6a", url="https://pypi.org/packages/8f/b6/b4fdcb6d01ee20f9cfe81dcf9d3cd6c2f874b996f186f1c0b898c4a59c04/Flask-2.0.2-py3-none-any.whl")
    version("1.1.2", sha256="8a4fdd8936eba2512e9c85df320a37e694c93945b33ef33c89946a340a238557", url="https://pypi.org/packages/f2/28/2a03252dfb9ebf377f40fba6a7841b47083260bf8bd8e737b0c6952df83f/Flask-1.1.2-py2.py3-none-any.whl")
    version("1.1.1", sha256="45eb5a6fd193d6cf7e0cf5d8a5b31f83d5faae0293695626f539a823e93b13f6", url="https://pypi.org/packages/9b/93/628509b8d5dc749656a9641f4caf13540e2cdec85276964ff8f43bbb1d3b/Flask-1.1.1-py2.py3-none-any.whl")
    version("0.12.5", sha256="2c710d1d42317c802c43000daa16de9de6026146b344ab3376cbc6d18846b863", url="https://pypi.org/packages/a4/36/756c34af4523bb0dfa77d3c83455bc4d5d01d6f03b20d8414f3e4deb8669/Flask-0.12.5-py2.py3-none-any.whl")
    version("0.12.4", sha256="6c02dbaa5a9ef790d8219bdced392e2d549c10cd5a5ba4b6aa65126b2271af29", url="https://pypi.org/packages/2e/48/f1936dadac2326b3d73f2fe0a964a87d16be16eb9d7fc56f09c1bea3d17c/Flask-0.12.4-py2.py3-none-any.whl")
    version("0.12.3", sha256="74bb782687731332b86aa8ab0817be14c9e63e5fa837934de8be4f9236d6d0d2", url="https://pypi.org/packages/24/3e/1b6aa496fa9bb119f6b22263ca5ca9e826aaa132431fd78f413c8bcc18e3/Flask-0.12.3-py2.py3-none-any.whl")
    version("0.12.2", sha256="49f44461237b69ecd901cc7ce66feea0319b9158743dd27a2899962ab214dac1", url="https://pypi.org/packages/eb/12/1c7bd06fcbd08ba544f25bf2c6612e305a70ea51ca0eda8007344ec3f123/Flask-0.12.2.tar.gz")
    version("0.12.1", sha256="9dce4b6bfbb5b062181d3f7da8f727ff70c1156cbb4024351eafd426deb5fb88", url="https://pypi.org/packages/24/6e/11b9c57e46f276a8a8dfda85a2fa7ada62b0463b68693616c7ab5df356fa/Flask-0.12.1.tar.gz")
    version("0.11.1", sha256="b4713f2bfb9ebc2966b8a49903ae0d3984781d5c878591cf2f7b484d28756b0e", url="https://pypi.org/packages/55/8a/78e165d30f0c8bb5d57c429a30ee5749825ed461ad6c959688872643ffb3/Flask-0.11.1.tar.gz")

    with default_args(type="run"):
        depends_on("py-blinker@1.6.2:", when="@2.3:")
        depends_on("py-click@8.1.3:", when="@2.3:")
        depends_on("py-click@8.0.0:", when="@2.1:2.2")
        depends_on("py-click@7.1.2:", when="@2.0.0-rc2:2.0")
        depends_on("py-click@5.1:", when="@1:1.1.2")
        depends_on("py-click@2:", when="@0.12.3:0")
        depends_on("py-importlib-metadata@3.6:", when="@2.1.1: ^python@:3.9")
        depends_on("py-itsdangerous@2.1.2:", when="@2.3:")
        depends_on("py-itsdangerous@2.0.0:", when="@2.0.0:2.2")
        depends_on("py-itsdangerous@0.24:", when="@1:1.1.2")
        depends_on("py-itsdangerous@0.21:", when="@0.12.3:0")
        depends_on("py-jinja2@3.1.2:", when="@2.3:")
        depends_on("py-jinja2@3.0.0:", when="@2.0.0:2.2")
        depends_on("py-jinja2@2.10.1:", when="@1.1:1.1.2")
        depends_on("py-jinja2@2.4:", when="@0.12.3:0")
        depends_on("py-werkzeug@3:", when="@3:")
        depends_on("py-werkzeug@2.3.7:", when="@2.3.3:2")
        depends_on("py-werkzeug@2.3.3:", when="@2.3.2")
        depends_on("py-werkzeug@2.3:", when="@2.3:2.3.1")
        depends_on("py-werkzeug@2.2.2:", when="@2.2.2:2.2")
        depends_on("py-werkzeug@2.2.0:", when="@2.2:2.2.1")
        depends_on("py-werkzeug@2.0.0:", when="@2.0.0:2.1")
        depends_on("py-werkzeug@0.15:", when="@1.1:1.1.2")
        depends_on("py-werkzeug@0.7:0", when="@0.12.5:0")
        depends_on("py-werkzeug@0.7:", when="@0.12.3:0.12.4")

