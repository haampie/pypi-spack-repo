# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyPyobjcFrameworkNetfs(PythonPackage):
    # BEGIN VERSIONS [WHEEL ONLY]
    version("10.2", sha256="e7a84497be6114ea2e47776efda640d9d8becaaa07214d712a204b5d446e3d95", url="https://pypi.org/packages/c3/78/57ff272aab896719554c1ea53395290ec8554a897097ddf80490179344a9/pyobjc_framework_NetFS-10.2-py2.py3-none-any.whl")
    version("10.1", sha256="a317c30a367af22f94858ca73cfe38a0dc4b63d0783f93532cb33780cd98a942", url="https://pypi.org/packages/04/44/c73954b7daaea71243320e81d309ea8df9c06581f1a6bd00d39ee215398f/pyobjc_framework_NetFS-10.1-py2.py3-none-any.whl")
    version("10.0", sha256="1ad29eb81bd4774259377a716fa3dd8b3e105e5f8021e295f640a8e036847cc0", url="https://pypi.org/packages/13/e8/e0f79b25b30228208a6d52f83275a0aa15d1648f7aaa14f303a69f80be41/pyobjc_framework_NetFS-10.0-py2.py3-none-any.whl")
    version("9.2", sha256="01fbc6f9dde19b5e0cd09d788d3072b592a5a0870132b7a4adb373684192d6e9", url="https://pypi.org/packages/23/5e/e729c256d13996ec3e1370217a50f8fb4722687c44d43623941ae63d3232/pyobjc_framework_NetFS-9.2-py2.py3-none-any.whl")
    version("9.1.1", sha256="05a0a32c0c27b8534de0462e8ecde0a6a2da675741d4d8b77c42741b7a018b4c", url="https://pypi.org/packages/be/26/7f648780fef5acbce81eb1fa44d953623851877965377d6ec65427a12fa4/pyobjc_framework_NetFS-9.1.1-py2.py3-none-any.whl")
    version("9.1", sha256="e87863a05c28f84dd6c14a51bde771e3ec31e4295bd81db310eb0a91e11e7c74", url="https://pypi.org/packages/10/53/9a72eda0cf3fa8d7bd8ecf61cd92ac6b94c794df216a9b1ba588d2f3429e/pyobjc_framework_NetFS-9.1-py2.py3-none-any.whl")
    version("9.0.1", sha256="30cce80d89a7e28e7139b7b46ef7df76f8417e277cdcfe87366666a76d94163a", url="https://pypi.org/packages/d8/57/7e00c71785f09bf7629b5c9a740b51e52258d6a1c051dca49c941fb38381/pyobjc_framework_NetFS-9.0.1-py2.py3-none-any.whl")
    version("9.0", sha256="4fa1adeb2cb7f251467cbd69449e9b18f8f87ef48a25517b378fad0094a10a82", url="https://pypi.org/packages/1a/20/b1165be692d922a544c6b835d8a770920ab83f3eb2ea1883f898f4f67d2c/pyobjc_framework_NetFS-9.0-py2.py3-none-any.whl")
    version("8.5.1", sha256="69574fe07fd9cb094a873edb8464466d1c5367027f8d2d6f00d82101e1501446", url="https://pypi.org/packages/f3/08/0980b34730d4933e56f8f720f2bdce8d188d79f10708ce8895751f8d9427/pyobjc_framework_NetFS-8.5.1-py2.py3-none-any.whl")
    version("8.5", sha256="9823def9da58b2f67f5c40193f01da621513a1add6328dde024417f4dc302281", url="https://pypi.org/packages/28/bc/c359787076bb4ce7a09b4c983658bb5f8bd3cdbc715e83fcc80ed2b5a108/pyobjc_framework_NetFS-8.5-py2.py3-none-any.whl")
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

