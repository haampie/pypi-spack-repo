# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkSocial(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("10.2", sha256="76ed463e3a77c58e5b527c37eb8b2dd60658dd736ba243cfa24b4704580b58c4", url="https://pypi.org/packages/b0/aa/ea83963edcb48e184614272a87612a05586ab8a5999234796c87eb42ed19/pyobjc_framework_Social-10.2-py2.py3-none-any.whl")
    version("10.1", sha256="81363d9d06c9c8ede16d96ec1d3cdba6deef195ef54cc64618e58c7fc1f574df", url="https://pypi.org/packages/4a/75/2dba00901d5decd1689e21ecc7a1c6f8235c04ee513c9f80b9ac9a4eab6f/pyobjc_framework_Social-10.1-py2.py3-none-any.whl")
    version("10.0", sha256="05d2cc1b62e2c1ffbe9ed8868e70fb846eb0f4d7157b87c8db77cd13bf0f2a92", url="https://pypi.org/packages/9e/60/df5abefb3b2690b39d435e472703c27f8ece059ac7c6a9e6a997dbbe4bff/pyobjc_framework_Social-10.0-py2.py3-none-any.whl")
    version("9.2", sha256="df4394568e2a21ed33f1889a6252f0ec5b8e9fa9e0c20ccf011eafe4da9823f2", url="https://pypi.org/packages/a1/ee/e8f8dcaf5c3222e77fd794226a2de5b3ce1b72881e765feeca5bc1984cda/pyobjc_framework_Social-9.2-py2.py3-none-any.whl")
    version("9.1.1", sha256="967146838af3e2e35f8dbf2d87c5b610f72cad74810ed49be31f1aa3b3f67559", url="https://pypi.org/packages/93/e8/21c67fe6263e210a9e240907991dd95943ffdd93f8bd6bce3bf6f32462dd/pyobjc_framework_Social-9.1.1-py2.py3-none-any.whl")
    version("9.1", sha256="93df2e7f63ed173bb9a54eadf125f04c992e3243f059a95f59e7b09db4a61662", url="https://pypi.org/packages/83/47/0332c64ac4e7bdb5f05c9c6ec5c96520d44dda7b5c106a08d7108f5e7c43/pyobjc_framework_Social-9.1-py2.py3-none-any.whl")
    version("9.0.1", sha256="fd5395ab95c271514f6befe0023c49636853efb32156408d9df9423fdd7bd75c", url="https://pypi.org/packages/51/e9/4769c40c60fccc36c57f5bcef955804fc6cf891015c52b1cc3386a3a7dd3/pyobjc_framework_Social-9.0.1-py2.py3-none-any.whl")
    version("9.0", sha256="3cb4cd0310ccd906ebdd5a8df455e7ebef20c1ada3f943dcbdc3dc6dc1270143", url="https://pypi.org/packages/f3/07/41935079a0f4785819b073fda9f56c85e67c5b96f9a607f0d743d9b1a7a8/pyobjc_framework_Social-9.0-py2.py3-none-any.whl")
    version("8.5.1", sha256="bc1af1fa162e59bfa8d8853ff1b69ac8064b120d10ff6ead54a7bf0eca464842", url="https://pypi.org/packages/16/36/e051ae3dc03951edd94991f554bf2600cf0aa4f49298c0ae96d2392ff0f8/pyobjc_framework_Social-8.5.1-py2.py3-none-any.whl")
    version("8.5", sha256="2394f0f772bd6b22b176ce5ecf454a317a25e90d7e824a648fa110ae2fe3142d", url="https://pypi.org/packages/ac/c8/5cd9bc2a9f6a40d0fbbba746f4900dc18e51a2d269ce41621aeedeb168f2/pyobjc_framework_Social-8.5-py2.py3-none-any.whl")
    # END VERSIONS

    # BEGIN VARIANTS
    # END VARIANTS
    # BEGIN DEPENDENCIES
    with default_args(type="run"):
        depends_on("py-pyobjc-core@10.2:", when="@10.2:")
        depends_on("py-pyobjc-core@10.1:", when="@10.1")
        depends_on("py-pyobjc-core@10:", when="@10:10.0")
        depends_on("py-pyobjc-core@9.2:", when="@9.2:9")
        depends_on("py-pyobjc-core@9.1.1:", when="@9.1.1:9.1")
        depends_on("py-pyobjc-core@9.1:", when="@9.1:9.1.0")
        depends_on("py-pyobjc-core@9.0.1:", when="@9.0.1:9.0")
        depends_on("py-pyobjc-core@9:", when="@9:9.0.0")
        depends_on("py-pyobjc-core@8.5.1:", when="@8.5.1:8")
        depends_on("py-pyobjc-core@8.5:", when="@8.5:8.5.0")
        depends_on("py-pyobjc-framework-cocoa@10.2:", when="@10.2:")
        depends_on("py-pyobjc-framework-cocoa@10.1:", when="@10.1")
        depends_on("py-pyobjc-framework-cocoa@10:", when="@10:10.0")
        depends_on("py-pyobjc-framework-cocoa@9.2:", when="@9.2:9")
        depends_on("py-pyobjc-framework-cocoa@9.1.1:", when="@9.1.1:9.1")
        depends_on("py-pyobjc-framework-cocoa@9.1:", when="@9.1:9.1.0")
        depends_on("py-pyobjc-framework-cocoa@9.0.1:", when="@9.0.1:9.0")
        depends_on("py-pyobjc-framework-cocoa@9:", when="@9:9.0.0")
        depends_on("py-pyobjc-framework-cocoa@8.5.1:", when="@8.5.1:8")
        depends_on("py-pyobjc-framework-cocoa@8.5:", when="@8.5:8.5.0")
    # END DEPENDENCIES

