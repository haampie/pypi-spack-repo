# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyJinja2(PythonPackage):
    # BEGIN VERSIONS
    version("3.1.3", sha256="7d6d50dd97d52cbc355597bd845fabfbac3f551e1f99619e39a35ce8c370b5fa", url="https://pypi.org/packages/30/6d/6de6be2d02603ab56e72997708809e8a5b0fbfee080735109b40a3564843/Jinja2-3.1.3-py3-none-any.whl")
    version("3.1.2", sha256="6088930bfe239f0e6710546ab9c19c9ef35e29792895fed6e6e31a023a182a61", url="https://pypi.org/packages/bc/c3/f068337a370801f372f2f8f6bad74a5c140f6fda3d9de154052708dd3c65/Jinja2-3.1.2-py3-none-any.whl")
    version("3.1.1", sha256="539835f51a74a69f41b848a9645dbdc35b4f20a3b601e2d9a7e22947b15ff119", url="https://pypi.org/packages/76/02/af4045156cde8feeefa30cb1c051e10321d4960c418bd52346a497feb302/Jinja2-3.1.1-py3-none-any.whl")
    version("3.1.0", sha256="da424924c069a4013730d8dd010cbecac7e7bb752be388db3741688bffb48dc6", url="https://pypi.org/packages/7b/82/743248f82f147e54a404163c7e12969f4c2436bdfe7c39bf6b5c7a273f3f/Jinja2-3.1.0-py3-none-any.whl")
    version("3.0.3", sha256="077ce6014f7b40d03b47d1f1ca4b0fc8328a692bd284016f806ed0eaca390ad8", url="https://pypi.org/packages/20/9a/e5d9ec41927401e41aea8af6d16e78b5e612bca4699d417f646a9610a076/Jinja2-3.0.3-py3-none-any.whl")
    version("3.0.2", sha256="8569982d3f0889eed11dd620c706d39b60c36d6d25843961f33f77fb6bc6b20c", url="https://pypi.org/packages/94/42/d8bca8e99789bcc35dfa9b03acaa8b518720d6e060163745bc2bf2ead842/Jinja2-3.0.2-py3-none-any.whl")
    version("3.0.1", sha256="1f06f2da51e7b56b8f238affdd6b4e2c61e39598a378cc49345bc1bd42a978a4", url="https://pypi.org/packages/80/21/ae597efc7ed8caaa43fb35062288baaf99a7d43ff0cf66452ddf47604ee6/Jinja2-3.0.1-py3-none-any.whl")
    version("3.0.0", sha256="2f2de5285cf37f33d33ecd4a9080b75c87cd0c1994d5a9c6df17131ea1f049c6", url="https://pypi.org/packages/48/9b/dc3bbfc44d851632df958acf9d47e4de662c6bbd238e46798d555d427b27/Jinja2-3.0.0-py3-none-any.whl")
    version("3.0.0-rc2", sha256="8e68a2e702a59a57c86305752df25532472a0dad2b4b2756a1d289c618a9e1f5", url="https://pypi.org/packages/0a/ed/f0ddd65b6c118322d38db13dc7a806ef121c43df89b60a8ec27ff1e2fbe4/Jinja2-3.0.0rc2-py3-none-any.whl")
    version("3.0.0-rc1", sha256="e45e6190f710fb7628af1315cb78354ea08955ab29db1d5fc53acc15cfbd52ee", url="https://pypi.org/packages/89/9b/5350267251fa4196af24c7c2ea87f002d098c3ef4a8f099451cfa2bca802/Jinja2-3.0.0rc1-py3-none-any.whl")
    version("3.0.0-alpha1", sha256="c10142f819c2d22bdcd17548c46fa9b77cf4fda45097854c689666bf425e7484", url="https://pypi.org/packages/3b/c4/d9e8cc19bd72e23aff339ce02ae0a2c447652ed6f8e82ef4d8294747ebc2/Jinja2-3.0.0a1-py3-none-any.whl")
    version("2.11.3", sha256="03e47ad063331dd6a3f04a43eddca8a966a26ba0c5b7207a9a9e4e08f1b29419", url="https://pypi.org/packages/7e/c2/1eece8c95ddbc9b1aeb64f5783a9e07a286de42191b7204d67b7496ddf35/Jinja2-2.11.3-py2.py3-none-any.whl")
    version("2.11.2", sha256="f0a4641d3cf955324a89c04f3d94663aa4d638abe8f733ecd3582848e1c37035", url="https://pypi.org/packages/30/9e/f663a2aa66a09d838042ae1a2c5659828bb9b41ea3a6efa20a20fd92b121/Jinja2-2.11.2-py2.py3-none-any.whl")
    version("2.11.1", sha256="b0eaf100007721b5c16c1fc1eecb87409464edc10469ddc9a22a27a99123be49", url="https://pypi.org/packages/27/24/4f35961e5c669e96f6559760042a55b9bcfcdb82b9bdb3c8753dbe042e35/Jinja2-2.11.1-py2.py3-none-any.whl")
    version("2.11.0", sha256="6e7a3c2934694d59ad334c93dd1b6c96699cf24c53fdb8ec848ac6b23e685734", url="https://pypi.org/packages/7b/af/b9ed1959cb4bb7332e2b0797476c878fa38d200bfcfe38c6d53517c29bdf/Jinja2-2.11.0-py2.py3-none-any.whl")
    version("2.10.3", sha256="74320bb91f31270f9551d46522e33af46a80c3d619f4a4bf42b3164d30b5911f", url="https://pypi.org/packages/65/e0/eb35e762802015cab1ccee04e8a277b03f1d8e53da3ec3106882ec42558b/Jinja2-2.10.3-py2.py3-none-any.whl")
    version("2.10.2", sha256="d599309630bb8b054b78089c567e29f805b4ac3b1fafc4ef03a149f2bf97914b", url="https://pypi.org/packages/38/31/cc05057b7a9aa08762fe692f09969d2006f7ef740e36b36f4479b63ffa4c/Jinja2-2.10.2-py2.py3-none-any.whl")
    version("2.10.1", sha256="14dd6caf1527abb21f08f86c784eac40853ba93edb79552aa1e4b8aef1b61c7b", url="https://pypi.org/packages/1d/e7/fd8b501e7a6dfe492a433deb7b9d833d39ca74916fa8bc63dd1a4947a671/Jinja2-2.10.1-py2.py3-none-any.whl")
    version("2.10", sha256="74c935a1b8bb9a3947c50a54766a969d4846290e1e788ea44c1392163723c3bd", url="https://pypi.org/packages/7f/ff/ae64bacdfc95f27a016a7bed8e8686763ba4d277a78ca76f32659220a731/Jinja2-2.10-py2.py3-none-any.whl")
    version("2.9.6", sha256="2231bace0dfd8d2bf1e5d7e41239c06c9e0ded46e70cc1094a0aa64b0afeb054", url="https://pypi.org/packages/5e/73/10c45b82a88ed6b7751bd40da31eeefd7b362e07b56a99aa6e56655a0794/Jinja2-2.9.6-py2.py3-none-any.whl")
    version("2.9.5", sha256="a7b7438120dbe76a8e735ef7eba6048eaf4e0b7dbc530e100812f8ec462a4d50", url="https://pypi.org/packages/3c/d1/49d69bc23d0e0c7612248dd8f5391bd043648865132309616c280ca1c837/Jinja2-2.9.5-py2.py3-none-any.whl")
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
        depends_on("py-babel@2.1:", when="@3:3.0.0-alpha1+i18n")
        depends_on("py-babel", when="@2.10:2+i18n")
        depends_on("py-markupsafe@2.0.0:", when="@3.0.1:")
        depends_on("py-markupsafe@2.0.0-rc2:", when="@3.0.0-rc1:3.0.0")
        depends_on("py-markupsafe@1.1:", when="@3:3.0.0-alpha1")
        depends_on("py-markupsafe@0.23:", when="@2.10:2")
    # END DEPENDENCIES

