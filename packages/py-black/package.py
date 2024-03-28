# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyBlack(PythonPackage):
    # BEGIN VERSIONS
    version("24.3.0", sha256="a0c9c4a0771afc6919578cec71ce82a3e31e054904e7197deacbc9382671c41f", url="https://pypi.org/packages/8f/5f/bac24a952668c7482cfdb4ebf91ba57a796c9da8829363a772040c1a3312/black-24.3.0.tar.gz")
    version("24.2.0", sha256="bce4f25c27c3435e4dace4815bcb2008b87e167e3bf4ee47ccdc5ce906eb4894", url="https://pypi.org/packages/29/69/f3ab49cdb938b3eecb048fa64f86bdadb1fac26e92c435d287181d543b0a/black-24.2.0.tar.gz")
    version("24.1.1", sha256="48b5760dcbfe5cf97fd4fba23946681f3a81514c6ab8a45b50da67ac8fbc6c7b", url="https://pypi.org/packages/77/ec/a429d15d2e7f996203bff98e2b2e84ad4cb3de318de147b0038dc93fbc71/black-24.1.1.tar.gz")
    version("24.1.0", sha256="30fbf768cd4f4576598b1db0202413fafea9a227ef808d1a12230c643cefe9fc", url="https://pypi.org/packages/ea/19/33d4f2f0babcbc07d3e2c058a64c76606cf19884a600536c837aaf4e4f2d/black-24.1.0.tar.gz")
    version("23.12.1", sha256="4ce3ef14ebe8d9509188014d96af1c456a910d5b5cbf434a09fef7e024b3d0d5", url="https://pypi.org/packages/fd/f4/a57cde4b60da0e249073009f4a9087e9e0a955deae78d3c2a493208d0c5c/black-23.12.1.tar.gz")
    version("23.12.0", sha256="330a327b422aca0634ecd115985c1c7fd7bdb5b5a2ef8aa9888a82e2ebe9437a", url="https://pypi.org/packages/5a/73/618bcfd4a4868d52c02ff7136ec60e9d63bc83911d3d8b4998e42acf9557/black-23.12.0.tar.gz")
    version("23.11.0", sha256="4c68855825ff432d197229846f971bc4d6666ce90492e5b02013bcaca4d9ab05", url="https://pypi.org/packages/ef/21/c2d38c7c98a089fd0f7e1a8be16c07f141ed57339b3082737de90db0ca59/black-23.11.0.tar.gz")
    version("23.10.1", sha256="1f8ce316753428ff68749c65a5f7844631aa18c8679dfd3ca9dc1a289979c258", url="https://pypi.org/packages/36/bf/a462f36723824c60dc3db10528c95656755964279a6a5c287b4f9fd0fa84/black-23.10.1.tar.gz")
    version("23.10.0", sha256="31b9f87b277a68d0e99d2905edae08807c007973eaa609da5f0c62def6b7c0bd", url="https://pypi.org/packages/2d/e0/8433441b0236b9d795ffbf5750f98144e0378b6e20401ba4d2db30b99a5c/black-23.10.0.tar.gz")
    version("23.9.1", sha256="24b6b3ff5c6d9ea08a8888f6977eae858e1f340d7260cf56d70a49823236b62d", url="https://pypi.org/packages/12/c3/257adbdbf2cc60bf844b5c0e3791a9d49e4fb4f7bcd8a2e875824ca0b7bc/black-23.9.1.tar.gz")
    version("23.9.0", sha256="9366c1f898981f09eb8da076716c02fd021f5a0e63581c66501d68a2e4eab844", url="https://pypi.org/packages/2a/c2/e2cd7f95aa0f1a4d77ed0153efb213b99bfa5f086226a8f1fcc67483f62a/black-23.9.0-py3-none-any.whl")
    version("23.7.0", sha256="022a582720b0d9480ed82576c920a8c1dde97cc38ff11d8d8859b3bd6ca9eedb", url="https://pypi.org/packages/e9/20/29d7a6614606785923edf9e8ec3ff630231992cc2fabc02eacb0d475372e/black-23.7.0.tar.gz")
    version("23.3.0", sha256="1c7b8d606e728a41ea1ccbd7264677e494e87cf630e399262ced92d4a8dac940", url="https://pypi.org/packages/d6/36/66370f5017b100225ec4950a60caeef60201a10080da57ddb24124453fba/black-23.3.0.tar.gz")
    version("23.1.0", sha256="b0bd97bea8903f5a2ba7219257a44e3f1f9d00073d6cc1add68f0beec69692ac", url="https://pypi.org/packages/15/11/533355217b1cc4a6df3263048060c1527f733d4720e158de2085293112bb/black-23.1.0.tar.gz")
    version("22.12.0", sha256="229351e5a18ca30f447bf724d007f890f97e13af070bb6ad4c0a441cd7596a2f", url="https://pypi.org/packages/a6/59/e873cc6807fb62c11131e5258ca15577a3b7452abad08dc49286cf8245e8/black-22.12.0.tar.gz")
    version("22.10.0", sha256="f513588da599943e0cde4e32cc9879e825d58720d6557062d1098c5ad80080e1", url="https://pypi.org/packages/a3/89/629fca2eea0899c06befaa58dc0f49d56807d454202bb2e54bd0d98c77f3/black-22.10.0.tar.gz")
    version("22.8.0", sha256="792f7eb540ba9a17e8656538701d3eb1afcb134e3b45b71f20b25c77a8db7e6e", url="https://pypi.org/packages/3a/1b/38a013f75022fae724ed766fdac5f6777544c45eecbe00a6d8fd91a2a26b/black-22.8.0.tar.gz")
    version("22.6.0", sha256="6c6d39e28aed379aec40da1c65434c77d75e65bb59a1e1c283de545fb4e7c6c9", url="https://pypi.org/packages/61/11/551b0d067a7e6836fc0997ab36ee46ec65259fea8f30104f4870092f3301/black-22.6.0.tar.gz")
    version("22.3.0", sha256="35020b8886c022ced9282b51b5a875b6d1ab0c387b31a065b84db7c33085ca79", url="https://pypi.org/packages/ee/1f/b29c7371958ab41a800f8718f5d285bf4333b8d0b5a5a8650234463ee644/black-22.3.0.tar.gz")
    version("22.1.0", sha256="a7c0192d35635f6fc1174be575cb7915e92e5dd629ee79fdaf0dcfa41a80afb5", url="https://pypi.org/packages/42/58/8a3443a5034685152270f9012a9d196c9f165791ed3f2777307708b15f6c/black-22.1.0.tar.gz")
    version("21.12-beta0", sha256="a615e69ae185e08fdd73e4715e260e2479c861b5740057fde6e8b4e3b7dd589f", url="https://pypi.org/packages/9b/27/b2f98b627738b02dcac06ae9e2ab13f14ab906fe6dd6366050c76883d4b5/black-21.12b0-py3-none-any.whl")
    version("21.11-beta1", sha256="802c6c30b637b28645b7fde282ed2569c0cd777dbe493a41b6a03c1d903f99ac", url="https://pypi.org/packages/c7/24/0de05480822e5f0f2cc539fce9029bc2507b44b7f85ec1a9e23d89dea6c3/black-21.11b1-py3-none-any.whl")
    version("21.11-beta0", sha256="0b1f66cbfadcd332ceeaeecf6373d9991d451868d2e2219ad0ac1213fb701117", url="https://pypi.org/packages/3d/ad/1cf514e7f9ee4c3d8df7c839d7977f7605ad76557f3fca741ec67f76dba6/black-21.11b0-py3-none-any.whl")
    version("21.10-beta0", sha256="6eb7448da9143ee65b856a5f3676b7dda98ad9abe0f87fce8c59291f15e82a5b", url="https://pypi.org/packages/12/df/0e55791b9c6ca07b4a3404eef6cee1ca42503bf16e9fc9df0247b4803cf1/black-21.10b0-py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    variant("colorama", default=False)
    variant("d", default=False)
    variant("jupyter", default=False)
    variant("uvloop", default=False)
    # END VARIANTS

    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-aiohttp@3.7.4:", when="@23.12:23.12.0,24:24.1.0 platform=linux")
        depends_on("py-aiohttp@3.7.4:", when="@23.12:23.12.0,24:24.1.0 platform=freebsd")
        depends_on("py-aiohttp@3.7.4:", when="@23.12:23.12.0,24:24.1.0 platform=darwin")
        depends_on("py-aiohttp@3.7.4:", when="@23.12:23.12.0,24:24.1.0 platform=cray")
        depends_on("py-aiohttp@3.7.4:", when="@21.10-beta0:21,22.10:+d")
        depends_on("py-click@8.0.0:", when="@22.10:")
        depends_on("py-click@7.1.2:", when="@20.8-beta1:21")
        depends_on("py-colorama@0.4.3:", when="@20:21,22.10:+colorama")
        depends_on("py-ipython@7.8:", when="@21.8-beta0:21,22.10:+jupyter")
        depends_on("py-mypy-extensions@0.4.3:", when="@20:21,22.10:")
        depends_on("py-packaging@22:", when="@23.1.0:")
        depends_on("py-pathspec@0.9:", when="@21.8-beta0:21,22.10:")
        depends_on("py-platformdirs@2.0.0:", when="@21.8-beta0:21,22.10:")
        depends_on("py-regex@2021.4:", when="@21.11-beta1:21.11")
        depends_on("py-regex@2020.1.8:", when="@20:21.11-beta0")
        depends_on("py-tokenize-rt@3.2:", when="@21.8-beta0:21,22.10:+jupyter")
        depends_on("py-tomli@1.1:", when="@22.10: ^python@:3.10")
        depends_on("py-tomli@0.2.6:1", when="@21.7-beta0:21")
        depends_on("py-typing-extensions@4.0.1:", when="@23.9: ^python@:3.10")
        depends_on("py-typing-extensions@3.10:", when="@22.10:23.7 ^python@:3.9")
        depends_on("py-typing-extensions@:3.10.0.0,3.10.0.2:", when="@21.8-beta0:21 ^python@3.10:")
        depends_on("py-typing-extensions@3.10:", when="@21.8-beta0:21")
        depends_on("py-uvloop@0.15.2:", when="@21.5-beta2:21,22.10:+uvloop")
    # END DEPENDENCIES

