# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyJinja2(PythonPackage):
    # BEGIN VERSIONS
    version("3.1.2", sha256="6088930bfe239f0e6710546ab9c19c9ef35e29792895fed6e6e31a023a182a61", url="https://pypi.org/packages/bc/c3/f068337a370801f372f2f8f6bad74a5c140f6fda3d9de154052708dd3c65/Jinja2-3.1.2-py3-none-any.whl")
    version("3.0.3", sha256="077ce6014f7b40d03b47d1f1ca4b0fc8328a692bd284016f806ed0eaca390ad8", url="https://pypi.org/packages/20/9a/e5d9ec41927401e41aea8af6d16e78b5e612bca4699d417f646a9610a076/Jinja2-3.0.3-py3-none-any.whl")
    version("3.0.1", sha256="1f06f2da51e7b56b8f238affdd6b4e2c61e39598a378cc49345bc1bd42a978a4", url="https://pypi.org/packages/80/21/ae597efc7ed8caaa43fb35062288baaf99a7d43ff0cf66452ddf47604ee6/Jinja2-3.0.1-py3-none-any.whl")
    version("2.11.3", sha256="03e47ad063331dd6a3f04a43eddca8a966a26ba0c5b7207a9a9e4e08f1b29419", url="https://pypi.org/packages/7e/c2/1eece8c95ddbc9b1aeb64f5783a9e07a286de42191b7204d67b7496ddf35/Jinja2-2.11.3-py2.py3-none-any.whl")
    version("2.10.3", sha256="74320bb91f31270f9551d46522e33af46a80c3d619f4a4bf42b3164d30b5911f", url="https://pypi.org/packages/65/e0/eb35e762802015cab1ccee04e8a277b03f1d8e53da3ec3106882ec42558b/Jinja2-2.10.3-py2.py3-none-any.whl")
    version("2.10.1", sha256="14dd6caf1527abb21f08f86c784eac40853ba93edb79552aa1e4b8aef1b61c7b", url="https://pypi.org/packages/1d/e7/fd8b501e7a6dfe492a433deb7b9d833d39ca74916fa8bc63dd1a4947a671/Jinja2-2.10.1-py2.py3-none-any.whl")
    version("2.10", sha256="74c935a1b8bb9a3947c50a54766a969d4846290e1e788ea44c1392163723c3bd", url="https://pypi.org/packages/7f/ff/ae64bacdfc95f27a016a7bed8e8686763ba4d277a78ca76f32659220a731/Jinja2-2.10-py2.py3-none-any.whl")
    version("2.9.6", sha256="2231bace0dfd8d2bf1e5d7e41239c06c9e0ded46e70cc1094a0aa64b0afeb054", url="https://pypi.org/packages/5e/73/10c45b82a88ed6b7751bd40da31eeefd7b362e07b56a99aa6e56655a0794/Jinja2-2.9.6-py2.py3-none-any.whl")
    version("2.8", sha256="1cc03ef32b64be19e0a5b54578dd790906a34943fe9102cfdae0d4495bd536b4", url="https://pypi.org/packages/96/a1/c56bc4d99dc2663514a8481511e80eba8994133ae75eebdadfc91a5597d9/Jinja2-2.8-py2.py3-none-any.whl")
    version("2.7.3", sha256="2e24ac5d004db5714976a04ac0e80c6df6e47e98c354cb2c0d82f8879d4f8fdb", url="https://pypi.org/packages/b0/73/eab0bca302d6d6a0b5c402f47ad1760dc9cb2dd14bbc1873ad48db258e4d/Jinja2-2.7.3.tar.gz")
    version("2.7.2", sha256="310a35fbccac3af13ebf927297f871ac656b9da1d248b1fe6765affa71b53235", url="https://pypi.org/packages/23/94/ca42176bf7a252ce1f5d165953013573dffdbe4b5dac07f57146146ea432/Jinja2-2.7.2.tar.gz")
    version("2.7.1", sha256="5cc0a087a81dca1c08368482fb7a92fe2bdd8cfbb22bc0fccfe6c85affb04c8b", url="https://pypi.org/packages/47/83/679b5592feb54e948d6599edf5dac61d2991778c3ecbef6b8041663f4740/Jinja2-2.7.1.tar.gz")
    version("2.7", sha256="474f1518d189ae7e318b139fecc1d30b943f124448cfa0f09582ca23e069fa4d", url="https://pypi.org/packages/33/db/9931c645626f9bf7867cc3c4225e7a8abf7aff37ecddb7e7d5df90a3b6c4/Jinja2-2.7.tar.gz")
    # END VERSIONS

    # BEGIN VARIANTS
    variant("i18n", default=False)
    # END VARIANTS

    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-babel@2.7:", when="@3.0.0-rc1:+i18n")
        depends_on("py-babel", when="@2.10:2+i18n")
        depends_on("py-markupsafe@2.0.0:", when="@3.0.1:")
        depends_on("py-markupsafe@0.23:", when="@2.10:2")
    # END DEPENDENCIES

